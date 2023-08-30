import pygame
import random

MAX_SPEED = 200
SPEED = 500 

class Ball(pygame.sprite.Sprite):

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
        #self.updateCollision(group)
        self.updatePosition(dt)
        self.boundaries(x,y)
        

    def boundaries(self, x, y):
        if (self.rect.x + 2*self.radius >= x or self.rect.x <= 0):
            self.speed.x = -self.speed.x
        elif(self.rect.y + 2*self.radius >= y or self.rect.y <= 0):
            self.speed.y = -self.speed.y

    def updatePosition(self, dt):
        self.rect.x += self.speed.x * dt
        self.rect.y += self.speed.y * dt

    def updateCollision(self, group):
        group.remove(self)
        currentState = pygame.sprite.spritecollideany(self, group)
        if(currentState is not None):
            self.updatePositionsPosCollision(currentState)
        group.add(self)

    def updatePositionsPosCollision(self, other):
        self.speed.x = -self.speed.x
        self.speed.y = -self.speed.y
        other.speed.x = -other.speed.x
        other.speed.y = -other.speed.y

    def colide(self, other):
        if(pow(self.radius-other.radius,2) <= pow(self.rect.x+self.radius,2) + pow(self.rect.y+self.radius,2) and
           pow(self.radius+other.radius,2) >= pow(self.rect.x+self.radius,2) + pow(self.rect.y+self.radius,2)):
            return True
        return False
    
            



        

