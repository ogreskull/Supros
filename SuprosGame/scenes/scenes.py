from typing import List, Tuple, Optional
import pygame

class Scene:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.next_scene: Optional[str] = None

    def process_input(self, events: List[pygame.event.Event]):
        raise NotImplementedError

    def update(self, dt: float):
        raise NotImplementedError

    def render(self, screen=None):
        if screen is None:
            screen = pygame.display.get_surface()

    def switch_to_scene(self, next_scene: str):
        self.next_scene = next_scene
