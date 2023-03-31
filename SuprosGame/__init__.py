import pygame
import sys
from SuprosGame.scenes import TitleScene, NewGameScene, LoadGameScene, OptionsScene

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.scenes = {
            'title': TitleScene(self),
            'new_game': NewGameScene(self),
            'load_game': LoadGameScene(self),
            'options': OptionsScene(self)
        }
        self.current_scene = 'title'
        self.quit = False

    def run(self):
        while not self.quit:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                else:
                    self.scenes[self.current_scene].handle_event(event)
            self.scenes[self.current_scene].update()
            self.scenes[self.current_scene].draw(self.screen)
            pygame.display.flip()

    def change_scene(self, scene_name):
        self.current_scene = scene_name