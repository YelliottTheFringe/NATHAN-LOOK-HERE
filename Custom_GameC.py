import socket as sk
from time import sleep
import pygame as p
import dataParser as pr

def waitfor(signal):
    brk=True
    while brk:
        if sock.recv(1024).decode() == signal:
            print("the game begins")
            break
        else:
            sleep(0.001)

    pass
p.init()
sh=600
sw=500
window=p.display.set_mode((sh,sw))
p.display.set_caption("Pong")
sock=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
sock.connect(('192.168.9.247',12002))
waitfor('000')
clientNum=sock.recv(1024).decode()
if clientNum=='A':
    c=60
elif clientNum=='B':
    c=sh-70
v=100
game=True
while game:
    coord=(c,v)
    sock.send(pr.parseOutSingle(coord))
    window.fill('Black')
    A,B=pr.parseInDouble(sock.recv(1024))
    p.draw.rect(window,'Red',(B[0],B[1],20,60)) #oponent
    p.draw.circle(window,"White",A,15)
    p.draw.rect(window,'White',(coord[0],coord[1],20,60)) # self
    keys = p.key.get_pressed()
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
    if keys[p.K_w] and v>3:
        v-=1
    elif keys[p.K_s]and v<(sw-60):
        v+=1
    if v<=3:
        v+=1
    elif v>(sw-30):
        v-=1
    p.display.update()
    pr.c(coord)
    
