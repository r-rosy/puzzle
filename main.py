import pygame,sys
from constvar import *
from config import *
from variedvar import *

def printstr(str,x,y):
    text=font.render(str,True,(0,0,0))
    textRect =text.get_rect()
    textRect.center = (x,y)
    screen.blit(text,textRect)

def create_rect(width, height, border, color, border_color,x,y):
    surf = pygame.Surface((width+border*2, height+border*2), pygame.SRCALPHA)
    pygame.draw.rect(surf, color, (border, border, width, height), 0)
    for i in range(1, border):
        pygame.draw.rect(surf, border_color, (border-i, border-i, width+5, height+5), 1)
    screen.blit(surf, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, 'black')
    # 在一个新 Surface 对象上绘制文本
    return textSurface, textSurface.get_rect()

def game_clock():
        pygame.time.get_ticks()
        if (pygame.time.get_ticks()%1000 == 0):
            timer = timer- 1
            clock_g = str(timer)
            largeText = pygame.font.SysFont('comicsansms', 25)
            TextSurf, TextRect = text_objects(clock_g, largeText)
            TextRect.center = (750, (display_height / 10))
            screen.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(15)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_F1:
            pygame.quit()
            sys.exit()

    screen.fill((255,255,255))

    pygame.draw.rect(screen,(192,192,192),(150,30,400,20))
    pygame.draw.rect(screen,(0,0,255),(150,30,step % 400,20))

    font = pygame.font.SysFont(['方正粗黑宋简体','microsoftsansserif'],20)

    printstr(str(111),575,40)
    printstr("试错次数:3",65,100)

    create_rect(35, 35, 3, 'white', (0,0,0),650,83)
    printstr("0",671,104)


    create_rect(rect_width, rect_height, 3, 'white', (0,0,0),rect_x,rect_y)

    count=1
    spray=1
    while count<=rank-1:
        pygame.draw.line(screen, (0,0,0), [rect_x+spray, rect_y+count*rect_height/rank], [rect_x+rect_width+4*spray, rect_y+count*rect_height/rank], 2)
        pygame.draw.line(screen, (0,0,0), [rect_x+count*rect_width/rank, rect_y+spray], [rect_x+count*rect_width/rank, rect_y+rect_height+4*spray], 2)
        count+=1

    game_clock()

    step += 1
    clock.tick(60)

    pygame.display.flip()