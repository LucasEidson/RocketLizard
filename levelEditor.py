import random
import pygame
from Sprites import Player, Tile, Enemy, Flag, Button
from settings import *
#-1 = player, 0 = nothing, 1 = tile, 2 = enemy, 3 - flag

class Level():
    def __init__(self):
        #the screen is 12 tiles high, 16 tiles wide
        self.display_surface = pygame.display.get_surface()
        #create groups:
        self.tiles = pygame.sprite.Group()
        self.flags = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle()
        self.buttons = pygame.sprite.Group()

        tile = Tile(pygame.math.Vector2(100,100))
        self.tiles.add(tile)

        #grids and nav
        #origin is the left side of the screen
        self.origin = 0
        self.scroll = 0
        self.screenMap = [
            [0] * 19,
            [0] * 19,
            [0] * 19,
            [0] * 19,
            [0] * 19,
            [0] * 19,
            [0] * 19,
            [0] * 19,
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3] * 19,
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 0, 2, 1],
            [1] * 19
        ]
        self.HEIGHT = 12
        self.WIDTH = 16
    
    def draw_grid(self):
        cols = DISPLAY_WIDTH // TILE_WIDTH
        rows = DISPLAY_HEIGHT // TILE_HEIGHT
        for col in range(cols * 200):
            x = self.origin + col * TILE_WIDTH
            pygame.draw.line(self.display_surface, 'black', (x, 0), (x, DISPLAY_HEIGHT))
        #for row in range()

    def scroll_screen(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.origin += 400 * dt
        elif keys[pygame.K_d]:
            self.origin -= 400 * dt
        #scroll through sprites, lines are in draw_grid
        for sprite in self.tiles:
            sprite.rect.x += self.origin
        for sprite in self.flags:
            sprite.rect.x += self.origin
        for sprite in self.enemies:
            sprite.rect.x += self.origin
        for sprite in self.player_group:
            sprite.rect.x += self.origin
        
        
    def run(self, dt):
        self.display_surface.fill([201, 251, 201])
        self.draw_grid()
        self.scroll_screen(dt)
        self.buttons.draw(self.display_surface)
        self.tiles.draw(self.display_surface)
        self.flags.draw(self.display_surface)
        self.enemies.draw(self.display_surface)
        self.player_group.draw(self.display_surface)
        pygame.display.update()

