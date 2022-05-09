# controls the background based on time (?)

import random
from steve_run import SteveRun

class BackgroundController:
    def __init__(self, steve_run):
        self.steve_run = steve_run
        self.x = SteveRun.SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.width = self.steve_run.image().get_width()

    def update(self):
        self.x -= self.steve_run.game_speed()
        if self.x < -self.width:
            self.x = SteveRun.SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)
