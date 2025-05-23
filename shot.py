from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, SHOT_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "firebrick1", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def rotate(self, heading):
        self.rotation += heading