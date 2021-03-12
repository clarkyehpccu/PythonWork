# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:01:45 2019

@author: clark
"""
import sys
from tkinter import *
import myDB
db = myDB.DBclass("student.db")

def getAllStudent():
    sqlstr = " select std_id, Std_Name, dep_id, sex,  religion, birth_place, birthday "
    sqlstr += "  from student"
    
    myset = db.getSQLresult(sqlstr)  #myset is list as [(tuple), (tuple),...,(tuple)]
    datalist.delete(0,END)
    for item in myset:
        datalist.insert(END,item)   
    #for idx, item in enumerate(myset, 0):
    #    datalist.insert(END,"{0}-{1}-{2}-{3}-{4}-{5}-{6}".format(item[0],item[1], item[2], item[3], item[4], item[5], item[6]))
def getitem(evt):
    global depvar
    global sexvar
    selecteditem = datalist.get(datalist.curselection()[0])   #tuple
    #selectedlist = selecteditem.split('-')
    #=== std_id ===
    std_id = selecteditem[0]
    std_name = selecteditem[1]
    estd_id.delete(0,END)
    estd_name.delete(0,END)
    estd_id.insert(0,std_id)
    estd_name.insert(0,std_name)
    #=== dep_id ===
    dep_id = selecteditem[2] #string in tuple   
    for idx, item in enumerate(depset,0): #depset is list as  as [(dep_id, tep_name), (tuple),...,(tuple)]
        #print(type(item))  item is string # item is (tuple)
        if dep_id == item[0]:   
           depvar.set(item)   #item is a tuple,  stdvar is a StringVar           
           break
    #--- end of getitem() --------------------------------   
    #== sex ==    
    sexvar.set(selecteditem[3])
    #-----信仰-----
    religion = selecteditem[4]
    ereligion.delete(0,END)
    ereligion.insert(END, religion)
    #-----出生地-----
    birth_place = selecteditem[5]
    ebirth_place.delete(0,END)
    ebirth_place.insert(END, birth_place)
    #-----生日-----
    birthday = selecteditem[6]
    ebirthday.delete(0,END)
    ebirthday.insert(END, birthday)
def preparedepList():
    global depset
    sqlstr =  'select dep_id, Dep_Name'
    sqlstr += ' from department '
    depset = db.getSQLresult(sqlstr)  #temp is list as [(dep_id, dep_name), (tuple),...,(tuple)]

def getSexValue():
    global sexbar
    print("sex:",  sexvar.get() )

def redirect_to_file(text):
    original = sys.stdout
    sys.stdout = open('/path/to/redirect.txt', 'w')
    print('This is your redirected text:')
    print(text)
    sys.stdout = original
 
    print('This string goes to stdout, NOT the file!')
#if __name__ != '__main__':
#   redirect_to_file('Back to main')    
#print(__name__)    
win1 = Tk()
win1.geometry("600x520")
win1.title('學生資料維護畫面')
win1.config(background="lightyellow")
#-------
   
    

    
queryStd = Button(win1)
queryStd.config(text="全部學生", bg="gray", fg="white", width=10, height=2, font="標楷體14", command=getAllStudent)
queryStd.grid(row=0, column=0, stick=W)
#--------
datalist = Listbox(win1)
datalist.bind('<<ListboxSelect>>', getitem)
datalist.config(width=80, height=15)
datalist.grid(row=1, column=0, columnspan=4)

#------
myScrollbar = Scrollbar(win1)
myScrollbar.grid(row=1, column=4, stick=N+S)
myScrollbar.config(command=datalist.yview)
#====================================================
#學號--------------------------
lstd_id = Label(win1, text="Std_Id")
lstd_id.grid(row=2, column=0)
estd_id = Entry(win1)
estd_id.grid(row=2, column=1, stick=W+E)
#姓名----------------------------
lstd_name = Label(win1, text="Std Name")
lstd_name.grid(row=2, column=2)
estd_name = Entry(win1)
estd_name.grid(row=2, column=3, stick=W+E)
#學系-----------------------------
def getdepListClick(evt):
    print(depvar.get())
ldepartment = Label(win1, text="學系")
ldepartment.grid(row=3, column=0)
depset = list() #depset是list, 元素是 tuple
preparedepList()
depvar = StringVar(win1) #準備 反映點選項目
depvar.set(depset[0]) #預設depList停駐的index
depList  = OptionMenu(win1, depvar, *depset, command=getdepListClick)
depList.grid(row=3, column=1, stick=W+E)

#性別----------------------------

lsex = Label(win1, text="性別")
lsex.grid(row=3, column=2)
sexFrame = Frame(win1)
sexFrame.grid(row=3, column=3, stick=W+E)

sexvar = StringVar(win1)
sexvar.set('M')
radioM = Radiobutton(sexFrame,text="男", variable=sexvar, value = "M", command=getSexValue)
radioM.grid(row=0, column=0, sticky=W)
radioF = Radiobutton(sexFrame,text="女", variable=sexvar, value = "F", command=getSexValue)
radioF.grid(row=0, column=1, sticky=W)

#---信仰----
lreligion = Label(win1, text="信仰")
lreligion.grid(row=4, column=0)
ereligion = Entry(win1)
ereligion.grid(row=4, column=1, stick=W+E)
#--生日---
lbirthday = Label(win1, text="生日")
lbirthday.grid(row=4, column=2)
ebirthday = Entry(win1)
ebirthday.grid(row=4, column=3, stick=W+E)

 #--生日---
lbirth_place = Label(win1, text="居住地")
lbirth_place.grid(row=5, column=2)
ebirth_place = Entry(win1)
ebirth_place.grid(row=5, column=3, stick=W+E)

#=====================
opFrame = Frame(win1)
opFrame.grid(row=6, column=0, columnspan=4, stick=W+E)
#
def InsertStd():
    sqlstr = " insert into student (Std_Id, Std_Name, sex, dep_id, Birth_Place, Birthday, Religion)values("
    sqlstr +=db.Qo(estd_id.get()) + ","
    sqlstr +=db.Qo(estd_name.get()) + ","
    sqlstr +=db.Qo(varSex.get()) + ","
    sqlstr +=db.Qo(str(depvar).split(':')[0]) + ","
    sqlstr +=db.Qo(ebirth_place.get()) + ","
    sqlstr +=db.Qo(ebirthday.get()) + ","
    sqlstr +=db.Qo(ereligion.get()) + ")"
    db.execSQLcommand(sqlstr)
    getAllStudent()
    
opInsert = Button(opFrame)
opInsert.config(text="新增", bg="gray", fg="blue", width=10, height=2, font="標楷體14", command=InsertStd)
opInsert.grid(row=0, column=0, stick=W+E)
def UpdateStd():
    sqlstr = " update student set " # (Std_Id, Std_Name, sex, dep_id, Birth_Place, Birthday, Religion)values("
    sqlstr += "std_name = " + db.Qo(estd_name.get()) + ","
    sqlstr += "sex = " + db.Qo(varSex.get()) + ","
    sqlstr += "dep_id = " +db.Qo(str(depvar).split(':')[0]) + ","
    sqlstr += "birth_place=" +db.Qo(ebirth_place.get()) + ","
    sqlstr += "birthday = " +db.Qo(ebirthday.get()) + ","
    sqlstr += "religion = " +db.Qo(ereligion.get()) 
    sqlstr += " where std_id = " +db.Qo(estd_id.get())
    db.execSQLcommand(sqlstr)
    getAllStudent()
opUpdate = Button(opFrame)
opUpdate.config(text="修改", bg="gray", fg="blue", width=10, height=2, font="標楷體14", command=UpdateStd)
opUpdate.grid(row=0, column=1, stick=W+E)
#
def DeleteStd():
    sqlstr = "delete from student where std_id = " +db.Qo(estd_id.get())
    db.execSQLcommand(sqlstr)
    getAllStudent()

opDelete = Button(opFrame)
opDelete.config(text="刪除", bg="gray", fg="blue", width=10, height=2, font="標楷體14", command=DeleteStd)
opDelete.grid(row=0, column=2, stick=W+E)

getAllStudent()

win1.mainloop() 