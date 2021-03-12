# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:01:45 2019

@author: clark
"""
import os
import sys
from tkinter import *
import myDB
db = myDB.DBclass("student.db")

def getAllData():
    sqlstr = " select r.std_id, s.std_name, r.course_id, c.course_name, r.rcd "
    sqlstr += "  from record r, course c, student s"
    sqlstr += "  where r.std_id = s.std_id "
    sqlstr += "    and r.course_id = c.course_id " 
    
    
    myset = db.getSQLresult(sqlstr)
    
    datalist.delete(0,END)
    for idx, item in enumerate(myset, 0):
        #print(type(item))
        datalist.insert(END, item)
def getitem(evt):
    selecteditem = datalist.get(datalist.curselection()[0])
    
    #=== std_id ===
    std_id = selecteditem[0]
    for idx, item in enumerate(stdset,0):
        if std_id == item[0]:
            #stdvar.set(stdset[idx])
            stdvar.set(item)   #item is a tuple,  stdvar is a StringVar
    
    #=== course_id
    course_id = selecteditem[2]
    for idx, item in enumerate(courseset,0):
        if course_id == item[0]:
            coursevar.set(courseset[idx])
    
    #===record
    rcd =  selecteditem[4]    
    ercd.delete(0,END)
    ercd.insert(END, rcd)
def preparedepList():
    global depset
    
    sqlstr =  'select dep_id, Dep_Name'
    sqlstr += ' from department '
    depset = db.getSQLresult(sqlstr)  #temp is list as [(dep_id, dep_name), (tuple),...,(tuple)]    
def preparestdList(stdset):
    dep_id = depvar.get()[1:-1].split(',')[0]
    sqlstr =  'select std_id , std_name '
    sqlstr += ' from student '
    sqlstr += ' where dep_id= ' + dep_id
    temp = db.getSQLresult(sqlstr)
    for item in temp:
        stdset.append(item)
        
def preparecourseList():
    global courseset
    sqlstr =  'select course_id , course_name '
    sqlstr += ' from course '
    courseset = db.getSQLresult(sqlstr)
    #for item in temp:
    #    courseset.append(item)
        
def getSexValue():
    print("sex:",  varSex.get() )

#def redirect_to_file(text):
#    original = sys.stdout
#    sys.stdout = open('main.py', 'w')
#    print('This is your redirected text:')
#    print(text)
#    sys.stdout = original
 
#    print('This string goes to stdout, NOT the file!')


if __name__ == '__main__':
   import tkinter.filedialog
   #print(__name__)
   os.system('main.py') 
   sys.exit(0) #離開此程式
   #pyexec = sys.executable
   #PathPy = tkinter.filedialog.askopenfilename(title="Open a file",filetypes=[('PYTHON file','.py')])
   #os.system('%s %s' % (sys.executable, 'main.py'))
   #sys.exit(0)
 
winr = Tk()
winr.geometry("600x520")
winr.title('成績資料維護畫面')
winr.config(background="lightyellow")
#-------

       
queryStd = Button(winr)
queryStd.config(text="全部學生", bg="gray", fg="white", width=10, height=2, font="標楷體14", command=getAllData)
queryStd.grid(row=0, column=0, stick=W)
#--------
datalist = Listbox(winr)
datalist.bind('<<ListboxSelect>>', getitem)
datalist.config(width=80, height=15)
datalist.grid(row=1, column=0, columnspan=4)

#------
myScrollbar = Scrollbar(winr)
myScrollbar.grid(row=1, column=4, stick=N+S)
myScrollbar.config(command=datalist.yview)
#====================================================
#學系-----------------------------
def getdepListClick(evt):
    dep_id = depvar.get()[1:-1].split(',')[0]
    global stdset
    sqlstr =  'select std_id , std_name '
    sqlstr += ' from student '
    sqlstr += ' where dep_id = ' + dep_id    
    stdset = db.getSQLresult(sqlstr)
    stdvar.set(stdset[0])
    
ldepartment = Label(winr, text="學系")
ldepartment.grid(row=3, column=0)
depset = list() #depset是list, 元素是 tuple
preparedepList()
depvar = StringVar(winr) #準備 反映點選項目
depvar.set(depset[0]) #預設depList停駐的index
depList  = OptionMenu(winr, depvar, *depset, command=getdepListClick)
depList.grid(row=3, column=1, stick=W+E)
#學生-----------------------------
lstd = Label(winr, text="學生")
lstd.grid(row=4, column=0)
stdset = list()
preparestdList(stdset)
stdvar = StringVar(winr) #準備 反映點選項目
stdvar.set(stdset[0]) #預設depList停駐的index

stdList  = OptionMenu(winr, stdvar, *stdset)
stdList.grid(row=4, column=1, stick=W+E)
#課程----------------------------
lcourse = Label(winr, text="課程")
lcourse.grid(row=4, column=2)
courseset = list()
preparecourseList()
coursevar = StringVar(winr) #準備 反映點選項目
coursevar.set(courseset[0]) #預設depList停駐的index

courseList  = OptionMenu(winr, coursevar, *courseset)
courseList.grid(row=4, column=3, stick=W+E)




#---成績---
lrcd = Label(winr, text="成績")
lrcd.grid(row=5, column=2)
ercd = Entry(winr)
ercd.grid(row=5, column=3, stick=W+E)

#=====================
opFrame = Frame(winr)
opFrame.grid(row=7, column=0, columnspan=4, stick=W+E)
#
def InsertData():
    
    #print(stdvar.get(), '/',  str(stdvar.get())[1:-1].split(',')[0])
    
    sqlstr = " insert into record (Std_Id, course_id, rcd)values("
    sqlstr += str(stdvar.get())[1:-1].split(',')[0] + ","
    sqlstr += str(coursevar.get())[1:-1].split(',')[0] + ","
    sqlstr += ercd.get() + ")"
    db.execSQLcommand(sqlstr)
    getAllData()
    
opInsert = Button(opFrame)
opInsert.config(text="新增", bg="gray", fg="blue", width=10, height=2, font="標楷體14", command=InsertData)
opInsert.grid(row=0, column=0, stick=W+E)
def UpdateData():
    sqlstr = " update record set " # (Std_Id, Std_Name, sex, dep_id, Birth_Place, Birthday, Religion)values("
    sqlstr += " rcd = " + ercd.get()
    sqlstr += " where std_id = " + str(stdvar.get())[1:-1].split(',')[0]
    sqlstr += "   and course_id = " + str(coursevar.get())[1:-1].split(',')[0]

    db.execSQLcommand(sqlstr)
    getAllData()
opUpdate = Button(opFrame)
opUpdate.config(text="修改", bg="gray", fg="blue", width=10, height=2, font="標楷體14", command=UpdateData)
opUpdate.grid(row=0, column=1, stick=W+E)
#
def DeleteData():
    sqlstr = "delete from record where std_id = " + str(stdvar.get())[1:-1].split(',')[0]
    db.execSQLcommand(sqlstr)
    getAllData()

opDelete = Button(opFrame)
opDelete.config(text="刪除", bg="gray", fg="blue", width=10, height=2, font="標楷體14", command=DeleteData)
opDelete.grid(row=0, column=2, stick=W+E)

getAllData()

winr.mainloop() 