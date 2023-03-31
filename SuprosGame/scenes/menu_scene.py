from scenes import Scene
from ui import Button, Label


class MenuScene(Scene):
    def __init__(self):
        super().__init__()

        title_label = Label("Menu", 48)
        title_label.center()
        self.add_ui_element(title_label)

        play_button = Button("Play", 24)
        play_button.center()
        play_button.y += 80
        self.add_ui_element(play_button)

        options_button = Button("Options", 24)
        options_button.center()
        options_button.y += 160
        self.add_ui_element(options_button)

        quit_button = Button("Quit", 24)
        quit_button.center()
        quit_button.y += 240
        self.add_ui_element(quit_button)

    def handle_input(self, input_event):
        if input_event.type == "KEYDOWN" or input_event.type == "MOUSEBUTTONDOWN":
            if input_event.key == "ESCAPE":
                self.quit_game()
            else:
                self.change_scene("play")
