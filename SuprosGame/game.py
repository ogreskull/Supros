import pygame
from .scenes.title_scene import TitleScene


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Supros Game")

        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        self.scene = TitleScene(self.screen)

    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.screen.fill((255, 255, 255))
            self.scene.update(dt)
            self.scene.draw(self.screen)
            pygame.display.update()
