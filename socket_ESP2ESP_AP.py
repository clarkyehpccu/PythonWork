# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:10:27 2020

@author: clark
"""
#COM3    AP
import network
import time
import socket
from machine import Pin 
myap=network.WLAN(network.AP_IF)
myap.active(True)
myap.config(essid='MicroPython-e47c74', password='micropythoN')
myap.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1', '208.67.222.222')) 
p2 = Pin(2, Pin.OUT) #LED
ap=network.WLAN(network.AP_IF)
ap.active(True)
#新設一個socket
mysocket = socket.socket()
mysocket.bind(('192.168.4.1', 8268)) # 8266已被使用, 8268 is int, 
mysocket.listen(4) # wait for connected
while True:
      p2.value(0)   #預設亮
      print('等待. . . ')    
      client, addr = mysocket.accept() #程式會停在accept(); addr會取得STA端的IP&port
      client_msg= client.recv(128).decode('utf-8')
      print('STA IP:{0}     Port:{1}'.format(addr[0], addr[1]))
      print('接到的訊息:', client_msg)
      client.send(b"--" + client_msg + " Finished--")
      if(client_msg=='exit'):
          print('關機中.....')
          client.send(b'exit')  #送訊息回去給STA端
          break
      # --------閃燈-------
      for i in range(1,5):
            p2.value(1)   #暗
            time.sleep(0.5)
            p2.value(0) #亮
            time.sleep(0.5) # End of while
client.send(b"--Job Finished--")
print('<--工作完成')

