import pygame 
import settings
#import main

class Player:
    def __init__(self):
        #display_surface is screen
        self.display_surface = pygame.display.get_surface()

        #for movement and nav
        self.origin = pygame.math.Vector2(settings.DISPLAY_WIDTH/2, settings.DISPLAY_HEIGHT - settings.TILE_HEIGHT) 

    #checks for input
    def event_loop(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.actions()
                

    #binding player actions and movements
    def actions(self):
        #abilities
        if pygame.mouse.get_pressed()[0]:
            #eventually make this shoot!
            self.shoot()
        elif pygame.mouse.get_pressed()[2]:
             #eventually make this dash!
             #set a cooldown
            self.dash()
    
    def move(self, dt, jump):
        #movement keys:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.origin.x -= settings.PLAYERSPEED * dt
        if keys[pygame.K_d]:
            self.origin.x += settings.PLAYERSPEED * dt
        #jumping
        #test if on ground by making rect size of image +1 pixel
        #then test if intersecting with floor rect
        if jump == False and keys[pygame.K_SPACE]: 
            jump = True
        if jump:
            self.origin.y -= settings.JSPEED * dt
            settings.JSPEED -= 10
            #a little unclean for now(only works if JSPEED == 500)
            if settings.JSPEED < -500:
                jump = False
                settings.JSPEED = 500
        return jump
    
    def shoot(self):
        print("shoot!")

    def dash(self):
        print("dash!")

    #runs the first stage
    def run(self):
        self.display_surface.fill([74, 140, 86])
        pygame.draw.circle(self.display_surface, 'black', self.origin, 10)