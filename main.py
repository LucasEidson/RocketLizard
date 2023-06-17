import pygame
import settings
from player import Player

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode([settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT])
        self.clock = pygame.time.Clock()
        
        self.player = Player()

    def run(self):
        running = True
        jump = False

        while running: 
            dt = self.clock.tick(60) / 1000 
            self.player.run()
            self.player.event_loop()
            jump = self.player.move(dt, jump)
            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.run()