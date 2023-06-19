import pygame
from settings import *
from Sprites import Player, Tile

class Game:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.sprites()

        self.jumping = False
        
        #navigation
        self.origin = pygame.math.Vector2()

    #input
    def event_loop(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
    #spawn sprites
    def sprites(self):
        #player
        self.player_group = pygame.sprite.GroupSingle()
        self.player = Player([DISPLAY_WIDTH / 2, DISPLAY_HEIGHT - 110])
        self.player.add(self.player_group)
        
        #tiles
        self.tiles = pygame.sprite.Group()
        #Drawing level map:
        map =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #1
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2
              [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], #3
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #4
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], #5
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #6
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #7
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #8
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], #9
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #10
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #11
              [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1]]#12
        #auto-draw map
        for j in range(len(map)):
            for i in range(len(map[j])):
                if map[j][i]:
                    tile = Tile([i * TILE_WIDTH, j * TILE_HEIGHT])
                    self.tiles.add(tile)
    #for jumping onto tiles
    def collisions(self):
        if pygame.sprite.spritecollide(self.player, self.tiles, False):
            jumping = False
        else:
            jumping = True
        return jumping
    
    def run(self, dt):
        #logic

        self.player.movement(dt, self.collisions())
        
        #draw
        self.display_surface.fill([201, 251, 201])
        self.player_group.draw(self.display_surface)
        self.tiles.draw(self.display_surface)
        pygame.display.update()