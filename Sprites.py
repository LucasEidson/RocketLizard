import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        #Player image and rect
        self.image = pygame.image.load("Graphics/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.alive = 1
        #jumping variables
        self.ySpeed = JUMP_HEIGHT
        self.in_air = False
        #shooting cooldown
        self.dShoot = 0
        self.shooting = False
        self.rocket_direction = 0
        #navigation and scrolling
        self.origin = pygame.math.Vector2()
    
    def movement(self, dt, tiles):
        #get input
        #im using 'move' to make sure I can keep the direction
        #without constantly moving the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.kill()
            self.alive = False
        if keys[pygame.K_a]:
            self.direction.x = 1
            move = 1
        elif keys[pygame.K_d]:
            self.direction.x = -1
            move = 1
        else:
            move = 0
        #change x pos and check for collision
        self.rect.x -= self.direction.x * PLAYERSPEED * dt * move
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
        #scroll
        self.origin = pygame.math.Vector2(self.rect.x, self.rect.y)
        #make sure player is facing the right direction
        self.flip_img()
        if self.rect.y < 0 or self.rect.y > DISPLAY_HEIGHT:
            self.kill()
            self.alive = False
        if self.origin.x > DISPLAY_WIDTH - SCROLL_THRESH or self.origin.x < SCROLL_THRESH:
            dx = self.direction.x * PLAYERSPEED * dt
            self.rect.x += dx
            return(dx)
        else:
            return(0)
            
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

    def collisions(self, enemies, flags):
        for sprite in enemies:
            if self.rect.colliderect(sprite.rect):
                self.kill()
                self.alive = 0
        for sprite in flags:
            if self.rect.colliderect(sprite.rect):
                self.alive = 2
        return self.alive

    def shoot(self, dt, rocket_group, can_collide):
        time = pygame.time.get_ticks()
        if pygame.mouse.get_pressed()[0] and time - self.dShoot > 2000:
            self.rocket_direction = -self.direction.x
            if self.rocket_direction == 0:
                self.rocket_direction = 1
            self.rocket = Rocket([self.rect.x, self.rect.y], self.rocket_direction)
            self.rocket.add(rocket_group)
            self.dShoot = time
            self.shooting = True
        if self.shooting:
            if time - self.dShoot < 2700:
                self.rocket.move(self.rocket_direction, dt)
                self.shooting = self.rocket.collide(can_collide)
        if time - self.dShoot > 2700:
            try:
                self.rocket.kill()
            except:
                pass
            self.shooting = False

    def flip_img(self):
        if self.direction.x > 0:
            self.image = pygame.transform.flip(pygame.image.load("Graphics/player.png").convert_alpha(), True, False)
        else:
            self.image = pygame.image.load("Graphics/player.png").convert_alpha()


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        #Tile image and rect
        self.name = "tile"
        self.image = pygame.image.load("Graphics/tile.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

class Rocket(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        super().__init__()
        if direction > 0:
            self.image = pygame.image.load("Graphics/rocket.png").convert_alpha()
            self.rect = self.image.get_rect(center=pos)
        else:
            self.image = pygame.transform.flip(pygame.image.load("Graphics/rocket.png").convert_alpha(), True, False)
            self.rect = self.image.get_rect(center=pos)
    
    def move(self, direction, dt):
        self.rect.x += 500 * direction * dt

    def collide(self, can_collide):
        alive = True
        for sprite in can_collide:
            if sprite.rect.colliderect(self.rect):
                self.explode()
                alive = False
                if sprite.name == 'enemy':
                    sprite.kill()
        return alive
    
    def explode(self):
        self.image = pygame.image.load("Graphics/explosion.png").convert_alpha()
        self.rect = self.image.get_rect(center=[self.rect.x, self.rect.y])

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        #enemy image and rect
        self.image = pygame.image.load("Graphics/enemy.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.name = "enemy"
        self.xDirection = 1
    
    def strafe(self, dt, can_collide):
        self.rect.x -= 200 * self.xDirection * dt
        self.xCollision(can_collide)

    def xCollision(self, can_collide):
        for sprite in can_collide:
            if sprite.rect.colliderect(self.rect) and not sprite.rect == self.rect:
                if self.xDirection > 0: #moving left
                    self.rect.left = sprite.rect.right
                    self.xDirection = -1
                elif self.xDirection < 0: #moving left
                    self.rect.right = sprite.rect.left
                    self.xDirection = 1
            
class Flag(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("Graphics/flag.png").convert_alpha()
        self.rect = self.image.get_rect(center=pos)

class Image(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()
        self.image = pygame.image.load("Graphics/" + type + ".png").convert_alpha()
        if type == 'flag':
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - FLAG_HEIGHT + TILE_HEIGHT))
        else:
            self.rect = self.image.get_rect(topleft=pos)