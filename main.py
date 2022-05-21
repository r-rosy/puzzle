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

def update(new_rank):
    global rank
    global step
    global timer
    global time
    global memory_timer
    global timer_adder
    global start_ticks
    global test
    global memory_time
    start_ticks =pygame.time.get_ticks()
    time=const_time+(new_rank-const_rank)*timer_adder
    timer=const_timer+(new_rank-const_rank)*timer_adder
    step=const_step
    memory_timer=const_memory_timer+(new_rank-const_rank)*timer_adder
    memory_time=const_memory_time+(new_rank-const_rank)*timer_adder
    rank=new_rank
    test=const_test

def text_objects(text, font):
    textSurface = font.render(text, True, 'black')
    # 在一个新 Surface 对象上绘制文本
    return textSurface, textSurface.get_rect()


start_ticks =pygame.time.get_ticks()
update(3)
while True:
    if test==True:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
        if seconds>1 and memory_timer!=0: # if more than 10 seconds close the game
            memory_timer-=1
            start_ticks=pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_F1:
                pygame.quit()
                sys.exit()
        if memory_timer==0 :
            test=False
            step=0
            start_ticks=pygame.time.get_ticks()
            continue
    
        screen.fill((255,255,255))

        pygame.draw.rect(screen,(192,192,192),(150,30,400,20))
        pygame.draw.rect(screen,(0,0,255),(150,30,step % 400,20))

        font = pygame.font.SysFont(['方正粗黑宋简体','microsoftsansserif'],20)

        printstr("第"+str(rank-2)+"关",75,40)
        printstr(str(memory_timer),575,40)
        printstr("记忆时间",65,100)

        create_rect(35, 35, 3, 'white', (0,0,0),650,83)
        printstr("0",671,104)


        create_rect(rect_width, rect_width, 3, 'white', (0,0,0),rect_x,rect_y)
        create_rect(80, 40, 3, 'white', (0,0,0),display_width-150,display_height-80)
        printstr("退出",display_width-100,display_height-60)

        count=1
        spray=1
        while count<=rank-1:
            pygame.draw.line(screen, (0,0,0), [rect_x+spray, rect_y+count*rect_height/rank], [rect_x+rect_width+4*spray, rect_y+count*rect_height/rank], 2)
            pygame.draw.line(screen, (0,0,0), [rect_x+count*rect_width/rank, rect_y+spray], [rect_x+count*rect_width/rank, rect_y+rect_height+4*spray], 2)
            count+=1

        step+=400/(60*memory_time)
        clock.tick(60)
        pygame.display.flip()
    else:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
        if seconds>1 and timer!=0: # if more than 10 seconds close the game
            timer-=1
            start_ticks=pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_F1:
                pygame.quit()
                sys.exit()
            if timer==0 and event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    update(3)
                    continue
        if timer==0 :
            screen.fill('white')
            printstr("游戏结束,请按回车键重开",display_width/2-20,display_height/2)
            pygame.display.update()
            continue
    
        screen.fill((255,255,255))

        pygame.draw.rect(screen,(192,192,192),(150,30,400,20))
        pygame.draw.rect(screen,(0,0,255),(150,30,step % 400,20))

        font = pygame.font.SysFont(['方正粗黑宋简体','microsoftsansserif'],20)

        printstr("第"+str(rank-2)+"关",75,40)
        printstr(str(timer),575,40)
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

        step+=400/(60*time)
        clock.tick(60)
        pygame.display.flip()
