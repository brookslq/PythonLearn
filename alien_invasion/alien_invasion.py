import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()

    #实例化一个Settings类，以方便调用参数
    ai_settings = Settings()

    #设置屏幕宽高
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #设置屏幕title
    pygame.display.set_caption("Alien Invasion")

    #创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    #创建一艘飞船
    ship = Ship(ai_settings, screen)
    #创建一个用于存储子弹的编组
    bullets = Group()


    # #创建一个外星人
    # alien = Alien(ai_settings, screen)

    #创建外星人编组
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # #设置背景色
    # bg_color = ai_settings.bg_color

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #开始游戏的主循环
    while True:
        #检查事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        # #监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()


        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)



        # #飞船状态更新 左移/右移
        # ship.update()
        #
        # gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        # # bullets.update()
        # #
        # # #删除已经消失的子弹
        # # for bullet in bullets.copy():
        # #     if bullet.rect.bottom <= 0:
        # #         bullets.remove(bullet)
        # # # print(len(bullets))
        #
        # #更新屏幕
        # gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        # # #屏幕填充背景色
        # # screen.fill(bg_color)
        # # #循环时绘制✈️
        # # ship.blitme()
        # # #让最近绘制的屏幕可见
        # # pygame.display.flip()
        #
        # #更新外星人位置
        # gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)


run_game()