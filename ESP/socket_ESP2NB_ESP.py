# -*- coding: utf-8 -*-
"""
sucket client
Created on Mon Sep 21 14:28:35 2020

@author: clark
"""
import socket
import time

#-----
while True:
    mysocket = socket.socket()
    mysocket.connect(('192.168.4.2',8268))  # ('192.168.1.4',8266)
    msg = input('Please input a message(Exit to quit):')
    if msg.upper() == 'EXIT':
        break
    
    mysocket.send(msg.encode('utf-8'))
    print("get:" +  mysocket.recv(128).decode('utf-8') )
    

mysocket.close();
print('Close Socket')
print('-----END------')