import pygame
import random
import numpy as np

MAX_SPEED = 500
MAX_ACELLERATION = 5

class Particle(pygame.sprite.Sprite):

    def __init__(self, radius, x, y):
        super().__init__()
        self.center = None
        
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
        self.speed = np.invert(self.speed)
        other.speed = np.invert(other.speed)

    def colide(self, other):
        return (self.rect.center[0] - other.rect.center[0]) * (self.rect.center[0] - other.rect.center[0]) + (self.rect.center[1] - other.rect.center[1]) * (self.rect.center[1] - other.rect.center[1]) <= pow(self.radius+other.radius,2)
    
    def __lt__(self, other):
         return self.rect.x < other.rect.x and self.rect.y < other.rect.y
    



        

