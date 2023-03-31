import pygame
from SuprosGame.scenes.title_scene import TitleScene

pygame.init()

class SuprosGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.current_scene = TitleScene(self)

    def change_scene(self, scene_name):
        if scene_name == 'title':
            self.current_scene = TitleScene(self)

    def run(self):
        while True:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                self.current_scene.handle_event(event)

            self.current_scene.update()
            self.current_scene.render(self.screen)

            pygame.display.flip()
