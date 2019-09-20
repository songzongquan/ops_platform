#!/usr/bin/python3
# encoding:utf8

import pymysql

class Virhost:

    __init__(self,ip,state,instant_name,os,root_pass,purpose,depart,owner,phone,email,memo):
        self.ip=ip
        self.state=state
        self.instant_name=instant_name
        self.os = os
        self.root_pass = root_pass
        self.purpose = purpose
        self.depart = depart
        self.owner = owner
        self.phone = phone
        self.email = email
        self.memo = memoa

    __init__(self,dbutil):
        self.dbutil = dbutil
    
    insert(self,virhost):
        sql = '''insert into vir_host(ip,
                                      state,
                                      instant_name,
                                      os,
                                      root_pass,
                                      purpose,
                                      depart,
                                      owner,
                                      phone,
                                      email,
                                      memo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        params = (self.ip,self.state,self.instant_name,self.os,self.root_pass,self.purpose,self.depart,self.owner,self.phone,self.email,self.memo)
        
        self.dbutil.update(sql,params)

    delete(id):
        pass
    update():
        pass
    

