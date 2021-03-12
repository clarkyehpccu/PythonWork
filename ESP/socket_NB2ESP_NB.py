# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:42:49 2020

@author: clark
"""
import time
import socket
from tkinter import *
win = Tk()
win.geometry('500x300')
win.config(bg='lightblue')


def sendmessage():
    mysocket = socket.socket()
    mysocket.connect(('192.168.4.1',8268))  # ('192.168.4.1',8268)
    #-----
    msgx= sendmsg.get()
    mysocket.send(msgx.encode('utf-8'))  #送出訊息到AP
    # message from AP
    recvmsg.delete(1, END)
    recvmsg.insert(1, mysocket.recv(128).decode('utf-8') ) #接收AP來的訊息, 沒收到會停在此
    mysocket.close();
    
def closesocket():
    mysocket = socket.socket()
    mysocket.connect(('192.168.4.1',8268))  # ('192.168.4.1',8268)
    #-----
    msgx= 'exit'
    mysocket.send(msgx.encode('utf-8'))  #送出訊息到AP
    #message from AP
    recvmsg.delete(1, END)
    recvmsg.insert(1, mysocket.recv(128).decode('utf-8') ) #接收AP來的訊息, 沒收到會停在此
       
    mysocket.close();

sendbtn = Button(win, text='send message', command=sendmessage)
sendbtn.grid(row=0, column=0)
closebtn = Button(win, text='close AP socket', command=closesocket)
closebtn.grid(row=0, column=1, sticky=E+W)

lbl1 = Label(win, text='Message:')
lbl1.grid(row=1, column=0, sticky=E+W)
sendmsg = Entry(win)
sendmsg.grid(row=1, column=1, sticky=E+W)
sendmsg.insert(1, 'Hello World')  #預設

lbl2 = Label(win, text='Msg From AP:')
lbl2.grid(row=2, column=0, sticky=E+W)
recvmsg = Entry(win)
recvmsg.grid(row=2, column=1, sticky=E+W)

win.mainloop()
