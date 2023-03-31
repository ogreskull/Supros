from .scenes import Scene
from SuprosGame.ui import Button, Label


class OptionsScene(Scene):
    def __init__(self):
        super().__init__()

        title_label = Label("Options", 48)
        title_label.center()
        self.add_ui_element(title_label)

        sound_button = Button("Sound", 24)
        sound_button.center()
        sound_button.y += 80
        self.add_ui_element(sound_button)

        controls_button = Button("Controls", 24)
        controls_button.center()
        controls_button.y += 160
        self.add_ui_element(controls_button)

        back_button = Button("Back", 24)
        back_button.center()
        back_button.y += 320
        self.add_ui_element(back_button)
