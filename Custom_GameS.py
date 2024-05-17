import socket as sk
import pygame as p
import dataParser as pr  
from random import randint
import math as m 
def initialize():
    global sock,game,con,cC,cliSockA,cliSockB, sh,sw, x,y,angle,mt
    sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    sock.bind(('',12002))
    sh=600
    sw=500 
    mt=0.08
    angle = 200
    x = 300
    y = 250
    sock.listen(2)
    game=True
    con=[]
    cC=(300,250)
    pr.c("Line 20")
    cliCon=False
    while not cliCon:
        try:
            cliSockA, cliIPA = sock.accept()
            cliSockA.send("valid".encode())
            if cliSockA.recv(1024).decode() == 'valid':
                cliCon=True
        except:
            pr.c("Nonclient connected, removing.")
            cliSockA=''        
    print("Player 1 connected!")
    cliCon=False
    while not cliCon:
        try:
            cliSockB, cliIPA = sock.accept()
            cliSockB.send("valid".encode())
            if cliSockB.recv(1024).decode() == 'valid':
                cliCon=True
        except:
            pr.c("Nonclient connected, removing.")
            cliSockB=''
    print("Player 2 connected! Game begins.")
    cliSockA.send('000'.encode())
    cliSockA.send('A'.encode())
    cliSockB.send('000'.encode())
    cliSockB.send('B'.encode())
initialize()
pr.c("Initialized and ready.")
while game:
    cA = pr.parseInSingle(cliSockA.recv(1024))
    conditA=(cC[0]+20>=cA[0]-20 and cC[0]+20<=cA[0]+20 and cC[1]+20>=cA[1]-60 and cC[1]+20<=cA[1]+60 and cC[1]-20>=cA[1]-60 and cC[1]-20<=cA[1]+60)
    cB = pr.parseInSingle(cliSockB.recv(1024))
    conditB=(cC[0]-20>=cB[0]-20 and cC[0]-20<=cB[0]+20 and cC[1]+20>=cB[1]-60 and cC[1]+20<=cB[1]+60 and cC[1]-20>=cB[1]-60 and cC[1]-20<=cB[1]+60)
    x  = 0
    y  = 0
    pr.c(int((mt*m.degrees(m.cos(m.radians(angle))))/10)+1)
    
    cC=(x,y)
    outCoordsA=cC,cB
    outCoordsB=cC,cA
    cliSockA.send(pr.parseOutDouble(outCoordsA))
    cliSockB.send(pr.parseOutDouble(outCoordsB))
