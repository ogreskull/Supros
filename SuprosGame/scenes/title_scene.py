import pygame

from SuprosGame.scenes import Scene
from SuprosGame.scenes.menu_scene import MenuScene
from SuprosGame.ui import Label


class TitleScene(Scene):
    def __init__(self):
        super().__init__()

        self.title_label = Label("Press any key to start", 48)
        self.title_label.center()
        self.add_ui_element(self.title_label)

    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.switch_to_scene(MenuScene())
