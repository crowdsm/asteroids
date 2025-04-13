# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *

def main():
    #
    num= 0
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group() 
    
    Player.containers = (updatable, drawable)

    # Needs to be created after the groups/containers defined (static changes) 
    player = Player(x,y)

    print(f"updateable: {updatable.sprites()}")
    print(f"drawable: {drawable.sprites()}")

    # game loop 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        screen.fill("black") 
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)/1000

    
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    



if __name__ == "__main__":
    main()