import pygame
from SuprosGame.scenes import Scene
from SuprosGame.ui import Button

class LoadGameScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.back_button = Button('Back', (50, 50), self.game.change_scene, args=('title',))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            # handle keydown event
            pass
