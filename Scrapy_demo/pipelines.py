# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from Scrapy_demo.db_tools.Demo_SQLALchemy import Demo

class DemoPipeline():

    def __init__(self):
        self.user = 'root'
        self.password = '123456'
        self.host = '127.0.0.1'
        self.port = '3306'
        self.table = 'Spiders'

    def process_item(self,item,spider):
        engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(self.user,self.password,self.host,self.port,self.table),encoding='utf-8')
        Session = sessionmaker(bind=engine)
        session = Session()
        obj = Demo(
            title = item['title'],
            start_addr = item['start_addr'],
            days = item['days'],
            attr = item['attr'],
            price = item['price'],
        )
        session.add(obj)
        session.commit()