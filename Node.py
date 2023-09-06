import pygame
from collections import deque

class Node(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()
        self.ne = None
        self.nd = None
        self.sd = None
        self.se = None
        self.image = pygame.Surface([width, width])
        self.image.fill("black")
        self.image.set_colorkey("black")
        self.color = ("red")
        pygame.draw.rect(self.image,self.color,(0,0, width, width),1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.divided = False
    
    def divide(self, arr):
        new_width = self.width >> 1
        self.ne = Node(self.rect.x,self.rect.y, new_width)
        self.nd = Node(self.rect.x+new_width,self.rect.y, new_width)
        self.sd = Node(self.rect.x+new_width,self.rect.y+new_width, new_width)
        self.se = Node(self.rect.x,self.rect.y+new_width, new_width)
        arr.append(self.ne)
        arr.append(self.nd)
        arr.append(self.sd)
        arr.append(self.se)
        self.divided = True

    
    def contains(self, other):
        if(self.rect.x <= other.rect.x + other.radius <= self.rect.x+self.width and self.rect.y <= other.rect.y + other.radius <= self.rect.y+self.width):
            if(other.rect.x >= self.rect.x and other.rect.x + other.radius <= self.rect.x+self.width and 
               other.rect.y >= self.rect.y and other.rect.y + other.radius <= self.rect.y+self.width):
                return True
        return False

    def getChildren(self, arr, group):
        if(self.ne is not None):
            arr.append(self.ne)
            arr.append(self.nd)
            arr.append(self.sd)
            arr.append(self.se)
        
            group.add(self.ne)
            group.add(self.nd)
            group.add(self.sd)
            group.add(self.se)

    def updateTree(self, ParticleList, drawList):
        ver = True
        drawList.add(self)
        count = 0
        transversed = deque()
        for particle in ParticleList:
            if (self.contains(particle)):
                count+=1
                transversed.append(particle)
            if(self.divided and count > 4 ):
                ver = False
                self.ne.updateTree(ParticleList, drawList)
                self.nd.updateTree(ParticleList, drawList)
                self.se.updateTree(ParticleList, drawList)
                self.sd.updateTree(ParticleList, drawList)
            elif (ver == True):
                self.updateBalls(transversed)
    
    def updateBalls(self, particleList):
        for ball1 in particleList:
            for ball2 in particleList:
                if (ball1 != ball2 and ball1.colide(ball2)):
                    ball1.updatePositionsPosCollision(ball2)

                
            


    