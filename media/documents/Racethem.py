import pygame
import time
import random

pygame.init()

display_width=700
display_hieght=600
bg=pygame.image.load("back.png")
obj=pygame.image.load("brick.png")

col=(241,223,15)
black=(0,0,0)
white=(255,255,255)
red=(200,0,0)
light_red=(255,0,0)
green=(0,200,0)
light_green=(0,255,0)
car_width=73
car_hieght=170

disp=pygame.display.set_mode((display_width,display_hieght))
pygame.display.set_caption("Race!!")
clock=pygame.time.Clock()

cimg=pygame.image.load("car.png")
def things_dodged(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("Dodged:"+str(count),True,black)
    disp.blit(text,(0,0))

def button(msg,x,y,h,w,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+h>mouse[0]>x and y+w>mouse[1]>y:
        pygame.draw.rect(disp,ic,(x,y,h,w))
        if click[0]==1 and action!=None:
            if action=="start":
                game_loop()
            elif action=="quit":
                pygame.quit()
                quit()
                
    else:
        pygame.draw.rect(disp,ac,(x,y,h,w))
    smallText=pygame.font.Font("freesansbold.ttf",20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center=((x+(h/2)),(y+(w/2)))
    disp.blit(TextSurf,TextRect)
        
def car(x,y):
    disp.blit(cimg,(x,y))
    
def things(thingx,thingy,thingw,thingh,color):
    disp.blit(obj,[thingx,thingy,thingw,thingh])

def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largeText=pygame.font.Font("freesansbold.ttf",40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center=((display_width/2),(display_hieght/2))
    disp.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(3)
    game_loop() 

def crash():
    message_display("Buddy You Crashed!!")

def start_menu():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        disp.blit(bg,(0,0))
        largeText=pygame.font.Font("freesansbold.ttf",40)
        TextSurf, TextRect = text_objects("Lets Race Them", largeText)
        TextRect.center=((display_width/2),(display_hieght/2))
        disp.blit(TextSurf,TextRect)

        button("Start !!",150,450,100,50,light_green,green,"start")
        button("Quit",500,450,100,50,light_red,red,"quit")

        mouse=pygame.mouse.get_pos()
        if 150+100>mouse[0]>150 and 450+50>mouse[1]>450:
            pygame.draw.rect(disp,light_green,(150,450,100,50))
        else:
            pygame.draw.rect(disp,green,(150,450,100,50))

        if 500+100>mouse[0]>500 and 450+50>mouse[1]>450:
            pygame.draw.rect(disp,light_red,(500,450,100,50))
        else:
            pygame.draw.rect(disp,red,(500,450,100,50))

        smallText=pygame.font.Font("freesansbold.ttf",20)
        TextSurf, TextRect = text_objects("Start!!", smallText)
        TextRect.center=((150+(100/2)),(450+(50/2)))
        disp.blit(TextSurf,TextRect)

        smallText=pygame.font.Font("freesansbold.ttf",20)
        TextSurf, TextRect = text_objects("Exit", smallText)
        TextRect.center=((500+(100/2)),(450+(50/2)))
        disp.blit(TextSurf,TextRect)

        pygame.display.update()
        clock.tick(15)

    
def game_loop():
    x=(display_width * 0.33)
    y=(display_hieght * 0.8)

    x_change=0
    y_change=0
    thing_startx=random.randrange(0,display_width)
    thing_starty=-600
    thing_speed=4
    thing_width=100
    thing_hieght=100
    dodged=0


    gameExit=False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key ==pygame.K_UP:
                    y_change = -5
                if event.key ==pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0


                

        x+=x_change
        y+=y_change

                
        disp.blit(bg,(0,0))
        things(thing_startx,thing_starty,thing_width,thing_hieght,col)
        thing_starty +=thing_speed

        
        car(x,y)
        things_dodged(dodged)
        
        if x>display_width-car_width or x<0:
            crash()

        if thing_starty>display_hieght:
            
            thing_starty=0-thing_hieght
            thing_startx=random.randrange(0,display_width)
            dodged+=1
                
            if dodged%3==0:
                thing_speed+=0.5

            if dodged%6==0:
                thing_width+=0.9

        if y<thing_starty+thing_hieght:
            if x>thing_startx and x<thing_startx+thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width:
                crash()

        if y<0:
            crash()
            
        pygame.display.update()
        clock.tick(70)
start_menu()
game_loop()
pygame.quit()
quit()
