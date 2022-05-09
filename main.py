'''
Main program to set up and run games of Steve Run.
'''

import pygame
import random

from steve_controller import SteveController
from steve_view import SteveView
from obstacle_view import SmallMarkView, LargeMarkView, HelicopterView
from steve_run import SteveRun


def main():
    '''
    Play a game of Steve Run.
    '''
    run = True

    steve_run = SteveRun()
    _steve_controller = SteveController(steve_run)
    _steve_view = SteveView(steve_run, _steve_controller)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SteveRun.SCREEN.fill((255, 255, 255))
        user_input = pygame.key.get_pressed()

        steve_run.background()

        _steve_view.draw(SteveRun.SCREEN)
        _steve_view._steve_controller.update(user_input)

        if len(steve_run.obstacles()) == 0:
            if random.randint(0, 2) == 0:
                steve_run.add_to_obstacles(SmallMarkView(steve_run,
                                                       SteveRun.SMALL_OBSTACLE_IMAGE))
            elif random.randint(0, 2) == 1:
                steve_run.add_to_obstacles(LargeMarkView(steve_run,
                                                       SteveRun.LARGE_OBSTACLE_IMAGE))
            elif random.randint(0, 2) == 2:
                steve_run.add_to_obstacles(HelicopterView(steve_run,
                                                       SteveRun.FLYING_OBSTACLE_IMAGE))

        for obstacle in steve_run.obstacles():
            obstacle.draw(SteveRun.SCREEN)
            obstacle.update()
            if _steve_controller.steve_rect.colliderect(obstacle.rect):
                steve_run.update_image(steve_run.CAUGHT_STEVE)
                pygame.time.delay(1000)
                steve_run.increase_caught_count()
                menu(steve_run.caught_count(), steve_run)

        steve_run.score()

        steve_run.clock.tick(30)
        pygame.display.update()


def menu(caught_count, steve_run):
    '''
    The menu that appears before/after each game.

    This menu shows your previous run score.
    '''
    run = True
    while run:
        SteveRun.SCREEN.fill((255, 255, 255))
        FONT = pygame.font.Font("Assets/COMIC.TTF", 30)

        # text = FONT.render("Use Space/Shift or Up/Down to Navigate\n", True, (0, 0, 0))
        if caught_count == 0:
            text = FONT.render("Press any Key to Start", True, (0, 0, 0))
        elif caught_count > 0:
            text = FONT.render("Press any Key to Restart", True, (0, 0, 0))
            score = FONT.render("Your Score: " + str(steve_run.points()), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SteveRun.SCREEN_WIDTH // 2, SteveRun.SCREEN_HEIGHT // 2 + 50)
            SteveRun.SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SteveRun.SCREEN_WIDTH // 2, SteveRun.SCREEN_HEIGHT // 2)
        SteveRun.SCREEN.blit(text, textRect)
        SteveRun.SCREEN.blit(SteveRun.RUNNING_IMAGE[0], (SteveRun.SCREEN_WIDTH // 2 - 20, SteveRun.SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


        # SteveRun.SCREEN.fill((255, 255, 255))
        # FONT = pygame.font.SysFont("comicsansms", 30)

        # text = "Use Space/Shift or Up/Down to Navigate\n"
        # if caught_count == 0:
        #     text = text + "Press any Key to Start"
        # elif caught_count > 0:
        #     caught_message = "You were caught!\nNow you have to work at " \
        #         "Facebook :(\n"
        #     text = caught_message + text + "Press any Key to Restart"
        #     score = FONT.render("Your Score: " + str(steve_run.points()), True, (0, 0, 0))
        #     scoreRect = score.get_rect()
        #     scoreRect.center = (SteveRun.SCREEN_WIDTH // 2, SteveRun.SCREEN_HEIGHT // 2 + 50)
        #     SteveRun.SCREEN.blit(score, scoreRect)

        # text = FONT.render(text, True, (0, 0, 0))

        # textRect = text.get_rect()
        # textRect.center = (SteveRun.SCREEN_WIDTH // 2, SteveRun.SCREEN_HEIGHT // 2)
        # SteveRun.SCREEN.blit(text, textRect)
        # SteveRun.SCREEN.blit(SteveRun.RUNNING_IMAGE[0], (SteveRun.SCREEN_WIDTH // 2 - 20, SteveRun.SCREEN_HEIGHT // 2 - 140))
        # pygame.display.update()
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False
        #     if event.type == pygame.KEYDOWN:
        #         main()

steve_run_2 = SteveRun()
menu(caught_count=0, steve_run=steve_run_2)
