# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    #
    num= 0

    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # game loop 
    while True:
        screen.fill("black") 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        pygame.display.flip()

    
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    



if __name__ == "__main__":
    main()