# displays the background

import random

class BackgroundView:
    def __init__(self, steve_run):
        self.steve_run = steve_run
        self.x = self.steve_run.SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self._image = self.steve_run.CLOUD

    def draw(self, SCREEN):
        SCREEN.blit(self._image, (self.x, self.y))
