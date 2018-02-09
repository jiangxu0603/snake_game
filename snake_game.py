
# import sys
# import pygame
#
# from settings import Settings
# from ship import Ship
# from alien import Alien
# from pygame.sprite import Group
# from game_stats import GameStats
# import game_functions as gf
#
#
# def run_game():
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 创建一个飞船
#     ship = Ship(screen, ai_settings)
#     # 创建一个用于储存子弹的编组
#     bullets = Group()
#     # 创建一个用于储存外形人的编组
#     aliens= Group()
#     gf.create_fleet(ai_settings, screen, ship, aliens)
#     alien = Alien(ai_settings, screen)
#     # 创建用于储存游戏统计信息的实例
#     stats = GameStats(ai_settings)
#     while True:
#         gf.check_events(ai_settings, screen, ship, bullets)
#         if stats.game_active:
#             ship.update()
#             gf.check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
#             # 删除消失的子弹
#             gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
#             gf.update_aliens(ai_settings, aliens, stats, ship, screen, bullets)
#         gf.update_screen(ai_settings, screen, ship, aliens, bullets)
#
import pygame
import game_functions as gf
from game_settings import Settings
from button import Button
from snake import Snake
from food import Food
from pygame.sprite import Group


def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Snake Game")
    # 创建开始按钮
    play_button = Button(game_settings, screen, "Play")
    # 创建贪吃蛇
    snake = Snake(game_settings, screen)
    # 获取Clock对象，来实现固定速度
    clock = pygame.time.Clock()
    # 创建一个food
    foods = Group()
    foods.add(Food(screen, game_settings))
    # 通过时间控制刷新率
    time_passed_seconds = 0
    while True:
        # 计算经过的时间
        time_passed_seconds += clock.tick() / 1000.0
        gf.check_events(game_settings, screen, snake)
        if time_passed_seconds >= 0.5:
            snake.update(time_passed_seconds, game_settings)
            time_passed_seconds = 0
        gf.update_screen(game_settings, screen, snake, foods)


run_game()