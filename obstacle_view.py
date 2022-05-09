'''
View for all the obstacles.
'''

import random

class ObstacleView:
    '''
    The general view for all obstacles.

    Attributes:
        steve_run: an instance of the SteveRun class, representing the current
            game being played.
        image: a list of images, representing the obstacles that can be
            displayed.
        type: an integer representing which, among the values of the
            `image` array, will be used.
        rect: an array of 2 integers, representing the dimensions of the
            obstacle image.
        rect.x: the x-dimension of the obstacle image selected.
    '''
    def __init__(self, steve_run, image, type):
        '''
        Args:
            steve_run: an instance of the SteveRun class.
            image: a list of images representing the options for all obstacles
                of the specified kind to be displayed.
            type: an integer representing which, among the values of the
                `image` array, will be used.
        '''
        self._steve_run = steve_run
        self._image = image
        self.type = type
        self.rect = self._image[self.type].get_rect()
        self.rect.x = self.steve_run.SCREEN_WIDTH

    def update(self):
        '''
        Once an obstacle moves off the screen on the left side, remove it from
        the list of obstacles.
        '''
        self.rect.x -= self._steve_run.game_speed()
        if self.rect.x < -self.rect.width:
            self._steve_run.obstacles().pop()
            del self

    def draw(self, SCREEN):
        '''
        Draw the obstacle in the game window.
        '''
        SCREEN.blit(self._image[self.type], self.rect)


class SmallMarkView(ObstacleView):
    '''
    The view for small obstacles.
    '''
    def __init__(self, steve_run, image):
        '''
        Args:
            steve_run: an instance of the SteveRun class.
            image: a list of images representing the options for all small
                obstacles to be displayed.
        '''
        self.steve_run = steve_run
        self.type = random.randint(0, 2)
        super().__init__(steve_run, image, self.type)
        self.rect.y = 325


class LargeMarkView(ObstacleView):
    '''
    The view for large obstacles.
    '''
    def __init__(self, steve_run, image):
        '''
        Args:
            steve_run: an instance of the SteveRun class.
            image: a list of images representing the options for all large
                obstacles to be displayed.
        '''
        self.steve_run = steve_run
        self.type = random.randint(0, 2)
        super().__init__(steve_run, image, self.type)
        self.rect.y = 300


class HelicopterView(ObstacleView):
    '''
    The view for flying obstacles.
    '''
    def __init__(self, steve_run, image):
        '''
        Args:
            steve_run: an instance of the SteveRun class.
            image: a list of images representing the options for all flying
                obstacles to be displayed.
        '''
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
