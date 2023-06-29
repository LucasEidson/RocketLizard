import pygame
from settings import *
from Sprites import Player, Tile, Enemy, Flag
from levelEditor import Level

class Game:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font("Graphics/square-deal.ttf", 32)
        self.restart = self.font.render('Left Click to Play Level, Right Click to Enter Level Editor', False, (255, 20, 20))
        self.restart_rect = self.restart.get_rect(center=pygame.math.Vector2(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT * 2/3))
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
        self.flags = pygame.sprite.Group()
        #level map:
        self.level = Level()
        map = self.level.screenMap
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
                elif map[j][i] == 3:
                    flag = Flag([i * TILE_WIDTH + (TILE_WIDTH / 2), j * TILE_HEIGHT])
                    self.flags.add(flag)
                #elif map[j][i] == -1:
                    #self.player = Player([i * TILE_WIDTH + (TILE_WIDTH / 2), (j * TILE_HEIGHT - PLAYER_HEIGHT)])
        #Create Rocket_Group (only one rocket at a time)
        self.rocket_group = pygame.sprite.GroupSingle() 

    def scroll(self, screen_scroll):
        for sprite in self.tiles:
            sprite.rect.x += screen_scroll
        for sprite in self.enemies:
            sprite.rect.x += screen_scroll
        for sprite in self.rocket_group:
            sprite.rect.x += screen_scroll
        for sprite in self.flags:
            sprite.rect.x += screen_scroll


    def run(self, dt):
        playerStatus = self.player.collisions(self.enemies, self.flags)
        enterEditor = False
        if playerStatus == 1:
            #logic
            screen_scroll = self.player.movement(dt, self.tiles)
            self.scroll(screen_scroll)
            self.player.shoot(dt, self.rocket_group, self.can_collide)
            for sprite in self.enemies.sprites():
                sprite.strafe(dt, self.can_collide)
            #display everything
            self.display_surface.fill([201, 251, 201])
            self.tiles.draw(self.display_surface)
            self.flags.draw(self.display_surface)
            self.enemies.draw(self.display_surface)
            self.rocket_group.draw(self.display_surface)
            self.player_group.draw(self.display_surface)
        else:
            #get rid of all sprites
            self.display_surface.fill([201, 251, 201])
            for sprite in self.tiles:
                sprite.kill()
            for sprite in self.enemies:
                sprite.kill()
            for sprite in self.rocket_group:
                sprite.kill()
            for sprite in self.player_group:
                sprite.kill()
            #display message
            if playerStatus == 0:
                self.message = self.font.render('You Died!', False, (255, 20, 20))
                self.message_rect = self.message.get_rect(center=pygame.math.Vector2(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2))
            else:
                self.message = self.font.render('You Won!', False, (20, 255, 20))
                self.message_rect = self.message.get_rect(center=pygame.math.Vector2(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2))
            self.display_surface.blit(self.message, self.message_rect)
            self.display_surface.blit(self.restart, self.restart_rect)
            if pygame.mouse.get_pressed()[0]:
                self.spawn_sprites()
            elif pygame.mouse.get_pressed()[2]:
                enterEditor = True
        pygame.display.update()
        return enterEditor