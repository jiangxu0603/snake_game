import pygame
import copy
from pygame.sprite import Sprite


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return [self.x, self.y]

    def __repr__(self):
        return 'Position(%r, %r)' % (self.x, self.y)


class Snake(Sprite):
    """管理贪吃蛇的类"""
    def __init__(self, game_settings, screen):
        # super(Snake, self).__init__()
        # self.screen = screen
        # self.screen_rect = screen.get_rect()
        #
        # self.rect = pygame.Rect(0, 0, game_settings.snake_width,
        #                         game_settings.snake_height)
        # self.rect.center = self.screen_rect.center
        # self.color = game_settings.snake_color
        # # 贪吃蛇属性
        # self.x = float(self.rect.x)
        # self.y = float(self.rect.y)
        # self.speed_factor = game_settings.snake_speed_factor
        # # 初始方向是向右
        # self.direction = 'right'

        # new
        super(Snake, self).__init__()
        # 贪吃蛇的身体节点位置信息
        self.nodes_list = []
        # 贪吃蛇的节点模型列表, 用来判断碰撞
        self.rect = 0
        self.node_rect = []
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 贪吃蛇的长度和厚度
        pass

        # 贪吃蛇的颜色
        self.color = game_settings.snake_color
        # 贪吃蛇的速度
        self.speed_factor = game_settings.snake_speed_factor
        # 贪吃蛇位置属性
        head = Node(self.screen_rect.centerx, self.screen_rect.centery)
        # self.nodes_list.append(head)
        # 初始方向是向右
        self.direction = 'right'
        node = Node(head.x - game_settings.snake_node_radius * 2, head.y)
        node1 = Node(head.x - (game_settings.snake_node_radius * 4), head.y)
        self.add_node(node)
        self.add_node(node1)

    def add_node(self, node):
        self.nodes_list.append(node)

    def eat(self, node):
        self.nodes_list.insert(0, node)

    def update(self, time_passed_seconds, game_settings):
        """根据方向和经过的时间更新蛇的位置"""
        # if self.direction == 'up':
        #     self.y -= self.speed_factor * time_passed_seconds
        #     self.rect.y = self.y
        # elif self.direction == 'down':
        #     self.y += self.speed_factor * time_passed_seconds
        #     self.rect.y = self.y
        # elif self.direction == 'left':
        #     self.x -= self.speed_factor * time_passed_seconds
        #     self.rect.x = self.x
        # elif self.direction == 'right':
        #     self.x += self.speed_factor * time_passed_seconds
        #     self.rect.x = self.x

        # new
        # 需要更新的位移
        updated_length = game_settings.snake_node_radius * 2
        head = copy.copy(self.nodes_list[0])
        for index, node in enumerate(self.nodes_list):
            print("The {index} node pos is {x}, {y}".format(index=index, x=node.x, y=node.y))
        # 根据位置更新head节点
        if self.direction == 'up':
            head.y -= updated_length
        elif self.direction == 'down':
            head.y += updated_length
        elif self.direction == 'left':
            head.x -= updated_length
        elif self.direction == 'right':
            head.x += updated_length
        self.nodes_list.insert(0, head)
        self.nodes_list.pop()

    def draw_snake(self, game_settings):
        """在屏幕上绘制蛇"""
        for index, node in enumerate(self.nodes_list):
            self.node_rect.append(pygame.draw.circle(self.screen, self.color,
                                                     [int(node.x), int(node.y)],
                                                     game_settings.snake_node_radius,
                                                     game_settings.snake_node_width))
            # print("The {index} node pos is {x}, {y}".format(index=index, x=node.x, y=node.y))

        self.rect = self.node_rect[0]
        del self.node_rect[:]
