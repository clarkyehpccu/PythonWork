# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
from tkinter import *
win = Tk()
win.geometry("1000x500")
win.config(bg='lightgreen')



#-----------------------------------------------------
cardList=[]
def isExist(card):
    flag_exist = 0
    for idx in range(len(cardList)):
        if card == cardList[idx]:
            flag_exist = 1
            break
    return flag_exist

def shuffle():
    #delete all list contnet
    for idx in range(len(cardList)):
        del cardList[0]
    #-------
    card_count = 0  #合法的牌數
    result.delete(0.0, END)
    result.insert(0.0,'<---Begin--->\n')
    while card_count < 52:
        cdclass = random.choice(('D', 'H', 'C', 'S'))
        cdnum = "{0:02d}".format(random.randint(1,13))
        card=cdclass + cdnum
        if not isExist(card):
            cardList.append(card)
            card_count += 1
    for idx, content in enumerate(cardList, 0):
        result.insert(END, "{0:02d}:{1:2s}\n".format(idx, content))
    result.insert(END,'<---ENd--->\n')

displayShuffle = Button(win, text='(1)顯示洗牌結果', command=shuffle)
displayShuffle.grid(row=0, column=0, sticky=W)

result = Text(win, width=20, height=20)
result.grid(row=1, column=0,  columnspan=3, sticky=E+W)
scroll1 = Scrollbar(win, command=result.yview)
scroll1.grid(row=1, column=3, sticky=N+S)

#-------------------------------------------------------
timex = 0
QueueCount = 0
QueueList = []
dif = 35
def showQueue():
    global timex, QueueCount
    timex += 1
    if timex % 2 == 0:
        QueueCount += 1
        
    if timex % 5 == 0:
        QueueCount -= 1
    
    #Destroy all btn
    for obj in QueueList: #remove all standman image
           obj.destroy()
    if QueueCount > 0:
        pos_x = 0    
        for idx in range(QueueCount):
            btn = Button(win, text='排:'+str(idx+1))
            btn.place(x=pos_x, y=300)
            QueueList.append(btn)
            pos_x += dif
    if timex == 60:
        return
    win.after(100,showQueue)
displayQueue = Button(win, text='(2)顯示2入5出排隊結果', command=showQueue)
displayQueue.grid(row=0, column=1, sticky=W)
#-----------------------------------------------------
def readFile():
    result.delete(0.0,END)
    fileObj = open("record.txt", "r")
    recordList=[]
    if fileObj != None:
       linestr = fileObj.readlines()
       for oneline in linestr:
           recordList = oneline.split(',')
           std_id = recordList[0] #學號
           course = recordList[1] #科目
           rcd = recordList[2]    #成績
           if course == "MATH":
               if int(rcd) < 90:
                  rcd = int(rcd) + 10
           result.insert(END, '學號:{0}, 科目:{1:5s}, 成績:{2:3d}\n'.format(std_id, course, int(rcd)))
    fileObj.close()

readFile = Button(win, text='(3讀取成績檔)', command=readFile)
readFile.grid(row=0, column=2, sticky=W)

win.mainloop()