import pygame

#This is adapted from Python Crash Course
class Ship():
    def __init__(self, screen):
        self.screen = screen
        #This will load the ship sprite and get its rect (or rectangle)
        self.image = pygame.image.load()
        self.rect = self.image.get_rect("finalProject/Shup.gif")
        self.screen_rect = screen.get_rect()
        #This will tell where to start the each new ship
        self.rect.centerx = self.screen_rect.centerx
        self.rect.left = self.screen_left
    def blitme(self):
        #THis code draws the ship at its current location on the screen
        self.screen.blit(self.image, self.rect)

    