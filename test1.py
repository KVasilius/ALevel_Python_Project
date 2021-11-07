"""
pygame.init()
pygame.display.set_mode((600,400))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
"""
import pygame
from pygame.locals import *
from time import sleep

class Snake_Segments(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.image = pygame.Surface([15, 15]) # change to variable later
        self.image.fill([255,255,255]) # change to variable later
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        
class Snake_Game:
    pygame.init()
    max_fps = 30
    def __init__(self,map_width, map_height):
        #self.size = 1080, 720 #int(input("Enter width: ")), int(input("Enter hight: ")) # place keepers
        self.screen = pygame.display.set_mode((map_width, map_height)) # imported from tkinter
        self.fps_clock = pygame.time.Clock()
        self.fps_clock.tick(Snake_Game.max_fps)
        self.running = True
        #self.rect = pygame.draw.rect(self.screen, (255,255,255),(150,150,15,15)) #xpos,ypos,width,height
        pygame.display.flip()

    def setup(self):
        #self.snake_segments()
        self.render()
        self.running_loop()

    def render(self):
        #return self.screen
        self.all_segments = pygame.sprite.Group()
        self.test1 = Snake_Segments(map_width, map_height)
        self.all_segments.add(self.test1)
        self.all_segments.draw(self.screen)
        self.all_segments.update()
        pygame.display.flip()

    def running_loop(self):
        self.all_segments_list = []
        self.seg_x_pos = map_height / 2
        self.seg_y_pos = map_width / 2
        for x in range(5):
            self.new_segment = Snake_Segments(self.seg_x_pos+15*x, self.seg_y_pos)
            self.all_segments_list.append(self.new_segment)
            self.all_segments.add(self.new_segment)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            print("s")
            pygame.display.update()
        #self.fps_clock.tick(5)

"""all_segments = pygame.sprite.Group()
test1 = Snake_Segments()
all_segments.add(test1)
"""
map_width, map_height = 1080, 720
print(map_height)
test_run = Snake_Game(map_width, map_height)
test_run.setup()
screen = test_run.render()
#all_segments.draw(screen)
"""
pygame.init()
pygame.display.set_mode((600,400))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()

"""

