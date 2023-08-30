import pygame
import random
from Ball import Ball
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
        self.test = []
        self.tree = None

        self.initVariables(x,y)
        self.initWindow()
        self.initTree()
    
    def initVariables(self, x, y):
        self.running = True
        pygame.init()
        self.clock = pygame.time.Clock()
        self.coord = pygame.math.Vector2(x,y)
        self.objects = pygame.sprite.Group()
        self.rectangles = pygame.sprite.Group()
        self.dt = self.clock.tick(60) / 1000

    def initWindow(self):
        self.window = pygame.display.set_mode((self.coord))
    
    def initTree(self):
        self.tree = Quadtree(self.coord.x, self.coord.y, pygame.math.Vector2(0,0),5)
        self.tree.subdivide(self.rectangles, self.test)

    def createBalls(self):
        create = True
        self.mousePosition = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == True:
            self.objects.add(Ball(random.randint(5,15), self.mousePosition[0], self.mousePosition[1]))

    def updateBalls(self):
        self.objects.update(self.coord.x, self.coord.y, self.dt, self.objects)
        
    def renderBalls(self):
        self.objects.draw(self.window)
    
    def updateTree(self):
        self.rectangles.empty()
        self.tree.update(self.rectangles, self.objects)
    
    def renderRectangles(self):
        self.rectangles.draw(self.window)

    def poolEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    self.running = False

    def update(self):
        self.poolEvent()
        self.createBalls()
        self.updateBalls()
        self.updateTree()
        
    def render(self):
        self.window.fill("black")

        self.renderBalls()

        self.renderRectangles()
        
        pygame.display.flip()
        self.dt = self.clock.tick(60) / 1000

    
    def isRunning(self):
        return self.running
    
    def stop(self):
        pygame.quit()

