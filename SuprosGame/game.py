import pygame
from SuprosGame.scenes.title_scene import TitleScene
from SuprosGame.scenes.menu_scene import MenuScene


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Supros")

        self.clock = pygame.time.Clock()

        self.scene = TitleScene(self.screen)
        self.scene.add_scene("menu", MenuScene(self.screen))

    def run(self):
        running = True

        while running:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    running = False

            self.scene.handle_events(events)
            self.scene.update()
            self.scene.render(self.screen)

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()