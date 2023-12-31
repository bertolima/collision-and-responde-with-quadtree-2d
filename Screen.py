import pygame
import random
import numpy as np
import time
import threading
from Particle import Particle
from Quadtree import Quadtree

class Screen:
    def __init__(self, x:int, y:int):
        self.coord = None

        self.window = None
        self.clock = None
        self.running = False
        self.dt = None
        self.mousePosition = None

        self.objects:pygame.sprite.Group = None
        self.rectangles:pygame.sprite.Group = None
        self.npParticles = None
        self.test = []
        self.tree = None
        self.cont = 0
        self.sum = 0
        self.canDrawTree = False

        self.initVariables(x,y)
        self.initWindow()
        self.initParticles()
        self.initTree()
    
    def initVariables(self, x, y):
        self.running = True
        pygame.init()
        self.clock = pygame.time.Clock()
        self.coord = pygame.math.Vector2(x,y)
        self.objects = pygame.sprite.Group()
        self.dt = self.clock.tick(60) / 1000

    def initWindow(self):
        self.window = pygame.display.set_mode((self.coord))
    
    def initTree(self):
        self.tree = Quadtree(int(self.coord.x),6)
        self.tree.divide()

    def initParticles(self):
        numberElementos = 100
        self.npParticles = np.empty(numberElementos, dtype=Particle)
        for i in range(numberElementos):
            new_element = Particle(random.randint(5,15), random.randint(20,780), random.randint(20,780))
            self.objects.add(new_element)
            self.npParticles[i] = new_element


    def createParticles(self):
        create = True
        self.mousePosition = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == True:
            self.objects.add(Particle(random.randint(5,15), self.mousePosition[0], self.mousePosition[1]))

    def updateParticles(self):
        self.objects.update(self.coord.x, self.coord.y, self.dt, self.objects)
        
    def renderParticles(self):
        self.objects.draw(self.window)
    
    def updateTree(self):
        self.tree.updateTree(self.npParticles)
    
    def renderRectangles(self):
        if(self.canDrawTree):
            self.tree.drawNode(self.window)

    def poolEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    self.running = False
                elif(event.key == pygame.K_f):
                    if(self.canDrawTree):
                        self.canDrawTree = False
                    else:
                        self.canDrawTree = True

    def update(self):
        self.poolEvent()
        self.updateParticles()
        self.updateTree()

    def render(self):
        self.cont +=1
        self.window.fill("black")

        self.renderParticles()

        self.renderRectangles()
        
        pygame.display.flip()
        self.dt = self.clock.tick(60) / 1000
        self.sum += self.clock.get_fps()
        media = self.sum//self.cont
        print(media)

    
    def isRunning(self):
        return self.running
    
    def stop(self):
        pygame.quit()

