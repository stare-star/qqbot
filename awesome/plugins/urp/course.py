from sqlalchemy import Column, String, Integer
from config import url
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine(url)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Courses(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    student_id= Column(String(255), nullable=True)
    course_id = Column(String(255), nullable=True)
    number = Column(String(255), nullable=True)
    name = Column(String(255), nullable=True)
    english_name = Column(String(255), nullable=False)
    credit = Column(String(255), nullable=False, index=True)
    attr = Column(String(255), nullable=False, index=True)
    mark = Column(String(255), nullable=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.number)


def add_info(course_id,
             student_id,
             number,
             name,
             english_name,
             credit,
             attr,
             mark
             ):
    print(course_id,
          student_id,
          number,
          name,
          english_name,
          credit,
          attr,
          mark)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = Courses(course_id=course_id,
                     student_id=student_id,
                     number=number,
                     name=name,
                     english_name=english_name,
                     credit=credit,
                     attr=attr,
                     mark=mark)
    session.add(result)
    session.commit()
    session.close()

def update_info():
    pass
def get_info(id):
    pass

if __name__ == '__main__':

    Base.metadata.create_all(engine)
    add_info(1,2 ,5,5,6,7,887,8)

