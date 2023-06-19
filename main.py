import pygame
from settings import *
from game import Game


class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])
        self.clock = pygame.time.Clock()
        self.game = Game()

    def run(self):
        while True: 
            dt = self.clock.tick(60) / 1000
            #from game.py
            self.game.run(dt)
            self.game.event_loop() 

if __name__ == '__main__':
    main = Main()
    main.run()