import sys

import pygame

from Source.component import GameStatus
from Source.component import MineBlock
from Source.setting import Settings


def print_text(screen, font, x, y, text, fcolor):
    imgText = font.render(text, True, fcolor)
    textRect = imgText.get_rect()
    textRect.center = (x,y)
    screen.blit(imgText, textRect)


def game_clock(screen, setting):
    pygame.time.get_ticks()
    if pygame.time.get_ticks() % 1000 == 0:
        setting.timer = setting.timer - 1
        clock_g = str(setting.timer)
        largeText = pygame.font.SysFont('comicsansms', 25)
        TextSurf, TextRect = text_objects(clock_g, largeText)
        TextRect.center = (750, (setting.display_height / 10))
        screen.blit(TextSurf, TextRect)
        pygame.display.update()
        setting.clock.tick(15)


def text_objects(text, font):
    textSurface = font.render(text, True, 'black')
    # 在一个新 Surface 对象上绘制文本
    return textSurface, textSurface.get_rect()


def create_rect(screen, width, height, border, color, border_color, x, y):
    surf = pygame.Surface((width + border * 2, height + border * 2), pygame.SRCALPHA)
    pygame.draw.rect(surf, color, (border, border, width, height), 0)
    for i in range(1, border):
        pygame.draw.rect(surf, border_color, (border - i, border - i, width + 5, height + 5), 1)
    screen.blit(surf, (x, y))


def main():
    pygame.init()

    setting = Settings()
    screen = pygame.display.set_mode((setting.display_width, setting.display_height))
    pygame.display.set_caption("Puzzle")

    font = pygame.font.Font("resources/a.TTF", setting.SIZE)
    fwidth, fheight = font.size('999')

    block = MineBlock.MineBlock()
    game_status = GameStatus.GameStatus.readied
    start_time = None
    elapsed_time = 0
    fcolor = (0, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_F1:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, (192, 192, 192), (150, 30, 400, 20))
        pygame.draw.rect(screen, (0, 0, 255), (150, 30, setting.step % 400, 20))

        print_text(screen, font, 575, 400, str(111), fcolor)
        print_text(screen, font, 65, 100, "试错次数:3", fcolor)

        create_rect(35, 35, 3, 'white', (0, 0, 0), 650, 83)
        print_text(screen, font, 671, 104, "0", fcolor)

        create_rect(screen, setting.rect_width, setting.rect_height, 3, 'white', (0, 0, 0), setting.rect_x,
                    setting.rect_y)

        count = 1
        spray = 1
        while count <= setting.rank - 1:
            pygame.draw.line(screen, (0, 0, 0),
                             [setting.rect_x + spray, setting.rect_y + count * setting.rect_height / setting.rank],
                             [setting.rect_x + setting.rect_width + 4 * spray,
                              setting.rect_y + count * setting.rect_height / setting.rank], 2)
            pygame.draw.line(screen, (0, 0, 0),
                             [setting.rect_x + count * setting.rect_width / setting.rank, setting.rect_y + spray],
                             [setting.rect_x + count * setting.rect_width / setting.rank,
                              setting.rect_y + setting.rect_height + 4 * spray], 2)
            count += 1

        game_clock()

        setting.step += 1
        setting.clock.tick(60)

        pygame.display.flip()
