# this is the model. it holds all the informtion and is changed (wel, an instance of it is changed) by the controllers. From there, the view can read in the model and change the view

import pygame
import os


class SteveRun:
    pygame.init()
    clock = pygame.time.Clock()

    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 900
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    FONT = pygame.font.Font('freesansbold.ttf', 20)
    BG = pygame.image.load(os.path.join("Assets/Other", "Background.png"))
    BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))

    steve_run_1 = pygame.image.load(os.path.join("Assets/Steve", "SteveRun1.png"))
    steve_run_2 = pygame.image.load(os.path.join("Assets/Steve", "SteveRun2.png"))
    RUNNING_IMAGE = [pygame.transform.scale(steve_run_1, (75, 100)),
                     pygame.transform.scale(steve_run_2, (75, 100))]
    steve_jump = pygame.image.load(os.path.join("Assets/Steve", "SteveJump.png"))
    JUMPING_IMAGE = pygame.transform.scale(steve_jump, (75, 100))
    steve_duck_1 = pygame.image.load(os.path.join("Assets/Steve", "SteveDuck1.png"))
    steve_duck_2 = pygame.image.load(os.path.join("Assets/Steve", "SteveDuck2.png"))
    DUCKING_IMAGE = [pygame.transform.scale(steve_duck_1, (75, 100)),
                     pygame.transform.scale(steve_duck_2, (75, 100))]

    small_mark_1 = pygame.image.load(os.path.join("Assets/Zuckerberg", "SmallZuckerberg1.png"))
    small_mark_2 = pygame.image.load(os.path.join("Assets/Zuckerberg", "SmallZuckerberg2.png"))
    small_mark_3 = pygame.image.load(os.path.join("Assets/Zuckerberg", "SmallZuckerberg3.png"))
    large_mark_1 = pygame.image.load(os.path.join("Assets/Zuckerberg", "LargeZuckerberg1.png"))
    large_mark_2 = pygame.image.load(os.path.join("Assets/Zuckerberg", "LargeZuckerberg2.png"))
    large_mark_3 = pygame.image.load(os.path.join("Assets/Zuckerberg", "LargeZuckerberg3.png"))
    SMALL_OBSTACLE_IMAGE = [pygame.transform.scale(small_mark_1, (125, 100)),
                            pygame.transform.scale(small_mark_2, (125, 100)),
                            pygame.transform.scale(small_mark_3, (125, 100))]
    LARGE_OBSTACLE_IMAGE = [pygame.transform.scale(large_mark_1, (150, 100)),
                            pygame.transform.scale(large_mark_2, (150, 100)),
                            pygame.transform.scale(large_mark_3, (150, 100))]
    helicopter_1 = pygame.image.load(os.path.join("Assets/Helicopter", "Helicopter1.png"))
    helicopter_2 = pygame.image.load(os.path.join("Assets/Helicopter", "Helicopter2.png"))
    FLYING_OBSTACLE_IMAGE = [pygame.transform.scale(helicopter_1, (225, 100)),
                             pygame.transform.scale(helicopter_2, (225, 100))]

    CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))
  
    def __init__(self):
        self._points = 0
        self._game_speed = 20
        self._death_count = 0
        self._image = self.RUNNING_IMAGE[0]
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self._obstacles = []

    def score(self):
        self._points += 1
        if self._points % 100 == 0:
            self._game_speed += 1
        text = self.FONT.render("Points: " + str(self._points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        self.SCREEN.blit(text, textRect)

    def background(self):
        image_width = self.BG.get_width()
        self.SCREEN.blit(self.BG, (self.x_pos_bg, self.y_pos_bg))
        self.SCREEN.blit(self.BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.SCREEN.blit(self.BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed()

    def points(self):
        return self._points

    def game_speed(self):
        return self._game_speed

    def death_count(self):
        return self._death_count

    def increase_death_count(self):
        self._death_count += 1

    def reset_death_count(self):
        self._death_count = 0

    def image(self):
        return self._image

    def update_image(self, new_image):
        self._image = new_image

    def obstacles(self):
        return self._obstacles

    def add_to_obstacles(self, new_obstacle):
        self._obstacles.append(new_obstacle)
