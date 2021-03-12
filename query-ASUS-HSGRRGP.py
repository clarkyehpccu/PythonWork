# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:01:45 2019

@author: clark
"""
import sys
from tkinter import *
import myDB
db = myDB.DBclass("student.db")
def winQuery():
    global depset
    global courseset
    global flag_dep_value
    global flag_course_value
    global flag_std_value
    def getAllData():
        global flag_dep_value
        global flag_course_value
        global flag_std_value
        sqlstr = " select d.dep_name, r.std_id, s.std_name, r.course_id, c.course_name, r.rcd "
        sqlstr += "  from record r, course c, student s, department d"
        sqlstr += "  where r.std_id = s.std_id "
        sqlstr += "    and r.course_id = c.course_id " 
        sqlstr += "    and s.dep_id = d.dep_id "
        if flag_dep_value.get() == True:
           sqlstr += " and d.dep_id =" + depvar.get()[1:-1].split(',')[0]
        if flag_course_value.get() == True:
            sqlstr += " and r.course_id = " + coursevar.get()[1:-1].split(',')[0]
        if flag_std_value.get() == True:
            sqlstr += " and s.std_name like '%" + estd_name.get() + "%'"
        print(sqlstr)
        myset = db.getSQLresult(sqlstr)
        
        datalist.delete(0,END)
        for idx, item in enumerate(myset, 0):
            itemstr = "{0:10s} {1:10s}  {2:7s}  {3:10s}  {4:10s}  {5:3d}".format(item[0],item[1],item[2],item[3],item[4],item[5])
            datalist.insert(END, itemstr)
        
    def preparedepList():
        global depset
        global depvar
        
        sqlstr =  'select dep_id, Dep_Name'
        sqlstr += ' from department '
        depset = db.getSQLresult(sqlstr)  #temp is list as [(dep_id, dep_name), (tuple),...,(tuple)]    
        print(sqlstr, depset)
    def preparestdList(stdset):
        dep_id = depvar.get()[1:-1].split(',')[0]
        sqlstr =  'select std_id , std_name '
        sqlstr += ' from student '
        sqlstr += ' where dep_id= ' + dep_id
        temp = db.getSQLresult(sqlstr)
        for item in temp:
            stdset.append(item)
    
    def exitWin():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
           #query.quit()
           winr.destroy()
           
            
    def preparecourseList():
        global courseset
        sqlstr =  'select course_id , course_name '
        sqlstr += ' from course '
        courseset = db.getSQLresult(sqlstr)
        #for item in temp:
        #    courseset.append(item)
            
    def getSexValue():
        print("sex:",  varSex.get() )
    '''
    def redirect_to_file(text):
        original = sys.stdout
        sys.stdout = open('/path/to/redirect.txt', 'w')
        print('This is your redirected text:')
        print(text)
        sys.stdout = original
     
        print('This string goes to stdout, NOT the file!')
    '''
       
    winr = Tk()
    winr.geometry("600x520")
    winr.title('查詢畫面')
    winr.config(background="lightyellow")
    #-------
    
    
    #學系-----------------------------
    flag_dep_value = BooleanVar(winr) 
    flag_dep_value.set(True)
    flag_dep = Checkbutton(winr, text="學系", var=flag_dep_value)
    flag_dep.grid(row=0, column=0)
    '''
    def getdepListClick(evt):
        dep_id = depvar.get()[1:-1].split(',')[0]
        global stdset
        sqlstr =  'select std_id , std_name '
        sqlstr += ' from student '
        #sqlstr += ' where dep_id = ' + dep_id    
        stdset = db.getSQLresult(sqlstr)
        stdvar.set(stdset[0])
    '''   
    
    depset = list() #depset是list, 元素是 tuple
    preparedepList()
    depvar = StringVar(winr) #準備 反映點選項目
    depvar.set(depset[0]) #預設depList停駐的index
    depList  = OptionMenu(winr, depvar, *depset)
    depList.grid(row=0, column=1, stick=W+E)
    #科目-----------------------------
    flag_course_value = BooleanVar(winr) 
    flag_course_value.set(True)
    flag_course = Checkbutton(winr, text="科目", var=flag_course_value)
    flag_course.grid(row=1, column=0)
    
    
    courseset = list()
    preparecourseList()
    coursevar = StringVar(winr) #準備 反映點選項目
    coursevar.set(courseset[0]) #預設depList停駐的index
    courseList  = OptionMenu(winr, coursevar, *courseset)
    courseList.grid(row=1, column=1, stick=W+E)
    
    #姓名-----------------------------
    flag_std_value = BooleanVar(winr) 
    flag_std_value.set(False)
    flag_std = Checkbutton(winr, text="姓名", var=flag_std_value)
    flag_std.grid(row=2, column=0)
    
    estd_name = Entry(winr)
    estd_name.grid(row=2, column=1, stick=W+E)
    
    #查詢
    query = Button(winr)
    query.config(text="查詢", bg="gray", fg="white", width=10, height=2, font="標楷體14", command=getAllData)
    query.grid(row=2, column=2, stick=W)
    
    #Exit
    exit = Button(winr)
    exit.config(text="離開", bg="red", fg="white", width=10, height=2, font="標楷體14", command=exitWin)
    exit.grid(row=2, column=3, stick=W)
    #--------
    datalist = Listbox(winr)
    
    datalist.config(width=80, height=15)
    datalist.grid(row=3, column=0, columnspan=4)
    
    #------
    myScrollbar = Scrollbar(winr)
    myScrollbar.grid(row=3, column=4, stick=N+S)
    myScrollbar.config(command=datalist.yview)
    #====================================================
    
    #winr.protocol("WM_DELETE_WINDOW", exitWin)
    
    #winr.protocol("WM_DELETE_WINDOW", on_closing)
    
    winr.mainloop() 
    