'''
The model holding all information within a Steve Run game.
'''

import pygame
import os


class SteveRun:
    '''
    A game of Steve Run with basic functionality.

    Attributes:
        SCREEN_HEIGHT: an integer representing the height of the pygame screen.
        SCREEN_WIDTH: an integer representing the width of the pygame screen.
        SCREEN: creates a surface to build the game upon, with the dimensions
            as specified by SCREEN_WIDTH and SCREEN_HEIGHT.
        FONT: The font style and size used to display the points accumulated
            during the current game.
        BG: an image, scaled to the pygame screen size, to be used as the
            background of the game.
        RUNNING_IMAGE: an array of 2 resized images representing Steve's
            character when running normally.
        JUMPING_IMAGE = a resized image representing Steve's character when
            jumping.
        CROUCHING_IMAGE = an array of 2 resized images representing Steve's
            character when crouching.
        SMALL_OBSTACLE_IMAGE: an array of 3 resized images representing small
            obstacles.
        LARGE_OBSTACLE_IMAGE: an array of 3 resized images representing large
            obstacles.
        FLYING_OBSTACLE_IMAGE: an array of 2 resized images representing flying
            obstacles.
        points: an integer representing the amount of points the player has
            achieved in their run.
        game_speed: an integer representing how fast the background and
            obstacles are scrolling.
        caught_count: an integer representing how many times the player has
            lost (or "got caught" by Zuckerberg) since the game window was
            first opened.
        image: an image reflecting Steve's current state (running, jumping, or
            ducking).
        x_pos_bg: an integer representing the horizontal position of the
            background.
        y_pos_bg: an integer representing the vertical position of the
            background.
        obstacles: an array of obstacles currently being displayed in the game
            window. This adds new obstacles and removes old ones continually.
    '''
    pygame.init()
    clock = pygame.time.Clock()

    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 900
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    FONT = pygame.font.Font("Assets/COMIC.TTF", 20)

    BG = pygame.image.load(os.path.join("Assets/Other", "Background.png"))
    BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # loading the images
    steve_run_1 = pygame.image.load(os.path.join("Assets/Steve", "SteveRun1.png"))
    steve_run_2 = pygame.image.load(os.path.join("Assets/Steve", "SteveRun2.png"))
    steve_jump = pygame.image.load(os.path.join("Assets/Steve", "SteveJump.png"))
    steve_crouch_1 = pygame.image.load(os.path.join("Assets/Steve", "SteveDuck1.png"))
    steve_crouch_2 = pygame.image.load(os.path.join("Assets/Steve", "SteveDuck2.png"))
    steve_caught = pygame.image.load(os.path.join("Assets/Steve", "SteveCaught.png"))
    small_mark_1 = pygame.image.load(os.path.join("Assets/Zuckerberg", "SmallZuckerberg1.png"))
    small_mark_2 = pygame.image.load(os.path.join("Assets/Zuckerberg", "SmallZuckerberg2.png"))
    small_mark_3 = pygame.image.load(os.path.join("Assets/Zuckerberg", "SmallZuckerberg3.png"))
    large_mark_1 = pygame.image.load(os.path.join("Assets/Zuckerberg", "LargeZuckerberg1.png"))
    large_mark_2 = pygame.image.load(os.path.join("Assets/Zuckerberg", "LargeZuckerberg2.png"))
    large_mark_3 = pygame.image.load(os.path.join("Assets/Zuckerberg", "LargeZuckerberg3.png"))
    helicopter_1 = pygame.image.load(os.path.join("Assets/Helicopter", "Helicopter1.png"))
    helicopter_2 = pygame.image.load(os.path.join("Assets/Helicopter", "Helicopter2.png"))

    # scaling all loaded images
    RUNNING_IMAGE = [pygame.transform.scale(steve_run_1, (75, 100)),
                     pygame.transform.scale(steve_run_2, (75, 100))]
    JUMPING_IMAGE = pygame.transform.scale(steve_jump, (75, 100))
    CROUCHING_IMAGE = [pygame.transform.scale(steve_crouch_1, (75, 100)),
                     pygame.transform.scale(steve_crouch_2, (75, 100))]
    CAUGHT_IMAGE = pygame.transform.scale(steve_caught, (100, 75))
    SMALL_OBSTACLE_IMAGE = [pygame.transform.scale(small_mark_1, (75, 75)),
                            pygame.transform.scale(small_mark_2, (75, 75)),
                            pygame.transform.scale(small_mark_3, (75, 75))]
    LARGE_OBSTACLE_IMAGE = [pygame.transform.scale(large_mark_1, (150, 100)),
                            pygame.transform.scale(large_mark_2, (150, 100)),
                            pygame.transform.scale(large_mark_3, (150, 100))]
    FLYING_OBSTACLE_IMAGE = [pygame.transform.scale(helicopter_1, (225, 100)),
                             pygame.transform.scale(helicopter_2, (225, 100))]

    def __init__(self):
        '''
        Set up baseline values for a Steve Run game.
        '''
        self._points = 0
        self._game_speed = 20
        self._caught_count = 0
        self._image = self.RUNNING_IMAGE[0]
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self._obstacles = []

    def score(self):
        '''
        Edits and displays the score during a game.
        '''
        self.increase_points()
        if self.points() % 100 == 0:
            self._game_speed += 1
        text = self.FONT.render("Points: " + str(self.points()), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (self.SCREEN_WIDTH - 100, 30)
        self.SCREEN.blit(text, textRect)

    def background(self):
        '''
        Displays and scrolls the background image.
        '''
        image_width = self.BG.get_width()
        self.SCREEN.blit(self.BG, (self.x_pos_bg, self.y_pos_bg))
        self.SCREEN.blit(self.BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.SCREEN.blit(self.BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed()

    def points(self):
        '''
        Returns the `points` attribute.
        '''
        return self._points

    def increase_points(self):
        '''
        Increases the total points by 1.
        '''
        self._points += 1

    def game_speed(self):
        '''
        Returns the `game_speed` attribute.
        '''
        return self._game_speed

    def caught_count(self):
        '''
        Returns the `caught_count` attribute.
        '''
        return self._caught_count

    def increase_caught_count(self):
        '''
        Adds one to the `caught_count` attribute.
        '''
        self._caught_count += 1

    def reset_caught_count(self):
        '''
        Resets the `caught_count` attribute to be 0.
        '''
        self._caught_count = 0

    def image(self):
        '''
        Returns the `image` attribute.
        '''
        return self._image

    def update_image(self, new_image):
        '''
        Set the `image` attribute to be a new image.

        Args:
            new_image: the new image to replace the `image` attribute.
        '''
        self._image = new_image

    def obstacles(self):
        '''
        Returns the `obstacles` attribute.
        '''
        return self._obstacles

    def add_to_obstacles(self, new_obstacle):
        '''
        Adds a new obstacle to the list of all currently-displayed obstacles.
        '''
        self._obstacles.append(new_obstacle)
