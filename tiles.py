#Stage1 map: 
#                      XXXXXX            e                            <|
#                      XXXXXX          XXXXX                           |
#                      XXXXXX                       XX                 | 
#                      XXXXXX          e                               |
#                        XX      XXXXXXXXXXXXXXXXX   X   X   X   XXXXXXX
#                               XXXX              /\/\/\/\/\/\/\/
#             XXXXXXXX    e   XXXXXX
#XXXXXXXXXXX /\/\/\ XXXXXXXXXXXXXXXX
import pygame
import settings
import player

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface([settings.TILE_WIDTH, settings.TILE_HEIGHT])
        self.image.fill("black")
        self.rect = self.image.get_rect(topleft=pos)
    