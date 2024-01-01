import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///users.db',echo=True)
class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    sex = Column(String(3))
    education = Column(String(10))
    email_id = Column(String(50))
    phone_no = Column(Integer)
    address = Column(String(100))

Base.metadata.create_all(engine)

def add_user_data(data):
    Session = sessionmaker(bind=engine)
    session = Session()

    for user_info in data:
        new_user = User(
            name = user_info['name'],
            age = user_info['age'],
            sex = user_info['sex'],
            education = user_info['education'],
            email_id = user_info['email_id'],
            phone_no = user_info['phone_no'],
            address = user_info['address']
        )
        session.add(new_user)    
    session.commit()    
    session.close()
