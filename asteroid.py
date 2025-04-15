import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "cornsilk3", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            break_angle = random.uniform(20,50)
            vec1 = self.velocity.rotate(break_angle)
            vec2 = self.velocity.rotate(-break_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new1 = Asteroid(self.position.x,self.position.y,new_radius)
            new2 = Asteroid(self.position.x,self.position.y,new_radius)
            new1.velocity = vec1*ASTEROID_SHOT_SPEED_BOOST
            new2.velocity = vec2*ASTEROID_SHOT_SPEED_BOOST