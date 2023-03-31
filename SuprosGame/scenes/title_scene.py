from typing import List, Tuple
import pygame

from scenes import Scene

class TitleScene(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

    def process_input(self, events: List[pygame.event.Event]):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.switch_to_scene("gameplay")

    def update(self, dt: float):
        pass

    def render(self):
        self.screen.fill((255, 255, 255))
        font = pygame.font.SysFont(None, 48)
        text = font.render("Title Scene", True, (0, 0, 0))
        rect = text.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(text, rect)
