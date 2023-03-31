import pygame
from SuprosGame.scenes.title_scene import TitleScene
from SuprosGame.scenes.menu_scene import MenuScene
from constants import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Supros")
        self.clock = pygame.time.Clock()
        self.scene = TitleScene(self.screen)
        self.running = True

    def game_loop(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.scene.handle_events(events)
            self.scene.update()

            if self.scene.next_scene == "menu":
                self.scene = MenuScene(self.screen)

            self.screen.blit(self.scene.background.image, self.scene.background.rect)
            self.scene.render_ui()
            pygame.display.update()
            self.clock.tick(FPS)

    def quit(self):
        pygame.quit()
        sys.exit()

    def run(self):
        clock = pygame.time.Clock()
        while not self.quit:
            dt = clock.tick(self.fps) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
            self.scene.handle_events(event)
            self.scene.update(dt)
            self.scene.render(self.screen)
            pygame.display.update()

