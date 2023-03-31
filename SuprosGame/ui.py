import pygame


class Button:
    def __init__(self, x, y, width, height, color, text='', font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text_surface, self.text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return True


class Label:
    def __init__(self, text='', font_size=30, x=0, y=0):
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(x=x, y=y)

    def center(self):
        self.text_rect.center = pygame.display.get_surface().get_rect().center

    def draw(self, surface):
        surface.blit(self.text_surface, self.text_rect)

    def set_text(self, text):
        self.text = text
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(x=self.text_rect.x, y=self.text_rect.y)
