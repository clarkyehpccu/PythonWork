# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:41:21 2020

@author: Administrator
"""
import requests
from tkinter import *
import sqlite3
def execSQLcommand(sqlstr):
    global myConn
    global myCursor
    try:
      myCursor = myConn.execute(sqlstr)
      myConn.commit()
      print("指令已成功執行:" + sqlstr)
      return myCursor
    except:
      print("指令有誤:", sqlstr)
myConn = sqlite3.connect("myData.db")
myCursor = myConn.cursor()

win = Tk()
win.geometry('800x500')
win.title('讀取網路資料')

def  qo(instr):
     return "'" + instr +"'"


#----- URL -------------------------------------------
lblURL = Label(win, text='URL:'); lblURL.grid(row=0, column=0)
etyURL = Entry(win, width=80); etyURL.grid(row=0, column=1, columnspan=2, sticky=W+E);
etyURL.insert(0, 'https://quality.data.gov.tw/dq_download_json.php?nid=133578&md5_url=ac39a7025bb0581ceb2eec2a28199191')
#-----讀取 URL 的 JSON 資料---------------------------
def getJson():
    resultList.delete(0, END)
    websource = requests.get(etyURL.get())
    myJson = websource.json()
    for idx , content in enumerate(myJson,0): 
        contentx ="站名:" + content['station_name'] + ",pH值:" + content['pH_value'] + ",濁度:" + content['turbidity'] + ',餘氯:' + content['residual_chlorine'] 
        resultList.insert(END, contentx )

btnSelectAll = Button(win, text='get From URL', fg='blue', command=getJson)
btnSelectAll.grid(row=1, column=0, columnspan=3, sticky=W+E)

    
resultList = Listbox(win, width=80)
resultList.grid(row=2, column=0, columnspan=2, sticky=W+E)
scrollresult = Scrollbar(win, command=resultList.yview)
scrollresult.grid(row=2, column=2, sticky=N+S)
#------輸入至資料庫-------------------------------------
def getAll():
    sqlLiteList.delete(0,END)
    sqlstr = "select * from water "
    listx = execSQLcommand(sqlstr).fetchall()
    for item in listx:
        contentx =  "站名:" + item[0] + ",pH值:" + str(item[1]) + ",濁度:" + str(item[2]) + ',餘氯:' + str(item[3] )
        sqlLiteList.insert(END,contentx)
def doInsert():
    sqlstr = " delete from water "
    execSQLcommand(sqlstr)
    for idx in range(0,resultList.size()):
        selectedStr = resultList.get(idx)
        dataArray = selectedStr.split(',')
        item1 = (dataArray[0].split(':'))[1]
        item2 = (dataArray[1].split(':'))[1]
        item3 = (dataArray[2].split(':'))[1]
        item4 = (dataArray[3].split(':'))[1]
        sqlstr = "insert into water(station_name, pH_value, turbidity, residual_chlorine) values("
        sqlstr +=  qo(item1) + ","
        sqlstr +=  item2 + ","
        sqlstr +=  item3 + ","
        sqlstr += item4 + ")"
        #print(sqlstr)
        execSQLcommand(sqlstr)
        getAll()
# =============================================================================
btnInsert = Button(win, fg='red', text='Insert into Database, and Get from Database', command=doInsert)
btnInsert.grid(row=3,column=0, sticky=W+E, columnspan=3)
sqlLiteList = Listbox(win, width=80)
sqlLiteList.grid(row=4, column=0, columnspan=2, sticky=W+E)
scrollsql = Scrollbar(win, command=sqlLiteList.yview)
scrollsql.grid(row=4, column=2, sticky=N+S)
win.mainloop()