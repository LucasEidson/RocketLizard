import pygame
import settings
from player import Player
from tiles import Tile
from stage1 import Stage1

class Main:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.stage1 = Stage1()
        self.player = Player()

    def run(self):
        running = True
        jump = False

        while running: 
            dt = self.clock.tick(60) / 1000 
            self.player.run()
            self.player.event_loop()
            jump = self.player.move(dt, jump)
            #runs display
            self.stage1.run()

if __name__ == '__main__':
    main = Main()
    main.run()