import random
import pygame
from Sprites import Image
from settings import *
#0 = nothing, 1 = tile, 2 = enemy, 3 = flag, 4 = player

class Level():
    def __init__(self):
        #the screen is 12 tiles high, 16 tiles wide
        self.display_surface = pygame.display.get_surface()
        #create groups:
        self.images = pygame.sprite.Group()
        #create important variables
        self.tile_types = ['none', 'tile', 'enemy', 'flag', 'player']
        self.selected = 0
        self.inEditor = True
        self.origin = 0
        self.screenMap = [[0] * 200, 
                          [0] * 200,
                          [0] * 200,
                          [0] * 200,
                          [0] * 200,
                          [0] * 200,
                          [0] * 200,
                          [0] * 200,
                          [0] * 200,
                          [0] * 200,
                          [0] * 200,
                          [0] * 200
                          ]
        self.HEIGHT = 12
        self.WIDTH = 16
    
    def draw_grid(self):
        cols = DISPLAY_WIDTH // TILE_WIDTH + 1
        rows = DISPLAY_HEIGHT // TILE_HEIGHT
        offset = self.origin - int(self.origin / TILE_WIDTH) * TILE_WIDTH
        for col in range(cols):
            x = offset + col * TILE_WIDTH
            pygame.draw.line(self.display_surface, 'black', (x, 0), (x, DISPLAY_HEIGHT))
        for row in range(rows):
            y = row * TILE_HEIGHT
            pygame.draw.line(self.display_surface, 'black', (0, y), (DISPLAY_WIDTH, y))

    def get_input(self):
        dx = 0
        keys = pygame.key.get_pressed()
        #select tile
        if keys[pygame.K_0]:
            self.selected = 0
        elif keys[pygame.K_1]:
            self.selected = 1
        elif keys[pygame.K_2]:
            self.selected = 2
        elif keys[pygame.K_3]:
            self.selected = 3
        elif keys[pygame.K_4]:
            self.selected = 4
        #move screen
        if keys[pygame.K_a] and self.origin < 0: #move everything right
            dx = 10
        if keys[pygame.K_d] and self.origin > (-200 * TILE_WIDTH) + DISPLAY_WIDTH: #move everything left
            dx = -10
        self.origin += dx
        self.scroll_sprites(dx)

        #leave editor
        if keys[pygame.K_ESCAPE]:
            self.inEditor = False


    def place_tiles(self):
        if pygame.mouse.get_pressed()[0]:
            x = int((pygame.mouse.get_pos()[0] - self.origin) // TILE_WIDTH)
            y = int(pygame.mouse.get_pos()[1] // TILE_HEIGHT)
            if 0 <= x < 200 and 0 <= y < (DISPLAY_HEIGHT // TILE_HEIGHT) and self.screenMap[y][x] == 0:
                self.screenMap[y][x] = self.selected
                if self.tile_types[self.selected] != 'none':
                    sprite = Image([x * TILE_WIDTH + self.origin, y * TILE_HEIGHT], self.tile_types[self.selected])
                    self.images.add(sprite)
        elif pygame.mouse.get_pressed()[2]:
            x = int((pygame.mouse.get_pos()[0] - self.origin) // TILE_WIDTH)
            y = int(pygame.mouse.get_pos()[1] // TILE_HEIGHT)
            if 0 <= x < 200 and 0 <= y < (DISPLAY_HEIGHT // TILE_HEIGHT):
                self.screenMap[y][x] = 0
                for sprite in self.images:
                    if (sprite.rect.x - self.origin) // TILE_WIDTH == x and sprite.rect.y // TILE_HEIGHT == y:
                        sprite.kill()
        
    def scroll_sprites(self, dx):
        for sprite in self.images:
            sprite.rect.x += dx

    def write_file(self):
        levelFile = open("Levels/level1.txt", "w")
        for i in range(len(self.screenMap)):
            if i > 0:
                levelFile.write('\n')
            for j in range(len(self.screenMap[i])):
                levelFile.write(str(self.screenMap[i][j]) + ", ")
        levelFile.close()

    def run(self, dt):
        self.display_surface.fill([201, 251, 201])
        self.get_input()
        self.draw_grid()
        self.place_tiles()

        #draw groups
        self.images.draw(self.display_surface)
        pygame.display.update()
        if self.inEditor == False:
            self.write_file()
        return(self.inEditor)

