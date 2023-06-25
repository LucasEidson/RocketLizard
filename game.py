import pygame
from settings import *
from Sprites import Player, Tile, Enemy
from level import level1

class Game:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        
        self.spawn_sprites()

    #input
    def event_loop(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        
    def spawn_sprites(self):
        #player
        self.player_group = pygame.sprite.GroupSingle()
        self.player = Player([DISPLAY_WIDTH / 2, DISPLAY_HEIGHT - TILE_HEIGHT * 2])
        self.player.add(self.player_group)
        #tiles and enemies
        self.can_collide = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        #level map:
        map = level1
        #auto-draw enemies and tiles
        for j in range(len(map)):
            for i in range(len(map[j])):
                if map[j][i] == 1:
                    tile = Tile([i * TILE_WIDTH, j * TILE_HEIGHT])
                    self.tiles.add(tile)
                    self.can_collide.add(tile)
                elif map[j][i] == 2:
                    enemy = Enemy([i * TILE_WIDTH - (ENEMY_WIDTH - TILE_WIDTH), j * TILE_HEIGHT - (ENEMY_HEIGHT - TILE_HEIGHT)])
                    self.enemies.add(enemy)
                    self.can_collide.add(enemy)
        #Create Rocket_Group (only one rocket at a time)
        self.rocket_group = pygame.sprite.GroupSingle()

    def scroll(self, screen_scroll):
        for sprite in self.tiles:
            sprite.rect.x += screen_scroll
        for sprite in self.enemies:
            sprite.rect.x += screen_scroll

    def run(self, dt):
        #logic
        screen_scroll = self.player.movement(dt, self.tiles)
        self.scroll(screen_scroll)
        self.player.shoot(dt, self.rocket_group, self.can_collide)
        for sprite in self.enemies.sprites():
            sprite.strafe(dt, self.can_collide)

        #draw
        self.display_surface.fill([201, 251, 201])
        self.tiles.draw(self.display_surface)
        self.enemies.draw(self.display_surface)
        self.rocket_group.draw(self.display_surface)
        self.player_group.draw(self.display_surface)
        pygame.display.update()