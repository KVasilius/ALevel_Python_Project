import pygame

############################################################
#Importing sprite parent class for the snake segments
class Snake_segments_class(pygame.sprite.Sprite):
    def __init__(self, segments_W, segments_H):
        super().__init__()
        self.image = pygame.Surface([segments_W, segments_H])
        self.image.fill((255,255,255))
        self.rect = self.image.get.rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
############################################################
#Initiating pygame
pygame.init()
screen = pygame.display.set_mode([800, 600])
allspriteslist = pygame.sprite.Group()
############################################################
#Creating snake
snake_segments = []
for i in range(15):
    x = 250 - (segments_W, segments_M) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)
############################################################
#Running loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
############################################################
#Change snake direction
        if event.tpe == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segments_W + segments_M) * -1
                
