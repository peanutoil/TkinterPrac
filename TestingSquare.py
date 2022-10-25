import pygame
import math
from pygame.locals import *
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Testing")
move = 0
black = (0,0,0)
WIDTH = 500
HEIGHT = 500

class Player():

    def __init__(self,color):
        self.x=WIDTH//2
        self.y=HEIGHT//2
        self.color = color
        self.right = 0
        self.left = 0
        self.up = 0
        self.down = 0
    def draw(self):
        pygame.draw.rect(window,self.color,(self.x,self.y,20,20))
        if self.right==1 and self.x<480:
            self.x=self.x+1
        if self.left==1 and self.x>0:
            self.x=self.x-1
        if self.up==1 and self.y>0:
            self.y=self.y-1
        if self.down == 1 and self.y<480:
            self.y = self.y+1
                
    def move(self,event):
        if event.type==KEYDOWN:
            if event.key==K_RIGHT or event.key==K_d:
                self.right=1
            if event.key==K_LEFT or event.key==K_a:
                self.left=1
            if event.key==K_UP or event.key==K_w:
                self.up=1
            if event.key==K_DOWN or event.key==K_s:
                self.down=1
               
        elif event.type==KEYUP:
            if event.key==K_RIGHT or event.key==K_d:
                self.right=0
            if event.key==K_LEFT or event.key==K_a:
                self.left=0
            if event.key==K_UP or event.key==K_w:
                self.up=0
            if event.key==K_DOWN or event.key==K_s:
                self.down=0

player1 = Player((0,255,255))

co = [100,100]
while True:
    window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        player1.move(event)
    player1.draw()
    pygame.draw.circle(window,black,co,7)
    print(co,player1.x,player1.y)
    testx = co[0]
    testy = co[1]
    if co[0]<player1.x:
        testx = player1.x
    elif co[0]>player1.x+20:
        testx = player1.x+20
    if co[1]<player1.y:
        testy = player1.y
    elif co[1]>player1.y+20:
        testy = player1.y+20
    distx = co[0]-testx
    disty = co[1]-testy
    dist = math.sqrt((distx*distx)+(disty*disty))
    if dist<=7:
        co=[-5,-5]
##    if((co[0]-7<player1.x<co[0]+7 or co[0]-7<player1.x+20<co[0]+7) and (co[1]-7<player1.y<co[1]+7 or co[1]-7<player1.y+20<co[1]+7)):
##        co = [-5,-5]
    pygame.display.update()







