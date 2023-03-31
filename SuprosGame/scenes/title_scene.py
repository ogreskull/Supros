import pygame
from SuprosGame.scenes import Scene
from SuprosGame.ui import Button

class TitleScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.new_game_button = Button('New Game', (200, 200), self.game.change_scene, args=('new_game',))
        self.load_game_button = Button('Load Game', (200, 250), self.game.change_scene, args=('load_game',))
        self.options_button = Button('Options', (200, 300), self.game.change_scene, args=('options',))
        self.quit_button = Button('Quit', (200, 350), sys.exit)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
        self.new_game_button.handle_event(event)
        self.load_game_button.handle_event(event)
        self.options_button.handle_event(event)
        self.quit_button.handle_event(event)

    def update(self):
        pass

    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.new_game_button.draw(surface)
        self.load_game_button.draw(surface)
        self.options_button.draw(surface)
        self.quit_button.draw(surface)