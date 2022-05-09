# reads in data from the model and displays it

class SteveView:
    def __init__(self, steve_run, steve_controller):
        self._steve_run = steve_run
        self._steve_controller = steve_controller

    def draw(self, screen):
        print(self._steve_run.image())
        screen.blit(self._steve_run.image(), (self._steve_controller.steve_rect.x,
                                 self._steve_controller.steve_rect.y))
