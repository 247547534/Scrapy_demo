#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index,Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

user = 'root'
password = '123456'
host = '127.0.0.1'
port = '3306'
table = 'Spiders'

engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8".format(user,password,host,port,table),encoding='utf-8',max_overflow=5)

Base = declarative_base()

# 创建单表
class Demo(Base):
    __tablename__ = 'Demo'
    id = Column(Integer, primary_key=True,autoincrement=True,unique=True)
    title = Column(String(64))
    start_addr = Column(String(16))
    attr = Column(String(16),index=True)
    days = Column(String(64),index=True)
    price = Column(String(16))


def init_db():  # 创建表
    Base.metadata.create_all(engine)


def drop_db():  # 删除表
    Base.metadata.drop_all(engine)


# drop_db()
# init_db()
#
#测试添加数据
# session = sessionmaker(bind=engine)
# Session = session()
#
# title = '海拔5276米的邂逅，四姑娘山二姑娘'
# start_addr = '北京'
# attr = '徒步'
# days = '共68期 / 6天行程'
# price = '￥2000'
#
# obj = Demo(
#     title=title,
#     start_addr=start_addr,
#     attr=attr,
#     days=days,
#     price=price
# )
# Session.add(obj)
# Session.commit()

