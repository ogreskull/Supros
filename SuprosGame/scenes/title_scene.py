from .scenes import Scene
from SuprosGame.ui import Button, Label

class TitleScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)

        title_label = Label("Supros", 72)
        title_label.center()
        title_label.y = 100
        self.add_ui_element(title_label)

        play_button = Button("Play", 36)
        play_button.center()
        play_button.y = 300
        play_button.on_click = self.play_game
        self.add_ui_element(play_button)

    def play_game(self):
        self.switch_to_scene(GameScene())

        quit_button = Button("Quit", 24)
        quit_button.center()
        quit_button.y += 320
        self.add_ui_element(quit_button)
