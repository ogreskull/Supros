import pygame
from pygame.locals import *
from scene import Scene
from button import Button

class NewGameScene(Scene):
    def __init__(self, game):
        super().__init__(game)

        self.title_font = pygame.font.Font('fonts/Pixeltype.ttf', 64)
        self.subtitle_font = pygame.font.Font('fonts/Pixeltype.ttf', 32)
        self.input_font = pygame.font.Font('fonts/Pixeltype.ttf', 24)
        self.button_font = pygame.font.Font('fonts/Pixeltype.ttf', 24)

        self.title_text = self.title_font.render('New Game', True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(self.game.width/2, self.game.height/4))

        self.name_input_text = self.subtitle_font.render('Enter your name:', True, (255, 255, 255))
        self.name_input_rect = self.name_input_text.get_rect(midleft=(self.game.width/4, self.game.height/2))

        self.name_input_box = pygame.Rect(self.game.width/4, self.game.height/2 + 10, self.game.width/2, 30)
        self.name_input = ''

        self.start_button = Button(
            self.game.width/2,
            self.game.height - 100,
            150,
            50,
            'Start',
            self.button_font,
            self.game,
            self.start_game
        )

        self.back_button = Button(
            self.game.width/2,
            self.game.height - 50,
            150,
            50,
            'Back',
            self.button_font,
            self.game,
            self.go_to_title
        )

    def start_game(self):
        self.game.player.name = self.name_input
        self.game.save_game()
        self.game.start_game()

    def go_to_title(self):
        self.game.change_scene('title')

    def handle_events(self, events):
        for event in events:
            if event.type == QUIT:
                self.game.quit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    self.name_input = self.name_input[:-1]
                else:
                    self.name_input += event.unicode
            elif event.type == MOUSEBUTTONDOWN:
                self.start_button.handle_click(event.pos)
                self.back_button.handle_click(event.pos)

    def update(self):
        pass

    def render(self, surface):
        surface.fill((0, 0, 0))

        surface.blit(self.title_text, self.title_rect)

        surface.blit(self.name_input_text, self.name_input_rect)

        pygame.draw.rect(surface, (255, 255, 255), self.name_input_box, 2)

        name_surface = self.input_font.render(self.name_input, True, (255, 255, 255))
        surface.blit(name_surface, (self.name_input_box.x + 5, self.name_input_box.y + 5))

        self.start_button.render(surface)
        self.back_button.render(surface)
