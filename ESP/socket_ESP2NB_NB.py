# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:42:49 2020

@author: clark
"""
import time
import socket
from tkinter import *
win = Tk()
win.geometry('600x400')
win.config(bg='lightblue')
op = 'Y'
colorx = 'R'
mysocket = socket.socket()
mysocket.bind(('192.168.4.2',8268)) # IP, Port
mysocket.listen(4)

             
def listern():
    global mysocket, count, colorx
    if op == 'Y':
       print('Enter While')
       message.insert(1.0, 'Waiting....\n')
       light.config(bg='blue', fg='white', text='待機')
       #message.insert(1.0, 'Waiting....\n')
       client, addr = mysocket.accept() #程式會停在accept(); addr會取得STA端的IP&port
       client_msg= client.recv(128).decode('utf-8')
       #message.delete(1.0,END)
       message.insert(1.0,'接到的訊息:Client IP:{0}     Port:{1}\n'.format(addr[0], addr[1]))
       message.insert(1.0,'--------------\n')
       message.insert(1.0,'接到的訊息:{0}\n'.format(client_msg))
       message.insert(1.0,'--------------\n')
       #==========
       if colorx == 'R':
          light.config(bg='red', fg='white', text='進行')
          colorx = 'G'
       else:
          light.config(bg='green', fg='white', text='進行')
          colorx = 'R'       
       #==========
       client.send(b"--Job Finished--")
       win.after(1000,listern)
    
def closesocket():
    global mysocket, op
    #message.delete(1, END)
    op = 'Y'
    message.insert(1, 'Socket已關閉') #接收AP來的訊息, 沒收到會停在此     
    mysocket.close();

sendbtn = Button(win, text='start socket Listern', command=listern)
sendbtn.grid(row=0, column=0)
closebtn = Button(win, text='close AP socket', command=closesocket)
closebtn.grid(row=0, column=1, sticky=E+W)



labelx = Label(win, text='Message:')
labelx.grid(row=1, column=0, sticky=E+W+N)
message = Text(win, height=20, width=60)
message.grid(row=1, column=1, sticky=E+W)

light = Button(win,text='信號燈', bg='blue', fg='yellow')
light.grid(row=4, column=0, columnspan=2, sticky=W+E)

win.mainloop()
