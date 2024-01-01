from flask import Flask, abort, render_template, request, jsonify, redirect
import json
import sqlalchemy
from sqlalchemy import select
from db import User,add_user_data,engine
from sqlalchemy.orm import sessionmaker, Session
app = Flask(__name__)

Session = sessionmaker(bind=engine)
session = Session()
session.rollback()
@app.route('/',methods=['GET','POST'])
def get():    
    users = session.query(User).all()
    return render_template('index.html',result=users)
#def filter():
#    if request.method=='POST':
#        filter=request.form.get('filter')
#        users = session.query(User).order_by(User.name.filter).all()
#        return render_template('index.html',filter=filter,users=users)

@app.route('/add',methods=['GET','POST'])

def add():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        sex = request.form.get('sex')
        education = request.form.get('education')
        email_id = request.form.get('email_id')
        phone_no = request.form.get('phone_no')
        address = request.form.get('address')
        result = {
            'name':name,
            'age': age,
            'sex': sex,
            'education': education,
            'email_id': email_id,
            'phone_no': phone_no,
            'address': address
        }        
        add_user_data([result])        
        print(result)
        message = 'User Added'
        return render_template('add.html',Add=result, message=message)

@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):    
    users = session.query(User).filter_by(id=id).first()        
    if request.method=='POST':    
        if users:            
            users.name = request.form.get('name')
            users.age = request.form.get('age')
            users.sex = request.form.get('sex')
            users.education = request.form.get('education')
            users.email_id = request.form.get('email_id')
            users.phone_no = request.form.get('phone_no')
            users.address = request.form.get('address')                                                                                          
            session.commit()        
            return render_template('edit.html',users=users)
    print(users)
    session.expunge_all()            
    return render_template('edit.html',users=users)

@app.route('/delete/<int:id>',methods=['GET','POST'])
def delete(id):        
    users = session.query(User).filter_by(id=id).first()
    print(id)
    if request.method =='POST' :
            session.delete(users) 
            session.commit()
            return redirect('/')                            
    return render_template('delete.html',id=id)

@app.route('/search',methods=['GET','POST'])
def search():
    if request.method=='POST':        
        name=request.form.get("name")
        print(name)
        if name:
            users = session.query(User).filter(User.name.like(name)).all()
            return render_template('search.html',users=users, name=name)
    return render_template('search.html',users=users, name=name)

if __name__ == '__main__':
    app.run(debug=True)
