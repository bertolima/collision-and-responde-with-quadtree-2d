import pygame
import random
import numpy as np

MAX_SPEED = 500
MAX_ACELLERATION = 5
MIN_ACCELERATION = 1

class Particle(pygame.sprite.Sprite):

    def __init__(self, radius, x, y):
        super().__init__()
        self.coord = np.array([x,y])
        self.image = pygame.Surface((radius<<1, radius<<1))
        self.image.fill("white")
        self.image.set_colorkey("white")
        self.color = (random.uniform(0,255), random.uniform(0,255),random.uniform(0,255))
        self.radius = radius
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.speed = np.random.randint(-MAX_SPEED//(self.radius>>1), MAX_SPEED//(self.radius>>1), 2)
        self.acceleration = np.random.randint(-MAX_ACELLERATION//self.radius, MAX_ACELLERATION//self.radius, 2)

    def update(self, x, y, dt, group):
        self.updatePosition(dt)
        self.boundaries(x,y)
        
    def boundaries(self, x, y):
        if (self.rect.x + (self.radius<<1) >= x or self.rect.x <= 0):
            self.speed[0] = self.speed[0] * -1
        if (self.rect.y + (self.radius<<1) >= y or self.rect.y <= 0):
            self.speed[1] = self.speed[1] * -1

    def updatePosition(self, dt):
        self.coord = np.add(self.coord, (self.speed.dot(dt)))
        self.rect.center = self.coord

    def updatePositionsPosCollision(self, other):
        m1, m2 = self.radius**2, other.radius**2
        M = m1 + m2
        r1, r2 = self.radius, other.radius
        d = np.linalg.norm(r1 - r2)**2
        v1, v2 = self.speed, other.speed
        u1 = v1 - 2*m2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
        u2 = v2 - 2*m1 / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1)
        self.speed = u1
        other.speed = u2

    def colide(self, other):
        return (self.rect.center[0] - other.rect.center[0]) * (self.rect.center[0] - other.rect.center[0]) + (self.rect.center[1] - other.rect.center[1]) * (self.rect.center[1] - other.rect.center[1]) <= pow(self.radius+other.radius,2)
    
    def __lt__(self, other):
         return self.rect.x < other.rect.x and self.rect.y < other.rect.y
    



        

