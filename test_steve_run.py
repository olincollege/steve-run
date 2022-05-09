import pygame


# time advances by the game, not real life
# points are added correctly
# oressing the key is corect


# for main and steve_controller
def create_key_mock(pressed_key):
    def helper():
        tmp = [0] * 300
        tmp[pressed_key] = 1
        return tmp
    return helper

pygame.key.get_pressed = create_key_mock(K_LEFT)
