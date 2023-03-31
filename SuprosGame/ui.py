import pygame

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)


class UIElement:
    """
    A class to represent a UI element.
    """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb):
        """
        Initialize the UIElement.

        :param center_position: tuple (x, y)
            The position of the center of the element.
        :param text: str
            The text to be displayed.
        :param font_size: int
            The font size of the text.
        :param bg_rgb: tuple (R, G, B)
            The background color of the element.
        :param text_rgb: tuple (R, G, B)
            The text color of the element.
        """
        self.center_position = center_position
        self.text = text
        self.font_size = font_size
        self.bg_rgb = bg_rgb
        self.text_rgb = text_rgb

        # create the font object
        self.font = pygame.font.SysFont(None, self.font_size)

        # create the rect object for the background surface
        self.background_surface = pygame.Surface((0, 0))
        self._update()

    def _update(self):
        """
        Update the background surface.
        """
        # get the size of the text surface
        text_surface = self.font.render(self.text, True, self.text_rgb)
        size = (text_surface.get_width() + 20, text_surface.get_height() + 20)
        self.background_surface = pygame.Surface(size)

        # fill the background surface with the background color
        self.background_surface.fill(self.bg_rgb)

        # draw the text surface onto the background surface
        text_x = (self.background_surface.get_width() - text_surface.get_width()) / 2
        text_y = (self.background_surface.get_height() - text_surface.get_height()) / 2
        self.background_surface.blit(text_surface, (text_x, text_y))

    def render(self, surface):
        """
        Render the element onto a surface.

        :param surface: pygame.Surface
            The surface to render the element onto.
        """
        # update the background surface
        self._update()

        # blit the background surface onto the provided surface
        rect = self.background_surface.get_rect(center=self.center_position)
        surface.blit(self.background_surface, rect)


class TextButton(UIElement):
    """
    A class to represent a text button.
    """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        """
        Initialize the TextButton.

        :param center_position: tuple (x, y)
            The position of the center of the element.
        :param text: str
            The text to be displayed.
        :param font_size: int
            The font size of the text.
        :param bg_rgb: tuple (R, G, B)
            The background color of the element.
        :param text_rgb: tuple (R, G, B)
            The text color of the element.
        :param action: callable
            The function to be called when the button is clicked.
        """
        super().__init__(center_position, text, font_size, bg_rgb, text_rgb)
        self.action = action

    def clicked(self):
        """Calls the attached function when the button is clicked."""
        if self.action is not None:
            self.action()

