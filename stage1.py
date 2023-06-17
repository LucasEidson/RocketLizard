import pygame
import settings
from tiles import Tile

class Stage1:
    def __init__(self):
        self.display_surface = pygame.display.set_mode([settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT])
        self.draw_tiles()
    
    def draw_tiles(self):
        self.tiles = pygame.sprite.Group()
        tile = Tile([0, settings.DISPLAY_HEIGHT - settings.TILE_HEIGHT])
        self.tiles.add(tile)

    def run(self):
        self.tiles.draw(self.display_surface)
        pygame.display.update()