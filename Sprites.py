import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        #Player image and rect
        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill('green')
        self.direction = pygame.math.Vector2(0, 0)
        #jumping variables
        self.ySpeed = JUMP_HEIGHT
        self.in_air = False
        #shooting cooldown
        self.dShoot = 0
        self.shooting = False
        self.rocket_direction = 0
    
    
    def movement(self, dt, tiles):
        #get input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.direction.x = 1
        elif keys[pygame.K_d]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        #change x pos and check for collision
        self.rect.x -= self.direction.x * PLAYERSPEED * dt
        self.xCollision(tiles)

        #jumping and gravity
        if keys[pygame.K_SPACE] and not self.in_air:
            self.direction.y = -1 #moving up
            self.in_air = True
        if self.in_air:
            self.direction.y += GRAVITY
        #change y pos and check for collision
        self.rect.y += self.direction.y * self.ySpeed * dt
        self.yCollision(tiles)
            

    #collision is weird if x and y are done in same function
    def xCollision(self, tiles):
        for sprite in tiles:
            if sprite.rect.colliderect(self.rect):
                #x
                if self.direction.x > 0: #moving left
                    self.rect.left = sprite.rect.right
                elif self.direction.x < 0: #moving left
                    self.rect.right = sprite.rect.left

        
    def yCollision(self, tiles):
        on_floor = False
        for sprite in tiles:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0: #moving down
                    self.rect.bottom = sprite.rect.top
                    self.ySpeed = JUMP_HEIGHT
                    self.direction.y = 0
                    on_floor = True
                else: #moving up
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
            self.in_air = not on_floor

    def shoot(self, dt, rocket_group, tiles):
        time = pygame.time.get_ticks()
        if pygame.mouse.get_pressed()[0] and time - self.dShoot > 2000:
            self.rocket_direction = -self.direction.x
            if self.rocket_direction == 0:
                self.rocket_direction = 1
            self.rocket = Rocket([self.rect.x, self.rect.y])
            self.rocket.add(rocket_group)
            self.dShoot = time
            self.shooting = True
        if self.shooting:
            if time - self.dShoot < 5000:
                self.rocket.move(self.rocket_direction, dt)
                self.shooting = self.rocket.collide(tiles)
            else:
                self.shooting = False
                self.rocket.kill()

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        #Tile image and rect
        self.image = pygame.Surface([TILE_WIDTH, TILE_HEIGHT])
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill([55, 25, 7])

class Rocket(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface([36, 12])
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill('red')
    
    def move(self, direction, dt):
        self.rect.x += 500 * direction * dt

    def collide(self, tiles):
        alive = True
        for sprite in tiles:
            if sprite.rect.colliderect(self.rect):
                self.kill()
                alive = False
        return alive