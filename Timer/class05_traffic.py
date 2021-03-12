# -*- coding: utf-8 -*-
"""
某交通路口交通工具到達狀況:
卡車:5秒鐘到達1台,  10秒離開1台
汽車:3秒鐘到達1台,   5秒離開1台
摩托車:1秒鐘到達1台, 2秒離開1台 
試用計時器, 顯示每秒交通路口的工具數量, 直到60秒為止
"""
from tkinter import *
win=Tk()
win.geometry('1000x500')
win.config(bg='white')
sec = 0
trank = 0
car = 0
motor = 0
def tick():
    global trank, car, motor, sec, final
    sec +=1
    #drive in
    if sec %5 == 0:
        trank += 1
    if sec % 3 == 0:
        car += 1
    motor += 1
    #drive out
    if (sec %10==0) and (trank > 0):
        trank -= 1
    if (sec %5 == 0)  and (car > 0):
        car -= 1
    if (sec % 2 == 0)  and (motor > 0):
        motor -= 1
    print('trank:{0}, car:{1}, motor:{2}'.format(trank, car, motor))
    #====erase all vehicle======
    for idx in range(len(tranklist)):
        tranklist[idx].destroy()
    for idx in range(len(carlist)):
        carlist[idx].destroy()
    for idx in range(len(motorlist)):
        motorlist[idx].destroy()
    #===print vehicle
    x_pos_motor = 10; y_pos_motor = 100
    for idx in range(motor):
        motorbtn = Button(win, image=imgmotor)
        motorbtn.place(x=x_pos_motor,y=y_pos_motor)
        motorlist.append(motorbtn)
        x_pos_motor += 120
    x_pos_car = 10; y_pos_car = 200
    for idx in range(car):
        carbtn = Button(win, image=imgcar)
        carbtn.place(x=x_pos_car,y=y_pos_car)
        carlist.append(carbtn)
        x_pos_car += 150
    x_pos_trank = 10; y_pos_trank = 300
    for idx in range(trank):
        trankbtn = Button(win, image=imgtrank)
        trankbtn.place(x=x_pos_trank,y=y_pos_trank)
        tranklist.append(trankbtn)
        x_pos_trank += 200
    final -= 1; secLabel.config(text=str(final))
    if final == 0:
        sec = 0
        final=30
        motor = car = trank = 0
        return
    win.after(1000, tick)
carlist=[]
tranklist=[]
motorlist=[]
final = 30    
mybtn=Button(win,text='計時開始', command=tick)
mybtn.place(x=0, y=0) 
secLabel=Label(win,text='秒數', bg='red', fg='white')
secLabel.place(x=100, y=0) 
imgmotor = PhotoImage(file=r"D:\2020Python\我的範例\交通工具\motor.PNG")
imgtrank = PhotoImage(file=r"D:\2020Python\我的範例\交通工具\trank.PNG")
imgcar =PhotoImage(file=r"D:\2020Python\我的範例\交通工具\car.PNG")
win.mainloop()