# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:41:21 2020

@author: Administrator
"""

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
def  qo(instr):
     return "'" + instr +"'"
def getAll():
    sqlstr = "select * from water "
    listx = execSQLcommand(sqlstr).fetchall()
    resultList.delete(0, END)
    for item in listx:
        contentx =  "站名:" + item[0] + ",pH值:" + str(item[1]) + ",濁度:" + str(item[2]) + ',餘氯:' + str(item[3] )
        resultList.insert(END, contentx)
myConn = sqlite3.connect("myData.db")
myCursor = myConn.cursor()

win = Tk()
win.geometry('500x500')
win.title("單筆編輯")
lblstation_name = Label(win, text='淨水場名稱:')
lblstation_name.grid(row=0, column=0)
etystation_name=Entry(win)
etystation_name.grid(row=0, column=1)

lblpHvalue = Label(win, text='pH值:')
lblpHvalue.grid(row=1, column=0)
etypHvalue=Entry(win)
etypHvalue.grid(row=1, column=1)

lblturbidity = Label(win, text='濁度')
lblturbidity.grid(row=2, column=0)
etyturbidity=Entry(win)
etyturbidity.grid(row=2, column=1)

lblresidual_chlorine = Label(win, text='餘氯')
lblresidual_chlorine.grid(row=3, column=0)
etyresidual_chlorine=Entry(win)
etyresidual_chlorine.grid(row=3, column=1)

btnSelectAll = Button(win, text='Query', command=getAll)
btnSelectAll.grid(row=4, column=0, columnspan=3, sticky=W+E)

def doInsert():
     sqlstr = "insert into water(station_name, pH_value, turbidity, residual_chlorine) values("
     sqlstr +=  qo(etystation_name.get()) + ","
     sqlstr +=  etypHvalue.get() + ","
     sqlstr +=  etyturbidity.get() + ","
     sqlstr += etyresidual_chlorine.get() + ")"
     execSQLcommand(sqlstr)
     getAll()
def doUpdate():
    sqlstr = " update water set"
    sqlstr += " pH_value = " + etypHvalue.get()
    sqlstr += ", turbidity = " + etyturbidity.get()
    sqlstr += ", residual_chlorine = " + etyresidual_chlorine.get()
    sqlstr += " where station_name = " +  qo(etystation_name.get())
    execSQLcommand(sqlstr)
    getAll()
def doDelete():
    sqlstr = " delete from water"
    sqlstr += " where station_name = " +  qo(etystation_name.get())
    execSQLcommand(sqlstr)
    getAll()
btnInsert = Button(win, text='Insert', fg='blue', command=doInsert)
btnInsert.grid(row=0,column=2, sticky=W+E)
btnUpdate = Button(win, text='Update', fg='blue', command=doUpdate)
btnUpdate.grid(row=1,column=2, sticky=W+E)
btnDelete = Button(win, text='Delete', fg='blue', command=doDelete)
btnDelete.grid(row=2,column=2, sticky=W+E)

def onselect(evt):
    idx = resultList.curselection()[0]
    selecteditem = resultList.get(idx) #tuple selected
    dataArray = selecteditem.split(',')
    item1 = dataArray[0].split(':')[1]
    item2 = dataArray[1].split(':')[1]
    item3 = dataArray[2].split(':')[1]
    item4 = dataArray[3].split(':')[1]

    
    etystation_name.delete(0, END);  
    etystation_name.insert(0, item1 )

    etypHvalue.delete(0, END); 
    etypHvalue.insert(0, item2 )
    
    etyturbidity.delete(0, END); 
    etyturbidity.insert(0, item3)
    
    etyresidual_chlorine.delete(0, END); 
    etyresidual_chlorine.insert(0, item4)

resultList = Listbox(win)
resultList.grid(row=5, column=0, columnspan=3, sticky=W+E)
resultList.bind('<<ListboxSelect>>', onselect)
scrollresult = Scrollbar(win, command=resultList.yview)
scrollresult.grid(row=5, column=3, sticky=N+S)
getAll()




win.mainloop()