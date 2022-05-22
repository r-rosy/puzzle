import pygame
import sys

WIDTH = 750  # 1000
HEIGHT = 650  # 600
FPS = 30  # 帧率
score = 0  # 游戏分数
x = 3
# 初始化
pygame.init()
pygame.mixer.init()  # 声音初始化
# 设置背景音乐
sound = pygame.mixer.Sound('bgm.mp3')

# 生成带边框矩阵，参数为(宽度，高度，边框厚度，矩阵内部颜色，边框颜色，左上角坐标)
def create_rect(screen, width, height, border, color, border_color, x, y):
    surf = pygame.Surface((width+border*2, height+border*2), pygame.SRCALPHA)
    pygame.draw.rect(surf, color, (border, border, width, height), 0)
    for i in range(1, border):
        pygame.draw.rect(surf, border_color, (border-i, border-i, width+5, height+5), 1)
    screen.blit(surf, (x, y))

# 结束窗口
def result_screen(screen, score):
    # 填充窗口颜色
    screen.fill((184, 235, 203))
    # 刷新屏幕
    pygame.display.update()
    # 加载退出符号按钮图像
    exit_location = 'exit.png'
    exit = pygame.image.load(exit_location)
    # 绘制退出符号按钮图像

    exit_img = pygame.transform.scale(exit, (100, 100), )  # 规定大小
    screen.blit(exit_img, (220, 380))
    # 加载返回符号按钮图像
    back_location = 'return.png'
    back = pygame.image.load(back_location)
    # 绘制返回符号按钮图像
    back_img = pygame.transform.scale(back, (100, 100), )
    screen.blit(back_img, (425, 380))
    # 生成退出圆圈(颜色，位置，半径，边框大小)
    pygame.draw.circle(screen, (0, 0, 0), (270, 430), 65, 5)
    # 生成返回圆圈(颜色，位置，半径，边框大小)
    pygame.draw.circle(screen, (0, 0, 0), (476, 430), 65, 5)
    # 加载结算符号按钮图像
    victory_location = 'victory.png'
    victory = pygame.image.load(victory_location)
    # 绘制结算符号按钮图像
    victory_img = pygame.transform.scale(victory, (150, 150), )
    screen.blit(victory_img, (300, 50))
    # 绘制分数图片
    a = pygame.freetype.Font(None, 36)
    b = a.render_to(screen, (350, 250), str(score), (0, 0, 0), size=80)


    pygame.display.update()


def ready_go(screen):
    # 填充窗口颜色
    screen.fill((184, 235, 203))
    # 刷新屏幕
    pygame.display.update()
    # 绘制分数图片
    a = pygame.freetype.Font(None, 36)
    b = a.render_to(screen, (240, 200), "Ready", (255, 120, 80), size=100)
    c = a.render_to(screen, (300, 350), "Go!", (255, 120, 80), size=100)
    pygame.display.update()
    t = pygame.time.wait(1000)  # 暂停时间1000ms


def text_objects(text, font):
    textSurface = font.render(text, True, 'black')
    # 在一个新 Surface 对象上绘制文本
    return textSurface, textSurface.get_rect()


def game(x, score):
    result = "false"
    if x == 3:
        result = "true"
    elif x == 4:
        result = "true"
    if result == "true":
        score += x
    return result, score

def main():
    # 创建主界面
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # 填充窗口颜色
    screen.fill((184, 235, 203))
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
    pygame.draw.circle(screen, (0, 0, 0), (650, 80), 50, 5)
    # 加载start标签
    start_location = 'START.jpg'
    start = pygame.image.load(start_location)
    start_img = pygame.transform.scale(start, (260, 60),)
    start_rect = start_img.get_rect()
    start_rect.centerx = WIDTH / 2  # 这样写更精确
    start_rect.centery = 320
    # screen.blit(start_img, (250, 285))
    screen.blit(start_img, start_rect)
    # 加载exit标签
    exit_location = 'EXIT.jpg'
    exit = pygame.image.load(exit_location)
    exit_img = pygame.transform.scale(exit, (200, 60), )
    exit_rect = exit_img.get_rect()
    exit_rect.centerx = WIDTH/2  # 这样写更精确
    exit_rect.centery = 420
    # screen.blit(exit_img, (280, 385))
    screen.blit(exit_img, exit_rect)
    # 加载音乐符号按钮图像
    music_location = 'music.png'
    music = pygame.image.load(music_location)
    # 绘制音乐符号按钮图像
    music_img = pygame.transform.scale(music, (60, 60),)
    screen.blit(music_img, (616, 45))
    # 绘制直线(画在哪，线的颜色，线的起点，线的终点，线宽)
    pygame.draw.line(screen, (0, 0, 0), (615, 45), (687, 110), 5)
    screen.blit(screen, (0, 0))
    pygame.display.update()
    # 加载小人图像
    man_location = 'man.png'
    man = pygame.image.load(man_location)
    # 绘制小人图像
    man_img = pygame.transform.scale(man, (150, 150),)
    man_rect = man_img.get_rect()
    man_rect.centerx = WIDTH / 2 -100  # 这样写更精确
    man_rect.centery = 150
    screen.blit(man_img, man_rect)
    # 加载平行四边形图像
    parallelogram_location = 'parallelogram.png'
    parallelogram = pygame.image.load(parallelogram_location)
    # 绘制平行四边形图像
    parallelogram_img = pygame.transform.scale(parallelogram, (100, 100),)
    parallelogram_rect = parallelogram.get_rect()
    parallelogram_rect.centerx = WIDTH / 2 + 250
    parallelogram_rect.centery = 230
    screen.blit(parallelogram_img, parallelogram_rect)
    parallelogram_rect.centerx = WIDTH / 2 + 350
    parallelogram_rect.centery = 230
    screen.blit(parallelogram_img, parallelogram_rect)

    # 设置不在窗口显示鼠标
    # pygame.mouse.set_visible(False)
    # 设置鼠标位置不离开窗口
    # pygame.event.set_grab(True)

    # 用于记录音乐开关，默认为关
    flag = 0
    stage = 1 # 阶段1：主界面
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
                print('鼠标按下编号', event.button)  # event.button表示鼠标按下键编号，左键为1，中间为2， 右键为3
                if mouse_up == 1 and stage == 1:  # 鼠标左击 阶段1
                    if abs(mouse_x - 650) <= 45 and abs(mouse_y - 80) <= 45:
                        print('在区域内')
                        if flag == 0:  # flag == 0 表示要打开音乐
                            pygame.draw.line(screen, (184, 235, 203), (615, 45), (687, 110), 5)
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
                    elif abs(mouse_x - WIDTH/2) <= 130 and abs(mouse_y - start_rect.centery) <= 30:
                        print('开始游戏')  # 下面加开始游戏后的代码
                        stage = 2  # 阶段2：Ready Go!
                        ready_go(screen)
                    elif abs(mouse_x - WIDTH / 2) <= 100 and abs(mouse_y - exit_rect.centery) <= 30:
                        # 卸载所有pygame模块
                        pygame.quit()
                        # 终止程序
                        sys.exit()
                elif stage == 2:  # 这里是虽然标的是2，实际上没有加入游戏，实际上应该是3
                    score = 0
                    for x in range(3, 6):  # 从3*3的规格开始依次增加
                        result, score = game(x, score)
                        if result == "false":
                            break
                    stage = 3
                elif stage == 3:
                    result_screen(screen, score)
                    if abs(mouse_x - 270) <= 65 and abs(mouse_y - 430) <= 65:
                        print('exit')
                        # 卸载所有pygame模块
                        pygame.quit()
                        # 终止程序
                        sys.exit()
                    elif abs(mouse_x - 476) <= 65 and abs(mouse_y - 430) <= 65:
                        print('return')
                        stage = 1
                        # 填充窗口颜色
                        screen.fill((184, 235, 203))
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
                        pygame.draw.circle(screen, (0, 0, 0), (650, 80), 50, 5)
                        # 加载start标签
                        start_location = 'START.jpg'
                        start = pygame.image.load(start_location)
                        start_img = pygame.transform.scale(start, (260, 60), )
                        start_rect = start_img.get_rect()
                        start_rect.centerx = WIDTH / 2  # 这样写更精确
                        start_rect.centery = 320
                        # screen.blit(start_img, (250, 285))
                        screen.blit(start_img, start_rect)
                        # 加载exit标签
                        exit_location = 'EXIT.jpg'
                        exit = pygame.image.load(exit_location)
                        exit_img = pygame.transform.scale(exit, (200, 60), )
                        exit_rect = exit_img.get_rect()
                        exit_rect.centerx = WIDTH / 2  # 这样写更精确
                        exit_rect.centery = 420
                        # screen.blit(exit_img, (280, 385))
                        screen.blit(exit_img, exit_rect)
                        # 加载音乐符号按钮图像
                        music_location = 'music.png'
                        music = pygame.image.load(music_location)
                        # 绘制音乐符号按钮图像
                        music_img = pygame.transform.scale(music, (60, 60), )
                        screen.blit(music_img, (616, 45))
                        # 绘制直线(画在哪，线的颜色，线的起点，线的终点，线宽)
                        pygame.draw.line(screen, (0, 0, 0), (615, 45), (687, 110), 5)
                        screen.blit(screen, (0, 0))
                        pygame.display.update()
                        # 加载小人图像
                        man_location = 'man.png'
                        man = pygame.image.load(man_location)
                        # 绘制小人图像
                        man_img = pygame.transform.scale(man, (150, 150), )
                        man_rect = man_img.get_rect()
                        man_rect.centerx = WIDTH / 2 - 100  # 这样写更精确
                        man_rect.centery = 150
                        screen.blit(man_img, man_rect)
                        # 加载平行四边形图像
                        parallelogram_location = 'parallelogram.png'
                        parallelogram = pygame.image.load(parallelogram_location)
                        # 绘制平行四边形图像
                        parallelogram_img = pygame.transform.scale(parallelogram, (100, 100), )
                        parallelogram_rect = parallelogram.get_rect()
                        parallelogram_rect.centerx = WIDTH / 2 + 250
                        parallelogram_rect.centery = 230
                        screen.blit(parallelogram_img, parallelogram_rect)
                        parallelogram_rect.centerx = WIDTH / 2 + 350
                        parallelogram_rect.centery = 230
                        screen.blit(parallelogram_img, parallelogram_rect)

        # 更新屏幕内容
        pygame.display.flip()


if __name__ == '__main__':
        main()
