#!/usr/bin/python3
#encoding:utf-8

import unittest

from dbutil import DBUtil

class MyTest(unittest.TestCase):
    def tearDown(self):
        print('当前用例执行后清理...')
              
        sql = 'delete from vir_host'
        params = ()
        self.dbutil.update(sql,params)
              
    def setUp(self):
        print('当前用例执行前初始化...')
        self.dbutil = DBUtil('localhost','root','','ops_db')
    @classmethod
    def tearDownClass(self):
        print('所有用例执行后的清理...')

    @classmethod
    def setUpClass(self):
        print('所有用例执行前的初始...')

    def test_update(self):
        sql = 'insert into vir_host(ip,purpose,type,state,root_pass,depart,owner,email,phone,memo)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        params = ('127.0.0.1',u'测试','test','active','123kissme',u'工业互联网','song','songzongquan@bonc.com.cn','18638217761','haha')
        self.dbutil.update(sql,params)
        
        sql = 'select ip,purpose,type,state,root_pass,depart,owner,email,phone,memo from vir_host where ip = %s'
        params = ('127.0.0.1')
        result = self.dbutil.query(sql,params)
        #print(result)
        
        self.assertEqual('test',result[0][2])

    def test_batchUpdate(self):
        
        sql1 = 'insert into vir_host(ip,purpose,type,state,root_pass,depart,owner,email,phone,memo)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        params1 = ('127.0.0.1',u'测试1','test1','active','123kissme',u'工业互联网','song','songzongquan@bonc.com.cn','18638217761','haha')
        sql2 = 'insert into vir_host(ip,purpose,type,state,root_pass,depart,owner,email,phone,memo)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        params2 = ('127.0.0.2',u'测试2','test2','active','123kissme',u'工业互联网','song','songzongquan@bonc.com.cn','18638217761','haha')     
        
        sql_params = []
        sql_param = {}
        sql_param['sql'] = sql1
        sql_param['params'] = (params1)
        
        sql_params.append(sql_param)
        
        sql_param2 ={}
        
        sql_param2['sql'] = sql2
        sql_param2['params'] = (params2)
        sql_params.append(sql_param2)
                       
        self.dbutil.batchUpdate(sql_params)
        
        sql = 'select count(1) from vir_host '
        params = ()
        result = self.dbutil.query(sql,params)
        
        
        
        self.assertEqual(2,result[0][0])

if __name__ == '__main__':
    unittest.main()
