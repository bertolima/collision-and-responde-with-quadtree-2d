import pygame

class Quadtree(pygame.sprite.Sprite):
    def __init__(self, width, height, coord , maxDepth = 8, depth = 0):
        super().__init__()
        self.nl = None
        self.nr = None
        self.sl = None
        self.sr = None
        self.divided = False
        self.maxDepth = maxDepth

        self.depth = depth
        self.width = width
        self.height = height
        self.coord = coord

        self.image = pygame.Surface([width, height])
        self.image.fill("black")
        self.image.set_colorkey("black")
        self.color = ("red")
        pygame.draw.rect(self.image,self.color,(0,0, self.width, self.height),1)
        self.rect = self.image.get_rect()
        self.rect.x = self.coord.x
        self.rect.y = self.coord.y
  
    
    def divide(self, groups:pygame.sprite.Group, objects):
        if(self.depth == self.maxDepth):
            return
        self.nl = Quadtree(self.width/2,self.height/2, pygame.math.Vector2(self.coord.x,self.coord.y), self.maxDepth, self.depth+1)
        self.nr = Quadtree(self.width/2,self.height/2, pygame.math.Vector2(self.coord.x+self.width/2,self.coord.y),self.maxDepth, self.depth+1)
        self.sl = Quadtree(self.width/2,self.height/2, pygame.math.Vector2(self.coord.x,self.coord.y+self.height/2), self.maxDepth, self.depth+1)
        self.sr = Quadtree(self.width/2,self.height/2, pygame.math.Vector2(self.coord.x+self.width/2,self.coord.y+self.height/2), self.maxDepth, self.depth+1)
        groups.add(self.nl)
        objects.append(self.nl)
        groups.add(self.nr)
        objects.append(self.nr)
        groups.add(self.sl)
        objects.append(self.sl)
        groups.add(self.sr)
        objects.append(self.sr)

        self.divided = True

    def subdivide(self, groups:pygame.sprite.Group, objects):
        self.divide(groups, objects)
        if(self.divided):
            self.nl.subdivide(groups, objects)
            self.nr.subdivide(groups, objects)
            self.sl.subdivide(groups, objects)
            self.sr.subdivide(groups, objects)

    def update(self, treeGroup, ballGroup):
        for elem in ballGroup:
            if(self.divided and self.contains(elem)):
                treeGroup.add(self)
                self.nl.update(treeGroup, ballGroup)
                self.nr.update(treeGroup, ballGroup)
                self.sl.update(treeGroup, ballGroup)
                self.sr.update(treeGroup, ballGroup)
    
    def draw(self, window):
        pygame.draw.aaline(window, self.color, self.p1,self.p2)
        pygame.draw.aaline(window, self.color, self.p2,self.p4)
        pygame.draw.aaline(window, self.color, self.p3,self.p4)
        pygame.draw.aaline(window, self.color, self.p1,self.p3)
        #pygame.draw.rect(window,self.color,(self.p1.x, self.p1.y, self.width, self.height),1)
    
    def contains(self, other):
        return (self.coord.x < other.rect.x-other.radius and
                self.coord.x + self.width > other.rect.x+other.radius and
                self.coord.y < other.rect.y-other.radius and
                self.coord.y + self.height > other.rect.y+other.radius)


