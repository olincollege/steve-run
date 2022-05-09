'''
View for the Steve character.
'''

class SteveView:
    '''
    The View for the Steve character within the current instance of the Steve
    Run game.

    Attributes:
        steve_run: an instance of SteveRun, representing the current game of
            Steve Run being played.
        steve_controller: an instance of the SteveController class.
    '''
    def __init__(self, steve_run, steve_controller):
        '''
        Args:
            steve_run: an instance of SteveRun, representing the current game of
                Steve Run being played.
            steve_controller: an instance of the SteveController class.
        '''
        self._steve_run = steve_run
        self._steve_controller = steve_controller

    def draw(self, screen):
        '''
        Display the Steve character in its current form.
        '''
        screen.blit(self._steve_run.image(), (self._steve_controller.steve_rect.x,
                                 self._steve_controller.steve_rect.y))
