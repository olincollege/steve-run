'''
Controller for the character in the game, Steve.

Takes in keyboard inputs and moves Steve based upon it.
'''

import pygame
from steve_run import SteveRun


class SteveController:
    '''
    Class representing a controller for the player/character in the game.

    Attributes:
        X_POSITION: an integer representing the horizontal position of Steve's
            character image. It is the left side of the image.
        Y_POSITION = an integer representing the vertical position of Steve's
            character image. It is the top of the image.
        Y_POSITION_CROUCHING: an integer representing the vertical position of
            Steve's character image when he is crouching.
        JUMP_VELOCITY: a float representing the maximum velocity achieved by
            Steve when he jumps. This is achieved at the beginning and end of
            the jump.
        steve_run: an instance of the SteveRun class, representing the current
            instance of the game.
        crouch_image: an array of 2 images representing Steve when crouching to
            avoid flying obstacles. Alternating between these images simulates
            a running animation.
        run_image: an array of 2 images representing Steve when running
            normally.  Alternating between these images simulates a running
            animation.
        jump_image: an image representing Steve when jumping.
        steve_crouching: a boolean representing whether Steve is currently
            crouching or not.
        steve_running = a boolean representing whether Steve is currently
            running or not.
        steve_jumping = a boolean representing whether Steve is currently
            jumping or not.
        step_index: an integer representing the duration each frame of a
            running/crouching animation lasts.
        jump_velocity: a float representing the speed at which Steve is rising
            or falling over the duration of a jump.
        steve_rect: an array of 2 integers representing the size of Steve's
            image.
        steve_rect.x: an integer representing the x-dimension of Steve's image.
        steve_rect.y: an integer representing the y-dimension of Steve's image.
    '''
    X_POSITION = 80
    Y_POSITION = 310
    Y_POSITION_CROUCHING = 340
    JUMP_VELOCITY = 8.5

    def __init__(self, steve_run):
        '''
        Args:
            steve_run: an instance of the SteveRun class, representing the
                current game being played.
        '''
        self.steve_run = steve_run

        self.crouch_image = SteveRun.CROUCHING_IMAGE
        self.run_image = SteveRun.RUNNING_IMAGE
        self.jump_image = SteveRun.JUMPING_IMAGE

        self.steve_crouching = False
        self.steve_running = True
        self.steve_jumping = False

        self.step_index = 0
        self.jump_velocity = self.JUMP_VELOCITY
        self.steve_rect = self.steve_run.image().get_rect()
        self.steve_rect.x = self.X_POSITION
        self.steve_rect.y = self.Y_POSITION

    def update(self, user_input):
        '''
        Changes Steve's state based on keyboard input and jumping status.

        Args:
            user_input: the input read in from the player's keyboard.
        '''
        if self.steve_crouching:
            self.crouch()
        if self.steve_running:
            self.run()
        if self.steve_jumping:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_SPACE] and not self.steve_jumping:
            self.steve_crouching = False
            self.steve_running = False
            self.steve_jumping = True
        elif user_input[pygame.K_LSHIFT] and not self.steve_jumping:
            self.steve_crouching = True
            self.steve_running = False
            self.steve_jumping = False
        elif not (self.steve_jumping or user_input[pygame.K_LSHIFT]):
            self.steve_crouching = False
            self.steve_running = True
            self.steve_jumping = False

    def crouch(self):
        '''
        Changes Steve's state to be 'crouching', and updates the model.
        '''
        self.image = self.crouch_image[self.step_index // 5]
        self.steve_run.update_image(self.image)
        self.steve_rect = self.image.get_rect()
        self.steve_rect.x = self.X_POSITION
        self.steve_rect.y = self.Y_POSITION_CROUCHING
        self.step_index += 1

    def run(self):
        '''
        Changes Steve's state to be 'running', and updates the model.
        '''
        self.image = self.run_image[self.step_index // 5]
        self.steve_run.update_image(self.image)
        self.steve_rect = self.image.get_rect()
        self.steve_rect.x = self.X_POSITION
        self.steve_rect.y = self.Y_POSITION
        self.step_index += 1

    def jump(self):
        '''
        Changes Steve's state to be 'jumping', and updates the model.
        '''
        self.image = self.jump_image
        self.steve_run.update_image(self.image)
        if self.steve_jumping:
            self.steve_rect.y -= self.jump_velocity * 4
            self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.steve_jumping = False
            self.jump_velocity = self.JUMP_VELOCITY
