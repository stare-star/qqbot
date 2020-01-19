'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: SqlHelper.py
@time: 2020-01-16 19:55
@desc:
'''
# 数据库内容封装

import time

import pytz
from sqlalchemy import Column, String, Integer, DateTime, func
from config import url_sql
from sqlalchemy import create_engine, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# engine = create_engine(url_sql)
Base = declarative_base()





class bot_speak(Base):
    __tablename__ = 'bot_speak'
    id = Column(Integer, primary_key=True)
    question = Column(String(255), nullable=True)
    answer = Column(String(255), nullable=True)
    user_id = Column(String(255), nullable=True)


    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.question)

class bot_speakExer(object):
    def __init__(self):
        engine = create_engine(url_sql)
        # Base = declarative_base()
        Session = sessionmaker(bind=engine)
        self.session = Session()
    # 添加问答句
    def insertQuestionAndAnswer(self, question, answer, userId):
        qa = bot_speak(question=question,answer=answer,user_id=userId)
        print(qa)
        self.session.add(qa)
        self.session.commit()
        return qa
    # 查询问答句
    def selectQuestion(self,question):
        qa = self.session.query(bot_speak).filter_by(question=question).all()
        return qa
    def deleteQuestion(self,question):
        qa = self.session.query(bot_speak).filter_by(question=question).delete(synchronize_session=False)
        self.session.commit()
        return qa
    def deleteQuestionByid(self,id):
        qa = self.session.query(bot_speak).filter_by(id=id).delete(synchronize_session=False)
        self.session.commit()
        return qa

#
if __name__ == '__main__':
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    s=bot_speakExer()
    # s.insertQuestionAndAnswer("jfwe非ej","jn","jhj")
    print(s.deleteQuestion("12"))
# import mysql.connector
#
#
#     class SqlHelper:
#         # 数据库连接
#         conn = mysql.connector.connect(user='root', password='123456', database='ChickenBotDataBase')
#         cursor = conn.cursor()

    # # 查询指定 user_id 是否存在，不存在返回false，存在返回true
    # def selectUserId(self, userId):
    #     sql = 'SELECT * FROM user_info WHERE User_Id =' + str(userId)
    #     self.cursor.execute(sql)
    #     value = self.cursor.fetchone()
    #     if value is None:
    #         return False
    #     else:
    #         return True
    #
    # # 签到用的方法，给User_Sign+1
    # def updateUserSign(self, userId):
    #     sql = 'UPDATE user_info SET User_Sign = User_Sign + 1,User_SignedToday = 1 WHERE User_Id = ' + str(userId)
    #     self.cursor.execute(sql)
    #     self.conn.commit()
    #
    # # 更新用户昵称
    # def updateUserNickName(self, userId, nickName):
    #     sql = 'UPDATE user_info SET User_NickName = \'' + str(nickName) + '\'WHERE User_Id =' + str(userId)
    #     self.cursor.execute(sql)
    #     self.conn.commit()
    #
    # # 添加新用户
    # def addNewUser(self, userId, groupId, nickName):
    #     # sql = 'INSERT INTO user_info VALUE (' + str(userId) + ',1,0,1,' + str(groupId) + '\'' + str(nickName) + '\')'
    #     sql = 'INSERT INTO user_info VALUES (' + str(userId) + ',1,0,1,' + str(groupId) + ',\'' + str(nickName) + '\')'
    #     self.cursor.execute(sql)
    #     self.conn.commit()
    #
    # # 查询用户签到和被封禁信息
    # def selectUserInfo(self, userId):
    #     sql = 'SELECT * FROM user_info WHERE User_Id = ' + str(userId)
    #     self.cursor.execute(sql)
    #     values = self.cursor.fetchone()
    #     return values
    #
    # # 增加用户的sleep时间
    # def addUserSleep(self, userId, number):
    #     sql = 'UPDATE user_info SET User_Sleep = User_Sleep + ' + str(number) + ' WHERE User_Id = ' + str(userId)
    #     self.cursor.execute(sql)
    #     self.conn.commit()
    #
    # # 查看sleep排行
    # def selectUserSleepRank(self, groupId):
    #     sql = 'SELECT User_Id,User_NickName,User_Sleep FROM user_info WHERE Group_id = ' + '\'' + str(
    #         groupId) + '\'' + 'ORDER BY User_Sleep DESC '
    #     self.cursor.execute(sql)
    #     values = self.cursor.fetchall()
    #     return values

