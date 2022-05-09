'''
Tester functions for Steve Run, using pytest.
'''

import pytest
import pygame
from steve_controller import SteveController
from steve_run import SteveRun

pygame.init()

def test__intial_score():
    '''
    Test if the game begins at a score of 0
    '''
    steve_run = SteveRun()
    assert steve_run.points() == 0

def test_score_update():
    '''
    Test if the game increases score by 1 when called.
    '''
    steve_run = SteveRun()
    steve_run.score()
    assert steve_run.points() == 1

def test_game_speed_start():
    '''
    Test if the game speed begins at 20
    '''
    steve_run = SteveRun()
    assert steve_run.game_speed() == 20

def test_game_speed_increase_1():
    '''
    Test if the game speed increases every 100 points
    '''
    steve_run = SteveRun()
    steve_run.increase_points(99)
    steve_run.score()
    print(steve_run.points())
    assert steve_run.game_speed() == 21

def test_game_speed_increase_2():
    '''
    Test if the game speed increases twice when at 200 points
    '''
    steve_run = SteveRun()
    steve_run.increase_points(99)
    steve_run.score()
    steve_run.increase_points(99)
    steve_run.score()
    print(steve_run.points())
    assert steve_run.game_speed() == 22


steve_images = [
    ("crouch", "crouch_image", True),
    ("crouch", "run_image", False),
    ("crouch", "jump_image", False),
    ("run", "crouch_image", False),
    ("run", "run_image", True),
    ("run", "jump_image", False),
    ("jump", "crouch_image", False),
    ("jump", "run_image", False),
    ("jump", "jump_image", True)
]

@pytest.mark.parametrize("state, image, expected_comparison", steve_images)
def test_steve_image_change(state, image, expected_comparison):
    '''
    Test that the character image changes when the attributes change.
    '''
    steve_run = SteveRun()
    steve_controller = SteveController(steve_run)

    if state == "crouch":
        steve_controller.crouch()
    if state == "run":
        steve_controller.run()
    if state == "jump":
        steve_controller.jump()

    if image == "crouch_image":
        compare_image = steve_run.CROUCHING_IMAGE
        comparison = (steve_run.image() == compare_image[0]) or \
            (steve_run.image() == compare_image[1])
    if image == "run_image":
        image_to_compare = steve_run.RUNNING_IMAGE
        comparison = (steve_run.image() == image_to_compare[0]) or \
            (steve_run.image() == image_to_compare[1])
    if image == "jump_image":
        image_to_compare = steve_run.JUMPING_IMAGE
        comparison = steve_run.image() == image_to_compare

    assert expected_comparison == comparison
