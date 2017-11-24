import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()

    #实例化一个Settings类，以方便调用参数
    ai_settings = Settings()

    #设置屏幕宽高
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #设置屏幕title
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(ai_settings, screen)
    #创建一个用于存储子弹的编组
    bullets = Group()

    # #设置背景色
    # bg_color = ai_settings.bg_color

    #开始游戏的主循环
    while True:

        #检查事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # #监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        #飞船状态更新 左移/右移
        ship.update()

        gf.update_bullets(bullets)
        # bullets.update()
        #
        # #删除已经消失的子弹
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom <= 0:
        #         bullets.remove(bullet)
        # # print(len(bullets))

        #更新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)
        # #屏幕填充背景色
        # screen.fill(bg_color)
        # #循环时绘制✈️
        # ship.blitme()
        # #让最近绘制的屏幕可见
        # pygame.display.flip()

run_game()