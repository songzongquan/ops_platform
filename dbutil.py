#!/usr/bin/python3
#encoding:utf-8

import pymysql

class DBUtil:
    
    '''构造方法 '''
    
    def __init__(self,host,user,passwd,dbname):
        self.host = host
        self.user = user
        self.password = passwd
        self.dbname = dbname
    '''打开连接 '''
    def openConn(self):
        self.conn = pymysql.connect(host=self.host,user=self.user, password=self.password, database=self.dbname, charset='utf8')        
        self.cursor = self.conn.cursor()
    '''关闭连接'''
    def closeConn(self):
        self.cursor.close()
        self.conn.close()
    '''查询  sql为字串，params为参数元组'''
    def query(self,sql,params):
        self.openConn()
        query = (sql)
        
        self.cursor.execute(query,params)
        result = self.cursor.fetchall()
        
        self.closeConn()
        return result
    '''插入，删除，更新 '''
    def update(self,sql,params):
        self.openConn()
        query = (sql)
        self.cursor.execute(query,params)
        self.conn.commit()
        self.closeConn()
    ''' 批量更新，即一次执行多个语句  ，sql_params为一个list，其元素为dict, dict中，KEY 为“sql”的值为sql语句，KEY为params的值为参数列表元组 '''
    def batchUpdate(self,sql_params):
        self.openConn()
        for sql_param in sql_params:
            query = (sql_param['sql'])
            params = sql_param['params']
            self.cursor.execute(query,params)

        
        self.conn.commit()
        self.closeConn()



