'''
View for the Steve character.
'''

from abc import ABC, abstractmethod


class CharacterView(ABC):
    """
    Abstract base class representing a view of a game of Steve Run.

    Attributes:
        steve_run: A SteveRun instance representing the Steve Run game to
            display.
    """

    def __init__(self, steve_run, steve_controller):
        """
        Create a new view of a Steve Run game.

        Args:
            steve_run: A SteveRun instance representing the Steve Run
                game to display.
        """
        self._steve_run = steve_run
        self._steve_controller = steve_controller

    @property
    def steve_run(self):
        """
        Return the SteveRun instance being represented by this view.
        """
        return self._steve_run

    @abstractmethod
    def draw(self, screen):
        """
        Display a representation of the current state of Steve Run.
        """


class SteveView(CharacterView):
    '''
    The View for the Steve character within the current instance of the Steve
    Run game.

    Attributes:
        steve_run: an instance of SteveRun, representing the current game of
            Steve Run being played.
        steve_controller: an instance of the SteveController class.
    '''
    def draw(self, screen):
        '''
        Display the Steve character in its current form.
        '''
        screen.blit(self._steve_run.image(),
                    (self._steve_controller.steve_rect.x,
                    self._steve_controller.steve_rect.y))
