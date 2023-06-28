import pygame
from settings import *
from game import Game 
from levelEditor import Level 

class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])
        pygame.display.set_caption("Rocket Lizard")
        icon = pygame.image.load("Graphics/Lizardstill1.png")
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.game = Game()
        self.level = Level()

    def run(self):
        enter_editor = False
        while True: 
            dt = self.clock.tick(60) / 1000
            #from game.py
            if enter_editor:
                self.level.run(dt)
            else:
                enter_editor = self.game.run(dt)
            self.game.event_loop() 

if __name__ == '__main__':
    main = Main()
    main.run()