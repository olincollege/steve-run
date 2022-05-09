# determines what steve does in response to keyboard inputs and touching obstacles. Sends that data to the model (ex: space bar is pressed --> this controller tells the model that steve is 'jumping' right now --> model state (the 'jumping' variable) is read by view to update steve's view --> after a period of time steve is not jumping anymore (either make this time based or y-level based) --> controller updates this to the model --> view reads this from model and updates steve's view)

import pygame
from steve_run import SteveRun

class SteveController:
    X_POSITION = 80
    Y_POSITION = 310
    Y_POSITION_DUCKING = 340
    JUMP_VELOCITY = 8.5

    def __init__(self, steve_run):
        self.steve_run = steve_run

        self.duck_image = SteveRun.DUCKING_IMAGE
        self.run_image = SteveRun.RUNNING_IMAGE
        self.jump_image = SteveRun.JUMPING_IMAGE

        self.steve_ducking = False
        self.steve_running = True
        self.steve_jumping = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VELOCITY
        # self.image = self.run_image[0]
        self.steve_rect = self.steve_run.image().get_rect()
        self.steve_rect.x = self.X_POSITION
        self.steve_rect.y = self.Y_POSITION

    def update(self, user_input):
        if self.steve_ducking:
            self.duck()
        if self.steve_running:
            self.run()
        if self.steve_jumping:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.steve_jumping:
            self.steve_ducking = False
            self.steve_running = False
            self.steve_jumping = True
        elif user_input[pygame.K_DOWN] and not self.steve_jumping:
            self.steve_ducking = True
            self.steve_running = False
            self.steve_jumping = False
        elif not (self.steve_jumping or user_input[pygame.K_DOWN]):
            self.steve_ducking = False
            self.steve_running = True
            self.steve_jumping = False

    def duck(self):
        self.image = self.duck_image[self.step_index // 5]
        self.steve_run.update_image(self.image)
        self.steve_rect = self.image.get_rect()
        self.steve_rect.x = self.X_POSITION
        self.steve_rect.y = self.Y_POSITION_DUCKING
        self.step_index += 1

    def run(self):
        self.image = self.run_image[self.step_index // 5]
        self.steve_run.update_image(self.image)
        self.steve_rect = self.image.get_rect()
        self.steve_rect.x = self.X_POSITION
        self.steve_rect.y = self.Y_POSITION
        self.step_index += 1

    def jump(self):
        self.image = self.jump_image
        self.steve_run.update_image(self.image)
        if self.steve_jumping:
            self.steve_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VELOCITY:
            self.steve_jumping = False
            self.jump_vel = self.JUMP_VELOCITY
