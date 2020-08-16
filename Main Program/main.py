import pygame, sys
import time
import serial
from pygame.locals import *

#-----------Path Plotter--------------------------------------------
def plot_left(x1,x2,y):
    i=x1
    while True:
        pygame.draw.circle(pywindow, BLUE, (i,y), 5, 0)
        i=i-1
        if i==x2:
            break
        
def plot_right(x1,x2,y):
    i=x1
    while True:
        pygame.draw.circle(pywindow, BLUE, (i,y), 5, 0)
        i=i+1
        if i==x2:
            break
        
def plot_up(x,y1,y2):
    i=y1
    while True:
        pygame.draw.circle(pywindow, BLUE, (x,i), 5, 0)
        i=i-1
        if i==y2:
            break
        
def plot_down(x,y1,y2):
    i=y1
    while True:
        pygame.draw.circle(pywindow, BLUE, (x,i), 5, 0)
        i=i+1
        if i==y2:
            break
#STATIC POINTS--------------------------------------------------------
def DEST_Point_1():
    pygame.draw.circle(pywindow, BLUE, (920,93), 10, 0) #1
def DEST_Point_2():
    pygame.draw.circle(pywindow, BLUE, (920,382), 10, 0) #2
def DEST_Point_3():
    pygame.draw.circle(pywindow, BLUE, (337,224), 10, 0) #3
def DEST_Point_4():
    pygame.draw.circle(pywindow, BLUE, (338,465), 10, 0) #4
def START_Point():
    pygame.draw.circle(pywindow, RED, (703,546), 10, 0) #Start
#RESET_WINDOW---------------------------------------------------------
def RESET_WINDOW():
    pywindow.blit(background_map,(0,0))
    DEST_Point_1()
    DEST_Point_2()
    DEST_Point_3()
    DEST_Point_4()
    START_Point()
#Plot Path------------------------------------------------------------
def Path_1():
    RESET_WINDOW()
    plot_up(703,548,225)
    plot_right(703,920,225)
    plot_up(920,225,93)
    START_Point()
def Path_2():
    RESET_WINDOW()
    plot_up(703,548,408)
    plot_right(703,920,408)
    plot_up(920,408,382)
    START_Point()
def Path_3():
    RESET_WINDOW()
    plot_up(703,548,225)
    plot_left(703,338,225)
    START_Point()
def Path_4():
    RESET_WINDOW()
    plot_up(703,548,466)
    plot_left(703,340,466)
    START_Point()

#DRIVE LOGIC---------------------------------------------------------------
def REFRESH_DRIVE():
    pywindow.blit(background_map,(0,0))
    DEST_Point_1()
    DEST_Point_2()
    DEST_Point_3()
    DEST_Point_4()

def render_up_dest1(x,y1,y2):
    #image backgroung
    pywindow.blit(background_map,(0,0))
    #updated path
    i=y1
    var = '1'
    while True:
        pygame.draw.circle(pywindow, BLUE, (x,i), 5, 0)
        i=i-1
        if i==y2:
            break
    plot_right(703,920,225)
    plot_up(920,225,93)
    DEST_Point_1()
    DEST_Point_2()
    DEST_Point_3()
    DEST_Point_4()
    pygame.draw.circle(pywindow, RED, (x,y1), 10, 0)
    pygame.display.update()
    fps.tick(fps_clock)

def render_up2_dest1(x,y1,y2):
    #image backgroung
    pywindow.blit(background_map,(0,0))
    #updated path
    i=y1
    while True:
        pygame.draw.circle(pywindow, BLUE, (x,i), 5, 0)
        i=i-1
        if i==y2:
            
            break
    DEST_Point_1()
    DEST_Point_2()
    DEST_Point_3()
    DEST_Point_4()
    pygame.draw.circle(pywindow, RED, (x,y1), 10, 0)
    pygame.display.update()
    fps.tick(fps_clock)

def render_right_dest1(x1,x2,y):
    #image backgroung
    pywindow.blit(background_map,(0,0))
    #updated path
    i=x1
    while True:
        pygame.draw.circle(pywindow, BLUE, (i,y), 5, 0)
        i=i+1
        if i==x2:
            break
    DEST_Point_1()
    DEST_Point_2()
    DEST_Point_3()
    DEST_Point_4()
    plot_up(920,225,93)
    pygame.draw.circle(pywindow, RED, (x1,y), 10, 0)
    pygame.display.update()
    fps.tick(fps_clock)
#Drive Path-------------------------------------------
def drive_dest_1():
    #Drive up----------
    x  = 703
    y1 = 548
    y2 = 225
    difference=y1-y2
    var='0'
    while difference>0:
        render_up_dest1(x,y1,y2)
        y1=y1-1
        if(difference==alert_time):
            ser.write(var.encode())
        if(y1==y2):
            break
        difference=difference-1
    
    ser.write(var.encode())
    #Drive right----------
    x1  = 703
    x2 = 920
    y = 225
    difference=x2-x1
    var='1'
    while difference>0:
        render_right_dest1(x1,x2,y)
        x1=x1+1
        if(difference==alert_time):
            ser.write(var.encode())
        if(x1==x2):
            break
        difference=difference-1
    ser.write(var.encode())    
    #Drive up 2----------
    x  = 920
    y1 = 225
    y2 = 93
    difference=y1-y2
    while difference>0:
        render_up2_dest1(x,y1,y2)
        y1=y1-1
        if(y1==y2):
            break
        difference=difference-1
    var='0'
    ser.write(var.encode())
    var='1'    
    ser.write(var.encode())
#--------------------------------------------------------------------------

def render_up_dest2(x,y1,y2):
    #image backgroung
    pywindow.blit(background_map,(0,0))
    #updated path
    i=y1
    while True:
        pygame.draw.circle(pywindow, BLUE, (x,i), 5, 0)
        i=i-1
        if i==y2:
            break
    DEST_Point_1()
    DEST_Point_2()
    DEST_Point_3()
    DEST_Point_4()
    plot_right(703,920,408)
    plot_up(920,408,382)
    pygame.draw.circle(pywindow, RED, (x,y1), 10, 0)
    pygame.display.update()
    fps.tick(fps_clock)

def render_up2_dest2(x,y1,y2):
    #image backgroung
    pywindow.blit(background_map,(0,0))
    #updated path
    i=y1
    while True:
        pygame.draw.circle(pywindow, BLUE, (x,i), 5, 0)
        i=i-1
        if i==y2:
            break
    DEST_Point_1()
    DEST_Point_2()
    DEST_Point_3()
    DEST_Point_4()
    pygame.draw.circle(pywindow, RED, (x,y1), 10, 0)
    pygame.display.update()
    fps.tick(fps_clock)

def render_right_dest2(x1,x2,y):
    #image backgroung
    pywindow.blit(background_map,(0,0))
    #updated path
    i=x1
    while True:
        pygame.draw.circle(pywindow, BLUE, (i,y), 5, 0)
        i=i+1
        if i==x2:
            break
    DEST_Point_1()
    DEST_Point_2()
    DEST_Point_3()
    DEST_Point_4()
    plot_up(920,408,382)
    pygame.draw.circle(pywindow, RED, (x1,y), 10, 0)
    pygame.display.update()
    fps.tick(fps_clock)

def drive_dest_2():
    #Drive up----------------------
    x  = 703
    y1 = 548
    y2 = 408
    difference=y1-y2
    var='0'
    while difference>0:
        render_up_dest2(x,y1,y2)
        y1=y1-1
        if(difference==alert_time):
            ser.write(var.encode())
        if(y1==y2):
            break
        difference=difference-1
    ser.write(var.encode())
    #Drive right----------
    x1  = 703
    x2 = 920
    y = 408
    difference=x2-x1
    var='1'
    while difference>0:
        render_right_dest2(x1,x2,y)
        x1=x1+1
        if(difference==alert_time):
            ser.write(var.encode())
        if(x1==x2):
            break
        difference=difference-1
    ser.write(var.encode())
    #Drive up2--------------------------------------
    x  = 920
    y1 = 408
    y2 = 382
    difference=y1-y2
    while difference>0:
        render_up2_dest2(x,y1,y2)
        y1=y1-1
        if(y1==y2):
            break
        difference=difference-1
    var='0'
    ser.write(var.encode())
    var='1'    
    ser.write(var.encode())
#--------------------------------------------------------------------------------
def render_up_dest3(x,y1,y2):
    #image backgroung
    pywindow.blit(background_map,(0,0))
    #updated path
    i=y1
    while True:
        pygame.draw.circle(pywindow, BLUE, (x,i), 5, 0)
        i=i-1
        if i==y2:
            break
    DEST_Point_1()
    DEST_Point_2()
    DEST_Point_3()
    DEST_Point_4()
    plot_left(703,338,225)
    pygame.draw.circle(pywindow, RED, (x,y1), 10, 0)
    pygame.display.update()
    fps.tick(fps_clock)

def render_left_dest3(x1,x2,y):
    #image backgroung
    pywindow.blit(background_map,(0,0))
    #updated path
    i=x1
    while True:
        pygame.draw.circle(pywindow, BLUE, (i,y), 5, 0)
        i=i-1
        if i==x2:
            break
    DEST_Point_1()
    DEST_Point_2()
    DEST_Point_3()
    DEST_Point_4()
    pygame.draw.circle(pywindow, RED, (x1,y), 10, 0)
    pygame.display.update()
    fps.tick(fps_clock)

    
def drive_dest_3():
    #Drive up----------------------
    x  = 703
    y1 = 548
    y2 = 225
    difference=y1-y2
    var='1'
    while difference>0:
        render_up_dest3(x,y1,y2)
        y1=y1-1
        if(difference==alert_time):
            ser.write(var.encode())
        if(y1==y2):
            break
        difference=difference-1
    ser.write(var.encode())
    #Drive left----------------------
    x1  = 703
    x2 = 338
    y = 225
    difference=x1-x2
    while difference>0:
        render_left_dest3(x1,x2,y)
        x1=x1-1
        if(x1==x2):
            break
        difference=difference-1
    var='0'
    ser.write(var.encode())
    var='1'
    ser.write(var.encode())
#------------------------------------------------------------

def render_up_dest4(x,y1,y2):
    #image backgroung
    pywindow.blit(background_map,(0,0))
    #updated path
    i=y1
    while True:
        pygame.draw.circle(pywindow, BLUE, (x,i), 5, 0)
        i=i-1
        if i==y2:
            break
    DEST_Point_1()
    DEST_Point_2()
    DEST_Point_3()
    DEST_Point_4()
    plot_left(703,340,466)
    pygame.draw.circle(pywindow, RED, (x,y1), 10, 0)
    pygame.display.update()
    fps.tick(fps_clock)

def render_left_dest4(x1,x2,y):
    #image backgroung
    pywindow.blit(background_map,(0,0))
    #updated path
    i=x1
    while True:
        pygame.draw.circle(pywindow, BLUE, (i,y), 5, 0)
        i=i-1
        if i==x2:
            break
    DEST_Point_1()
    DEST_Point_2()
    DEST_Point_3()
    DEST_Point_4()
    pygame.draw.circle(pywindow, RED, (x1,y), 10, 0)
    pygame.display.update()
    fps.tick(fps_clock)

def drive_dest_4():
    #Drive up----------------------
    x  = 703
    y1 = 548
    y2 = 466
    difference=y1-y2
    var='1'
    while difference>0:
        render_up_dest4(x,y1,y2)
        y1=y1-1
        if(difference==alert_time):
            ser.write(var.encode())
        if(y1==y2):
            break
        difference=difference-1
    ser.write(var.encode())
    #Drive left----------------------
    x1  = 703
    x2 = 340
    y = 466
    difference=x1-x2
    while difference>0:
        render_left_dest4(x1,x2,y)
        x1=x1-1
        if(x1==x2):
            break
        difference=difference-1
    var='0'
    ser.write(var.encode())
    var='1'
    ser.write(var.encode())






ser = serial.Serial('COM5', 9600, timeout=0)
alert_time= 70


pygame.init()
fps = pygame.time.Clock()
fps_clock=20
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pywindow = pygame.display.set_mode((1100, 600))
pygame.display.set_caption('Cross Guage')
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255,0,0)
GREEN = (0,128,0)
background_map = pygame.image.load("map.png")
pywindow.fill(WHITE)

RESET_WINDOW()

flag=0
Destination=0

while True: #main game loop

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: #This checks for the mouse press event
            mouse = pygame.mouse.get_pos()
            #DESTINATION 1
            if 50+195 > mouse[0] > 50 and 40+70 > mouse[1] > 40:
                #pygame.draw.rect(pywindow, RED,(50,40,195,70)) #Troubleshoot
                Path_1()
                Destination=1
            #DESTINATION 2
            if 50+195 > mouse[0] > 50 and 125+70 > mouse[1] > 125:
                Path_2()
                Destination=2
            #DESTINATION 3
            if 50+195 > mouse[0] > 50 and 210+70 > mouse[1] > 210:
                Path_3()
                Destination=3
            #DESTINATION 4
            if 50+195 > mouse[0] > 50 and 295+70 > mouse[1] > 295:
                Path_4()
                Destination=4
            #Start
            if 50+195 > mouse[0] > 50 and 380+70 > mouse[1] > 380:
                RESET_WINDOW()
                if(Destination==1):
                    drive_dest_1()
                elif(Destination==2):
                    drive_dest_2()
                elif(Destination==3):
                    drive_dest_3()
                elif(Destination==4):
                    drive_dest_4()
                else:
                    pygame.draw.rect(pywindow, RED,(50,380,195,70)) #Troubleshoot
                Destination=0
            #Reset
            if 50+195 > mouse[0] > 50 and 465+70 > mouse[1] > 465:
                RESET_WINDOW()
                var='0'
                ser.write(var.encode())
                var='1'    
                ser.write(var.encode())
                Destination=0
            #circ = pygame.mouse.get_pos() #Gets the mouse position
            #print(circ)
##            if flag==0:
##                flag=1
##                #pygame.draw.circle(pywindow, BLUE, (circ), 5, 0) #Draws a circle at the mouse position!
##            else:
##                #pygame.draw.circle(pywindow, RED, (circ), 5, 0) #Draws a circle at the mouse position!
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
