import pygame
from collections import deque
from Node import Node

class Quadtree():
    def __init__(self, width, maxDepth = 8):
        super().__init__()

        self.maxDepth = maxDepth
        self.root = Node(0, 0, width)
        self.Nodes = pygame.sprite.Group()
  
    def divide(self):
        parent = deque()
        parent.append(self.root)
        for i in range(self.maxDepth-1):
            children = deque()
            for elem in parent:
                elem.divide(children)
            parent = children

    def drawNode(self, window):
        self.Nodes.draw(window)

    def updateTree(self, ParticleList):
        self.Nodes.empty()
        self.root.updateTree(ParticleList, self.Nodes)


        


                

            

            

        


        

