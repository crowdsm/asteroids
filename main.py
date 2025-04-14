# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

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
    astroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group() 

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, astroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # Needs to be created after the groups/containers defined (static changes) 
    player = Player(x,y)
    astroid_field = AsteroidField()

    # game loop 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for astroid in astroids:
            if astroid.collisions_check(player):
                return print("Game over!")
        
            for bullet in shots:
                if astroid.collisions_check(bullet):
                    astroid.kill()
                    bullet.kill()
        
        screen.fill("black") 
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)/1000  


if __name__ == "__main__":
    main()