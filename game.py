import pygame
from settings import *
from Sprites import Player, Tile

class Game:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        
        self.spawn_sprites()

        #navigation
        self.origin = pygame.math.Vector2()

    #input
    def event_loop(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        
    def spawn_sprites(self):
        #player
        self.player_group = pygame.sprite.GroupSingle()
        self.player = Player([0, 0])
        self.player.add(self.player_group)
        #tiles
        self.tiles = pygame.sprite.Group()
        #Drawing level map:
        map =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #1
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2
              [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], #3
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], #4
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], #5
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], #6
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #7
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], #8
              [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #9
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #10
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], #11
              [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1]] #12
        #auto-draw map
        for j in range(len(map)):
            for i in range(len(map[j])):
                if map[j][i]:
                    tile = Tile([i * TILE_WIDTH, j * TILE_HEIGHT])
                    self.tiles.add(tile)
        #Create Rocket_Group (only one rocket at a time)
        self.rocket_group = pygame.sprite.GroupSingle()

    def run(self, dt):
        #logic
        self.player.movement(dt, self.tiles)
        self.player.shoot(dt, self.rocket_group, self.tiles)

        #draw
        self.display_surface.fill([201, 251, 201])
        self.tiles.draw(self.display_surface)
        self.rocket_group.draw(self.display_surface)
        self.player_group.draw(self.display_surface)
        pygame.display.update()