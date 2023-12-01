from settings import *
from utilities import *
import pygame

class TitleScreen:

    def __init__(self, game):
        self.game = game
        self.title_font = Font(PRIMARY_FONT, 80)
        self.subtitle_font = Font(SECONDARY_FONT, 64)
        self.default_font = Font(SECONDARY_FONT, 32)
        self.bigboner_font = Font(BONER_FONT, 80)
        self.medboner_font = Font(BONER_FONT, 64)
        self.smboner_font = Font(BONER_FONT, 32)
        self.color = (0, 0, 0)
        
    def update(self):
        pass

    def draw(self, surface):
        self.game.screen.fill(self.color)
        text = self.bigboner_font.render("low morale", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.bottom = HEIGHT // 2 - 8
        surface.blit(text, rect)
    
        text = self.smboner_font.render("press space to start", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2 + 8
        surface.blit(text, rect)


class WinScreen:

    def __init__(self, game):
        self.game = game

        self.game = game
        self.title_font = Font(PRIMARY_FONT, 80)
        self.subtitle_font = Font(SECONDARY_FONT, 64)
        self.default_font = Font(SECONDARY_FONT, 32)
        self.bigboner_font = Font(BONER_FONT, 80)
        self.medboner_font = Font(BONER_FONT, 64)
        self.smboner_font = Font(BONER_FONT, 32)
        self.color = (0, 0, 0)
        
    def update(self):
        pass

    def draw(self, surface):
        self.game.screen.fill(self.color)
        text = self.medboner_font.render("bliss", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.bottom = HEIGHT // 2 - 8
        surface.blit(text, rect)
    
        text = self.smboner_font.render("press r to find a new babe", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2 + 8
        surface.blit(text, rect)


class LoseScreen:

    def __init__(self, game):
        self.game = game

        self.game = game
        self.title_font = Font(PRIMARY_FONT, 80)
        self.subtitle_font = Font(SECONDARY_FONT, 64)
        self.default_font = Font(SECONDARY_FONT, 32)
        self.bigboner_font = Font(BONER_FONT, 80)
        self.medboner_font = Font(BONER_FONT, 64)
        self.smboner_font = Font(BONER_FONT, 32)
        self.color = (0, 0, 0)
        
    def update(self):
        pass

    def draw(self, surface):
        text = self.subtitle_font.render("You lose!", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.bottom = HEIGHT // 2 - 8
        surface.blit(text, rect)
    
        text = self.default_font.render("Press 'r' to play again.", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2 + 8
        surface.blit(text, rect)


class LevelCompleteScreen:

    def __init__(self, game):
        self.game = game
        self.title_font = Font(PRIMARY_FONT, 80)
        self.subtitle_font = Font(SECONDARY_FONT, 64)
        self.default_font = Font(SECONDARY_FONT, 32)
        self.bigboner_font = Font(BONER_FONT, 80)
        self.medboner_font = Font(BONER_FONT, 64)
        self.smboner_font = Font(BONER_FONT, 32)
        self.color = (0, 0, 0)
        
    def update(self):
        pass

    def draw(self, surface):
        text = self.subtitle_font.render("Level Complete!", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.bottom = HEIGHT // 2 - 8
        surface.blit(text, rect)


class PauseScreen:

    def __init__(self, game):
        self.game = game
        self.title_font = Font(PRIMARY_FONT, 80)
        self.subtitle_font = Font(SECONDARY_FONT, 64)
        self.default_font = Font(SECONDARY_FONT, 32)
        self.bigboner_font = Font(BONER_FONT, 80)
        self.medboner_font = Font(BONER_FONT, 64)
        self.smboner_font = Font(BONER_FONT, 32)
        self.color = (0, 0, 0)
        
    def update(self):
        pass

    def draw(self, surface):
        text = self.medboner_font.render("paused", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.bottom = HEIGHT // 2 - 8
        surface.blit(text, rect)
    
        text = self.smboner_font.render("press p to continue", True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2 + 8
        surface.blit(text, rect)


class HUD:

    def __init__(self, game):
        self.game = game
        self.title_font = Font(PRIMARY_FONT, 80)
        self.subtitle_font = Font(SECONDARY_FONT, 64)
        self.default_font = Font(SECONDARY_FONT, 32)
        self.bigboner_font = Font(BONER_FONT, 80)
        self.medboner_font = Font(BONER_FONT, 64)
        self.smboner_font = Font(BONER_FONT, 32)
        self.color = (0, 0, 0)
        
    def update(self):
        pass

    def draw(self, surface):
        text = self.subtitle_font.render('Altitude: ' + str(self.game.hero.rect.bottom * -1 + 512), True, WHITE)
        rect = text.get_rect()
        rect.top = 16
        rect.left = 16
        surface.blit(text, rect)

        text = self.subtitle_font.render('Ammo: ' + str(self.game.hero.ammo), True, WHITE)
        rect = text.get_rect()
        rect.top = 64
        rect.left = 16
        surface.blit(text, rect)

# Used for level editing
class Grid:

    def __init__(self, game, color=(0, 0, 0)):
        self.game = game
        self.on = False

        self.color = color
        self.font = Font(None, 16)

    def toggle(self):
        self.on = not self.on

    def draw(self, surface, offset_x=0, offset_y=0):
        if self.on:
            width = surface.get_width()
            height = surface.get_height()
            
            for x in range(0, width + GRID_SIZE, GRID_SIZE):
                adj_x = x - offset_x % GRID_SIZE
                pygame.draw.line(surface, self.color, [adj_x, 0], [adj_x, height], 1)

            for y in range(0, height + GRID_SIZE, GRID_SIZE):
                adj_y = y - offset_y % GRID_SIZE
                pygame.draw.line(surface, self.color, [0, adj_y], [width, adj_y], 1)

            for x in range(0, width + GRID_SIZE, GRID_SIZE):
                for y in range(0, height + GRID_SIZE, GRID_SIZE):
                    adj_x = x - offset_x % GRID_SIZE + 4
                    adj_y = y - offset_y % GRID_SIZE + 4
                    disp_x = x // GRID_SIZE + offset_x // GRID_SIZE
                    disp_y = y // GRID_SIZE + offset_y // GRID_SIZE
                    
                    point = f'({disp_x}, {disp_y})'
                    text = self.font.render(point, True, self.color)
                    surface.blit(text, [adj_x, adj_y])
