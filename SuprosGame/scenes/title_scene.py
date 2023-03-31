import pygame
from scenes import Scene
from SuprosGame.ui import Label


class TitleScene(Scene):
    def __init__(self, screen):
        self.ui_elements = []
        super().__init__(screen)
        self.background = pygame.image.load('..\\SuprosAssets\\images\\backgrounds\\title_screen.png')
        press_start_label = Label(100, 100, "Press any key to start", 24)
        press_start_label.center()
        press_start_label.y = self.screen.get_rect().centery
        self.add_ui_element(press_start_label)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.next_scene = "menu"

    def update(self):
        pass

    def add_ui_element(self, element):
        self.ui_elements.append(element)