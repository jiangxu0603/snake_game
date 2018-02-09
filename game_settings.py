class Settings():
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_size = (self.screen_width, self.screen_height)
        self.bg_color = (0xFF, 0xFF, 0xFF)
        self.FullScreen = False

        """蛇的相关设置"""
        # 游戏速度
        self.snake_speed_factor = 1
        # 蛇的初始长度
        self.snake_node_radius = self.snake_speed_factor * 20
        self.snake_node_width = 3
        self.snake_color = (0xFF, 0x40, 0x40)


