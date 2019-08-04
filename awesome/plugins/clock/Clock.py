'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: Clock.py
@time: 2019-08-04 11:06
@desc:
'''
import time

import pytz
from sqlalchemy import Column, String, Integer, DateTime, func
from config import url
from sqlalchemy import create_engine, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine(url)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Clock(Base):
    __tablename__ = 'clocks'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=True)
    status = Column(String(25), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    records = relationship('ClockRecord', backref="clock")

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)


class ClockRecord(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    clock_id = Column(Integer, ForeignKey('clocks.id'))
    time = Column(DateTime(255), nullable=False)
    mark = Column(String(255), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.time)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    qq = Column(String(255), nullable=True)

    clocks = relationship('Clock', backref="user")

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.qq)


def add_user(qq):
    user = User(qq=qq)
    session.add(user)
    session.commit()
    return user


def add_clock(name, user_id):
    clock = Clock(name=name, user_id=user_id, status="1")
    session.add(clock)
    session.commit()
    return clock


def add_clock_record(clock_id,
                     user_id,
                     mark="无"
                     ):
    now = int(time.time())
    time_array = time.localtime(now)
    now = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    print(now)
    record = ClockRecord(
        clock_id=clock_id,
        time=now,
        user_id=user_id,
        mark=mark)
    session.add(record)
    session.commit()
    return record


def update_info():
    pass


def get_info(id):
    pass


if __name__ == '__main__':
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)

    # add_clock("熬夜",1123)
    # user=add_user(123)
    # add_clock("e",user.id)
    # clock = session.query(Clock).filter_by(name="b").first()
    # if clock is None:
    #   print(clock)
    # qq = 1023256421
    # user = session.query(User).filter_by(qq=qq).first()
    #
    # res = user.clocks
    # print(res[0].name)
    # num = session.query(ClockRecord).filter_by(clock_id=res[0].id).count()
    # last_time = session.query(func.max(ClockRecord.time)).filter_by(clock_id=res[1].id).scalar()
    # print(last_time)
    now = int(time.time())
    time_array = time.localtime(now)
    now = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    print(now)