import pygame
import random

from background_controller import BackgroundController
from steve_controller import SteveController
from background_view import BackgroundView
from steve_view import SteveView
from obstacle_view import SmallMarkView, LargeMarkView, HelicopterView
from steve_run import SteveRun
# from menu_controller import menu


def main():
    run = True

    ## stuff below here is what I am definig, p sure its right
    steve_run = SteveRun()    # create an instance of the SteveRun class
    _steve_controller = SteveController(steve_run)
    _background_controller = BackgroundController(steve_run)
    _steve_view = SteveView(steve_run, _steve_controller)
    _background_view = BackgroundView(steve_run)
    # _obstacles_view = ObstacleView()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SteveRun.SCREEN.fill((255, 255, 255))
        user_input = pygame.key.get_pressed()

        steve_run.background()
        _background_view.draw(SteveRun.SCREEN)
        _background_controller.update()

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
                print("Flying Obstacle Image")

        for obstacle in steve_run.obstacles():
            obstacle.draw(SteveRun.SCREEN)
            obstacle.update()
            if _steve_controller.steve_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                steve_run.increase_death_count()
                menu(steve_run.death_count(), steve_run)

        steve_run.score()

        steve_run.clock.tick(30)
        pygame.display.update()


def menu(death_count, steve_run):
    run = True
    while run:
        SteveRun.SCREEN.fill((255, 255, 255))
        FONT = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = FONT.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = FONT.render("Press any Key to Restart", True, (0, 0, 0))
            score = FONT.render("Your Score: " + str(steve_run.points), True, (0, 0, 0))
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

steve_run_2 = SteveRun()
menu(death_count=0, steve_run=steve_run_2)