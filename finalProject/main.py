#Me and Aaron will be working on making a side scroller with a ship shooting lasers, power ups, and maybe a boss at the end
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Import libraries
import pygame
import sys
from ship import Ship()
from laser import Laser()
from settings import Settings()
from boss import Boss()



#Code gotten from Python Crash Course that runs the actual screen for the game
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Space Shooter")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.flip()

run_game()