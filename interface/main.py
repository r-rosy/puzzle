import pygame
import sys

WIDTH = 750  # 1000
HEIGHT = 650  # 600
FPS = 30  # 帧率
# 初始化
pygame.init()
pygame.mixer.init()  # 声音初始化
# 设置背景音乐
# pygame.mixer.music.load('bgm.mp3')
sound = pygame.mixer.Sound('bgm.mp3')

# 生成带边框矩阵，参数为(宽度，高度，边框厚度，矩阵内部颜色，边框颜色，左上角坐标)
def create_rect(screen, width, height, border, color, border_color, x, y):
    surf = pygame.Surface((width+border*2, height+border*2), pygame.SRCALPHA)
    pygame.draw.rect(surf, color, (border, border, width, height), 0)
    for i in range(1, border):
        pygame.draw.rect(surf, border_color, (border-i, border-i, width+5, height+5), 1)
    screen.blit(surf, (x, y))


#def result_screen():




def main():

    # 创建主界面
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # 填充窗口颜色
    screen.fill('white')
    # 设置窗口标题
    pygame.display.set_caption("puzzle")
    # 刷新屏幕
    pygame.display.update()
    # 绘制边框
    create_rect(screen, 110, 40, 3, 'white', 'black', 320, 295)
    create_rect(screen, 90, 40, 3, 'white', 'black', 331, 395)
    # 绘制start文字
    start = pygame.font.Font(None, 60)
    startimage = start.render("start", True, 'Black')
    screen.blit(startimage, (332, 300))
    # 绘制exit文字
    exit = pygame.font.Font(None, 60)
    exitimage = exit.render("exit", True, 'Black')
    screen.blit(exitimage, (340, 400))
    # 生成圆圈(颜色，位置，半径，边框大小)
    # pygame.draw.circle(screen, (0, 0, 0), (900, 80), 50, 5)
    pygame.draw.circle(screen, (0, 0, 0), (650, 80), 50, 5)
    # 加载音乐符号按钮图像
    music_location = 'music.png'
    music = pygame.image.load(music_location)
    # 绘制音乐符号按钮图像
    music_img = pygame.transform.scale(music, (60, 60),)
    # screen.blit(music_img, (866, 45))
    screen.blit(music_img, (616, 45))
    # 绘制直线(画在哪，线的颜色，线的起点，线的终点，线宽)
    # pygame.draw.line(screen, (0, 0, 0), (866, 44), (933, 110), 5)
    pygame.draw.line(screen, (0, 0, 0), (615, 45), (687, 110), 5)
    screen.blit(screen, (0, 0))
    pygame.display.update()
    # 设置不在窗口显示鼠标
    # pygame.mouse.set_visible(False)
    # 设置鼠标位置不离开窗口
    # pygame.event.set_grab(True)
    # 循环
    # 用于记录音乐开关，默认为关
    flag = 0

    while True:
        # 循环获取事件，监听事件
        for event in pygame.event.get():
            # 判断用户是否点了关闭按钮
            if event.type == pygame.QUIT:
                # 卸载所有pygame模块
                pygame.quit()
                # 终止程序
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                mouse_up = event.button
                print('鼠标按下', event.pos)
                print('鼠标按下编号', event.button)  # event.button表示鼠标按下键编号，左键为1，右键为3
                if mouse_up == 1:
                    if abs(mouse_x - 650) <= 45 and abs(mouse_y - 80) <= 45:
                        print('在区域内')
                        if flag == 0:  # flag == 0 表示要打开音乐
                            pygame.draw.line(screen, (255, 255, 255), (615, 45), (687, 110), 5)
                            screen.blit(screen, (0, 0))
                            pygame.draw.circle(screen, (0, 0, 0), (650, 80), 50, 5)
                            screen.blit(music_img, (616, 45))
                            flag = 1
                            sound.play()
                        elif flag == 1:
                            pygame.draw.line(screen, (0, 0, 0), (615, 45), (687, 110), 5)
                            screen.blit(screen, (0, 0))
                            flag = 0
                            sound.stop()
        # 更新屏幕内容
        pygame.display.flip()


if __name__ == '__main__':
        main()
