#!/usr/bin/python3
#encoding:utf8

import pymysql

class DBUtil:

    openConn(self,host,user,passwd,dbname):
        self.conn = pymysql.connect(host=host,user=user, password=password, database=dbname, charset='utf8')        
        self.cursor = self.conn.cursor()

    closeConn(self):
        self.cursor.close()
        self.conn.close()

    query(self,sql):
        pass

    update(self,sql,params):
        self.openConn()
        query = (sql)
        self.cursor.execute(query,params)
        self.conn.commit()
        self.closeConn()

    batchUpdate(self,sql_params):
        self.openConn()
        for sql_param in sql_params:
            query = (sql_param['sql'])
            params = sql_param['params']
            self.cursor.execute(query,params)

        
        self.conn.commit()
        self.closeConn()



