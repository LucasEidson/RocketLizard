import pygame
import settings
from stage1 import Stage1

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode([settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT])
        self.clock = pygame.time.Clock()
        
        self.stage1 = Stage1()

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(60) / 1000
            self.stage1.run()
            self.stage1.event_loop(dt)
            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.run()