import random

class ObstacleView:
    def __init__(self, steve_run, image, type):
        '''
        Args:
        image: __
        type: ___
        '''
        self._steve_run = steve_run
        self._image = image
        self.type = type
        # self.game_speed = game_speed
        self.rect = self._image[self.type].get_rect()
        self.rect.x = self.steve_run.SCREEN_WIDTH

    def update(self):
        '''
        '''
        self.rect.x -= self._steve_run.game_speed()
        if self.rect.x < -self.rect.width:
            self._steve_run.obstacles().pop()
            del self

    def draw(self, SCREEN):
        '''
        '''
        SCREEN.blit(self._image[self.type], self.rect)

class SmallMarkView(ObstacleView):
    def __init__(self, steve_run, image):
        '''
        '''
        self.steve_run = steve_run
        self.type = random.randint(0, 2)
        super().__init__(steve_run, image, self.type)
        self.rect.y = 325

class LargeMarkView(ObstacleView):
    def __init__(self, steve_run, image):
        self.steve_run = steve_run
        self.type = random.randint(0, 2)
        super().__init__(steve_run, image, self.type)
        self.rect.y = 300

class HelicopterView(ObstacleView):
    def __init__(self, steve_run, image):
        self.steve_run = steve_run
        self.image = image
        self.type = 0
        super().__init__(steve_run, image, self.type)
        self.rect.y = 225
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1
