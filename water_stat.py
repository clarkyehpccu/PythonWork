# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:30:09 2020

@author: clark
"""

from tkinter import * 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 


import sqlite3
from pandas import DataFrame
import matplotlib.pyplot as plt



import pandas as pd


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
win.title("統計圖表")

def genStat():
    listStationName=[]
    listPhValue=[]
    listTurbidity=[]
    listResidualChlorine=[]
    sqlstr = " select station_name, pH_Value, turbidity, residual_chlorine from water "
    listx = execSQLcommand(sqlstr).fetchall()
    for itempair in listx:
        listStationName.append(itempair[0])
        listPhValue.append(itempair[1])
        listTurbidity.append(itempair[2])
        listResidualChlorine.append(itempair[3])
        #print (itempair)
    #seriesX = pd.Series(list2, index=list1, name="Price")
    #seriesX.plot(kind="bar")
    plt.plot(listStationName, listPhValue, '--b', label='PH Value')
    plt.plot(listStationName, listTurbidity, '--r', label='Turbidity')
    plt.plot(listStationName, listResidualChlorine,'--g', label='Residual Chlorine')
    plt.grid(True)
    plt.legend()
    plt.show()
def genStatInTkinter():
    listStationName=[]
    listPhValue=[]
    listTurbidity=[]
    listResidualChlorine=[]
    sqlstr = " select station_name, pH_Value, turbidity, residual_chlorine from water "
    listx = execSQLcommand(sqlstr).fetchall()
    for itempair in listx:
         listStationName.append(itempair[0])
         listPhValue.append(itempair[1])
         listTurbidity.append(itempair[2])
         listResidualChlorine.append(itempair[3])
         #print (itempair)
    # the figure that will contain the plot 
    fig = Figure(figsize = (5, 5),  dpi = 100) 
    plot1 = fig.add_subplot(111) 
    
    # plotting the graph 
    plot1.plot(listPhValue, 'b')  
    plot1.plot(listTurbidity,'r')
    plot1.plot(listResidualChlorine,'g')
  
    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, master = win)   
    canvas.draw() 
    canvas.get_tk_widget().grid(row=2, column=0)
    
  
    # placing the canvas on the Tkinter window 
    
  
    # creating the Matplotlib toolbar 
    #toolbar = NavigationToolbar2Tk(canvas, win) 
    #toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    #canvas.get_tk_widget().grid(row=1, column=0)
# =============================================================================
#     listStationName=[]
#     listPhValue=[]
#     listTurbidity=[]
#     listResidualChlorine=[]
#     sqlstr = " select station_name, pH_Value, turbidity, residual_chlorine from water "
#     listx = execSQLcommand(sqlstr).fetchall()
#     for itempair in listx:
#         listStationName.append(itempair[0])
#         listPhValue.append(itempair[1])
#         listTurbidity.append(itempair[2])
#         listResidualChlorine.append(itempair[3])
#         #print (itempair)
#     #seriesX = pd.Series(list2, index=list1, name="Price")
#     #seriesX.plot(kind="bar")
#     plt.plot(listStationName, listPhValue, '--b', label='PH Value')
#     plt.plot(listStationName, listTurbidity, '--r', label='Turbidity')
#     plt.plot(listStationName, listResidualChlorine,'--g', label='Residual Chlorine')
#     plt.grid(True)
#     plt.legend()
#     plt.show()
#     
#     figure2 = plt.Figure(figsize=(5,3), dpi=100) # figsize(width,height)
#     ax2 = figure2.add_subplot(111)
#     line2 = FigureCanvasTkAgg(figure2, win)
#     line2.get_tk_widget().grid(row=2, column=0)
#     #df2 = listStationName
#     df2 = DataFrame(listPhValue,columns=listStationName)
#     df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
#     ax2.set_title('Year Vs. Unemployment Rate')
# =============================================================================

btnStat = Button(win, text='產生圖表', width=30, command=genStat)
btnStat.grid(row=0, column=0)

btnStatByTkinter = Button(win, text='在tkinter產生圖表', width=30, command=genStatInTkinter)
btnStatByTkinter.grid(row=1, column=0)



win.mainloop()