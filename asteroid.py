import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
from random import uniform as rand_uni


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH,
        )

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        new_dir_degrees = rand_uni(20, 50)
        first_new_dir = self.velocity.rotate(new_dir_degrees)
        sec_new_dir = self.velocity.rotate(-new_dir_degrees)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = first_new_dir * 1.2

        sec_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        sec_asteroid.velocity = sec_new_dir * 1.2

    def update(self, dt):
        self.position += self.velocity * dt
