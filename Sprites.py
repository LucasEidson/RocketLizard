import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        #Player image and rect
        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill("green")
        self.ySpeed = JUMP_HEIGHT
    
    
    def movement(self, dt, jumping):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= PLAYERSPEED * dt
        if keys[pygame.K_d]:
            self.rect.x += PLAYERSPEED * dt
        #jumping and gravity
        if keys[pygame.K_SPACE]:
            jumping = True
            self.ySpeed = JUMP_HEIGHT
        if jumping:
            self.rect.y -= self.ySpeed * dt
            self.ySpeed -= GRAVITY 
        return(jumping)

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        #Tile image and rect
        self.image = pygame.Surface([TILE_WIDTH, TILE_HEIGHT])
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill([55, 25, 7])