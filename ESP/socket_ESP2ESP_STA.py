# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:10:27 2020

@author: clark
"""

#COM4    STA
import network
import time
import socket

myap=network.WLAN(network.AP_IF)
myap.active(0)  #關閉192.168.4.1
myap.ifconfig()
mysta=network.WLAN(network.STA_IF)
mysta.active(True)
mysta.connect('MicroPython-e47c74', 'micropythoN')# micropythoN
mysta.ifconfig()

#-----
while True:
    mysocket = socket.socket()
    mysocket.connect(('192.168.4.1',8268))  # ('192.168.1.4',8266)
    msg = input('Please input a message(Exit to quit):')
    if msg.upper() == 'EXIT':
        break 
    mysocket.send(msg.encode('utf-8'))
    print("get:" +  mysocket.recv(128).decode('utf-8') )
mysocket.close();
print('Close Socket')
print('-----END------')

