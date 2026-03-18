import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
class Asteroid(CircleShape):

    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2
        
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        krug = pygame.draw.circle(surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH)
    def update(self, dt):

        self.position += self.velocity * dt
    