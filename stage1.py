import pygame 
import settings
#import main

class Stage1:
    def __init__(self):
        #display_surface is screen
        self.display_surface = pygame.display.get_surface()

        #for movement and nav
        self.origin = pygame.math.Vector2(settings.DISPLAY_WIDTH/2, settings.DISPLAY_HEIGHT - 40) 

    #checks for input
    def event_loop(self, dt):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                self.actions(dt)

    #binding player actions and movements
    def actions(self, dt):
        #abilities
        if pygame.mouse.get_pressed()[0]:
            #eventually make this shoot!
            self.shoot()
        elif pygame.mouse.get_pressed()[2]:
             #eventually make this dash!
             #set a cooldown
            self.dash()
        #movement keys:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.origin.x -= 300 * dt
        if keys[pygame.K_d]:
            self.origin.x += 300 * dt
    def shoot(self):
        print("shoot!")

    def dash(self):
        print("dash!")

    #runs the first stage
    def run(self):
        self.display_surface.fill([74, 140, 86])
        pygame.draw.circle(self.display_surface, 'black', self.origin, 10)