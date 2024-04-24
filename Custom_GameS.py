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
    cliSockA, cliIPA = sock.accept()
    print("Player 1 connected!")
    cliSockB, cliIPB = sock.accept()
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
    x  = x+int((mt*m.degrees(m.cos(m.radians(angle/15)))))
    y  = y+int((mt*m.degrees(m.sin(m.radians(angle/15)))))
    pr.c(int((mt*m.degrees(m.cos(m.radians(angle))))/10)+1)
    if x<=20 or x >580 or y<=20 or y>480 or conditA or conditB:
        mt=-mt
        angle = randint(1,360)
        if x<=20:
            x=21
        if x>=580:
            x=579
        if y<=20:
            y=21
        if y>=480:
            y=479
    if angle>360:
        angle -=360
    elif angle<0:
        angle +=360
    cC=(x,y)
    outCoordsA=cC,cB
    outCoordsB=cC,cA
    cliSockA.send(pr.parseOutDouble(outCoordsA))
    cliSockB.send(pr.parseOutDouble(outCoordsB))
