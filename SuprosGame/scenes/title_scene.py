from .scenes import Scene
from SuprosGame.ui import Button, Label

class TitleScene(Scene):
    def __init__(self):
        super().__init__()

        title_label = Label("Welcome to SuprosGame!", 48)
        title_label.center()
        self.add_ui_element(title_label)

        new_game_button = Button("New Game", 24)
        new_game_button.center()
        new_game_button.y += 80
        self.add_ui_element(new_game_button)

        load_game_button = Button("Load Game", 24)
        load_game_button.center()
        load_game_button.y += 160
        self.add_ui_element(load_game_button)

        options_button = Button("Options", 24)
        options_button.center()
        options_button.y += 240
        self.add_ui_element(options_button)

        quit_button = Button("Quit", 24)
        quit_button.center()
        quit_button.y += 320
        self.add_ui_element(quit_button)
