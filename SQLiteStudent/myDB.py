# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 21:15:25 2019

@author: Administrator
"""
import sqlite3
class DBclass:
 def __init__(self, connStr):
     self.myConn = sqlite3.connect(connStr)
 def getSQLresult(self, sqlstr):
    resultset = self.myConn.execute(sqlstr).fetchall()
    return resultset

 def execSQLcommand(self, sqlstr):
    global myConn
    global myCursor
    try:
      myCursor = self.myConn.execute(sqlstr)
      self.myConn.commit()
      print("指令已成功執行:" + sqlstr)    
    except Exception as ex:
      print("指令有誤:", sqlstr, ex)
 def getStringItem(item_no, instr, sep):
     return str(instr).split(sep)[item_no]     
 
 def showitem(value, valueset, sep):
     for idx, item in enumerate(valueset,0):
         if value == getStringItem(0,item[0],sep):
             return item
 def Qo(self, instr):
    return "'" + instr.strip() + "'"
        
