# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:01:45 2019

@author: clark
"""
import sys
from tkinter import *
import myDB
db = myDB.DBclass("student.db")

def getAllData():
    sqlstr = " select dep_id, dep_name "
    sqlstr += "  from department "
    
    #myset = list()
    myset = db.getSQLresult(sqlstr)
    datalist.delete(0,END)
    for idx, item in enumerate(myset, 0):
        #datalist.insert(END,"{0}-{1}-{2}".format(item[0],item[1], item[2]))
        datalist.insert(END, item)
def getitem(evt):
    selecteditem = datalist.get(datalist.curselection()[0])
    #selectedlist = selecteditem.split('-')
    #=== std_id ===
    dep_id = selecteditem[0]
    dep_name = selecteditem[1]
    
    edep_id.delete(0,END)
    edep_name.delete(0,END)
    edep_id.insert(END, dep_id)
    edep_name.insert(END, dep_name)
    
    
win = Tk()
win.geometry("600x520")
win.title('學系資料維護畫面')
win.config(background="lightyellow")
#-------
   
    

    
queryAll = Button(win)
queryAll.config(text="全部資料", bg="gray", fg="white", width=10, height=2, font="標楷體14", command=getAllData)
queryAll.grid(row=0, column=0, stick=W)
#--------
datalist = Listbox(win)
datalist.bind('<<ListboxSelect>>', getitem)
datalist.config(width=80, height=15)
datalist.grid(row=1, column=0, columnspan=4)

#------
myScrollbar = Scrollbar(win)
myScrollbar.grid(row=1, column=4, stick=N+S)
myScrollbar.config(command=datalist.yview)
#====================================================
#課號--------------------------
ldep_id = Label(win, text="Dep_Id")
ldep_id.grid(row=2, column=0)
edep_id = Entry(win)
edep_id.grid(row=2, column=1, stick=W+E)
#系名----------------------------
ldep_name = Label(win, text="Dep Name")
ldep_name.grid(row=2, column=2)
edep_name = Entry(win)
edep_name.grid(row=2, column=3, stick=W+E)

#=====================
opFrame = Frame(win)
opFrame.grid(row=6, column=0, columnspan=4, stick=W+E)
#
def InsertData():
    sqlstr = " insert into department(dep_Id, dep_Name)values("
    sqlstr +=db.Qo(edep_id.get()) + ","
    sqlstr +=db.Qo(edep_name.get()) + ")"
    
    db.execSQLcommand(sqlstr)
    getAllData()
    
opInsert = Button(opFrame)
opInsert.config(text="新增", bg="gray", fg="blue", width=10, height=2, font="標楷體14", command=InsertData)
opInsert.grid(row=0, column=0, stick=W+E)
def UpdateData():
    sqlstr = " update department set " # (Std_Id, Std_Name, sex, dep_id, Birth_Place, Birthday, Religion)values("
    sqlstr += "dep_name = " + db.Qo(edep_name.get()) 
    sqlstr += " where dep_id = " +db.Qo(edep_id.get())
    db.execSQLcommand(sqlstr)
    getAllData()
opUpdate = Button(opFrame)
opUpdate.config(text="修改", bg="gray", fg="blue", width=10, height=2, font="標楷體14", command=UpdateData)
opUpdate.grid(row=0, column=1, stick=W+E)
#
def DeleteData():
    sqlstr = "delete from department where dep_id = " +db.Qo(edep_id.get())
    db.execSQLcommand(sqlstr)
    getAllData()

opDelete = Button(opFrame)
opDelete.config(text="刪除", bg="gray", fg="blue", width=10, height=2, font="標楷體14", command=DeleteData)
opDelete.grid(row=0, column=2, stick=W+E)

win.mainloop() 