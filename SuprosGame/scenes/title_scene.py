from SuprosGame.scenes.scene import Scene
from SuprosGame.ui.button import Button
from SuprosGame.ui.label import Label

class TitleScene(Scene):
    def __init__(self):
        super().__init__()

        self.title_label = Label("Welcome to Supros", 64, (255, 255, 255), self.window_width // 2, self.window_height // 3)

        self.start_button = Button("Start", (self.window_width // 2, self.window_height // 2), self.on_start_clicked)
        self.quit_button = Button("Quit", (self.window_width // 2, self.window_height * 2 // 3), self.on_quit_clicked)

        self.add_ui_element(self.title_label)
        self.add_ui_element(self.start_button)
        self.add_ui_element(self.quit_button)

    def on_start_clicked(self):
        pass

    def on_quit_clicked(self):
        self.quit_game()
