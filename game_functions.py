import sys
import pygame
import copy
from snake import Node
from food import Food


def check_events(game_settings, screen, snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                game_settings.FullScreen = not game_settings.FullScreen
                if game_settings.FullScreen:
                    screen = pygame.display.set_mode(game_settings.screen_size, pygame.FULLSCREEN, 0)
                else:
                    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
            # 判断方向，切不能改变成相反的方向
            if event.key == pygame.K_UP and snake.direction != 'down':
                snake.direction = 'up'
            elif event.key == pygame.K_DOWN and snake.direction != 'up':
                snake.direction = 'down'
            elif event.key == pygame.K_LEFT and snake.direction != 'right':
                snake.direction = 'left'
            elif event.key == pygame.K_RIGHT and snake.direction != 'left':
                snake.direction = 'right'
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                pass


def update_screen(game_settings, screen, snake, foods):
    screen.fill(game_settings.bg_color)
    snake.draw_snake(game_settings)
    update_snake(snake, foods, screen, game_settings)
    for food in foods:
        food.draw()
    # play_button.draw_button()
    # pygame.draw.circle(screen, (255, 0, 0), (300, 300), 500)
    pygame.display.flip()


def _add_node(snake, game_settings):
    length = game_settings.snake_node_radius * 2
    add_node = copy.copy(snake.nodes_list[0])
    if snake.direction == 'up':
        add_node.y += length
    elif snake.direction == 'down':
        add_node.y -= length
    elif snake.direction == 'left':
        add_node.x -= length
    elif snake.direction == 'right':
        add_node.x += length
    snake.nodes_list.insert(0, add_node)


def update_snake(snake, foods, screen, game_settings):
    # 如果碰撞，将对应的果实吃掉
    attacker = None
    attacker = pygame.sprite.spritecollideany(snake, foods)
    if attacker:
        foods.remove(attacker)
        # 吃掉果实后，增加一个新的果实
        foods.add(Food(screen, game_settings))
        # 增加蛇的长度
        _add_node(snake, game_settings)