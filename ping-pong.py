import pygame
import random
import sys

x = 500
y = 500

sbreite = 100
shoehe = 15

sx = 200
sy = 450

bx = int(x/2)
by = int(y/2)

bradius = 15

speed = 0

bxspeed = 1
byspeed = -2
leben = 3

pygame.init()
screen = pygame.display.set_mode((x, y))
screen.fill((0, 0, 0))

pygame.draw.circle(screen, (255, 255, 0), (bx, by), bradius, 0)
pygame.draw.rect(screen, (255, 40, 0), (sx, sy, sbreite,shoehe), 0)
pygame.display.flip()

def sblock():
    global speed
    if sx <= 0 or sx >= x-sbreite:
        speed = 0

def ballbewegung():
    global bx, by
    bx += bxspeed
    by += byspeed

def reset():
    global byspeed,bxspeed,leben,bx,by,sx,sy,speed
    sx = 200
    sy = 450

    bx = int(x/2)
    by = int(y/2)

    speed = 0
    bxspeed = random.randint(-2,2)
    if bxspeed == 0:
        bxspeed = 1
    byspeed = random.randint(-2,2)
    if byspeed == 0:
        byspeed = 2
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 0), (bx, by), bradius, 0)
    pygame.draw.rect(screen, (255, 40, 0), (sx, sy, sbreite,shoehe), 0)
    pygame.display.flip()
    pygame.time.wait(1000)

def ballblock():
    global byspeed,bxspeed,leben
    if by-bradius <= 0:
        byspeed *= -1
    if bx-bradius <= 0:
        bxspeed *= -1
    if bx+bradius >= x:
        bxspeed *= -1
    if by >= 435 and by <= 440:
        if bx >= sx-15 and bx <= sx+sbreite+15:
            byspeed *= -1
        else:
            leben -= 1
            reset()

def sbewegung():
    global sx
    sx += speed

while leben>0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = -2
            if event.key == pygame.K_RIGHT:
                speed = 2

    screen.fill((0, 0, 0))
    sbewegung()
    sblock()
    pygame.draw.rect(screen, (255, 40, 0), (sx, sy, sbreite,shoehe), 0)
    ballbewegung()
    ballblock()
    pygame.draw.circle(screen, (255, 255, 0), (bx, by), bradius, 0)
    pygame.display.flip()
    pygame.time.wait(5)

print("Du Loser!")


    
    
        
    


            
    
       
