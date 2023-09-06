import pygame
import random
import math

MAX_SPEED = 200
SPEED = 2000 

class Particle(pygame.sprite.Sprite):

    def __init__(self, radius, x, y):
        super().__init__()
        self.center = None
        direction = random.randint(1,4)
        if(direction == 1):
            self.speed = pygame.math.Vector2(SPEED/radius,SPEED/radius)
        elif(direction == 2):
            self.speed = pygame.math.Vector2(-SPEED/radius,-SPEED/radius)
        elif(direction == 3):
            self.speed = pygame.math.Vector2(-SPEED/radius,SPEED/radius)
        elif(direction == 4):
            self.speed = pygame.math.Vector2(SPEED/radius,-SPEED/radius)

        self.image = pygame.Surface((radius*2, radius*2))
        self.image.fill("white")
        self.image.set_colorkey("white")
        self.color = (random.uniform(0,255), random.uniform(0,255),random.uniform(0,255))
        self.radius = radius
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        

    def update(self, x, y, dt, group):
        self.updatePosition(dt)
        #self.updateCollision(group)
        self.boundaries(x,y)
        

    def boundaries(self, x, y):
        if (self.rect.x + 2*self.radius >= x or self.rect.x <= 0):
            self.speed.x = -self.speed.x
        if (self.rect.y + 2*self.radius >= y or self.rect.y <= 0):
            self.speed.y = -self.speed.y

    def updatePosition(self, dt):
        self.rect.x += self.speed.x * dt
        self.rect.y += self.speed.y * dt

    def updateCollision(self, group):
        aux = pygame.sprite.Group()
        for elem1 in group:
            current = elem1
            group.remove(elem1)
            aux.add(current)
            for elem2 in group:
                if(current.colide(elem2)):
                    current.updatePositionsPosCollision(elem2)
        for elem in aux:
            group.add(elem)

    def updatePositionsPosCollision(self, other):
        self.speed.x = -self.speed.x
        self.speed.y = -self.speed.y
        other.speed.x = -other.speed.x
        other.speed.y = -other.speed.y

    def colide(self, other):
        d = math.sqrt((self.rect.x - other.rect.x) * (self.rect.x - other.rect.x) + (self.rect.y - other.rect.y) * (self.rect.y - other.rect.y))
        return (d <= self.radius+other.radius)
    
    def __lt__(self, other):
         return self.rect.x < other.rect.x and self.rect.y < other.rect.y
    



        

