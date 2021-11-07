import pygame, keyboard, _thread, random
from pygame.locals import *

class Snake_Segments(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, size):
        super().__init__()
        self.image = pygame.Surface([size, size]) # change to variable later
        self.image.fill([255,255,255]) # change to variable later
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        
class Snake_Game:
    pygame.init()
    def __init__(self,map_width, map_height):
        global seg_chg
        #----SETTINGS----#
        self.running = True
        self.size = 15
        #self.size = map_width, map_height #int(input("Enter width: ")), int(input("Enter hight: ")) # place keepers
        self.max_fps = 1 #speed
        self.seg_x_pos = 561#map_height / 2
        self.seg_y_pos = 353#map_width / 2
        self.screen = pygame.display.set_mode((map_width, map_height)) # imported from tkinter
        self.coordinate_list = []
        seg_chg = 0
        self.x_pos_counter = 0
        self.snake_segments_list = []
        self.snake_segments = pygame.sprite.Group()
        self.food_segments = pygame.sprite.Group()
        self.obstical_peramiters_list = []
        self.obstical_collision_list = []
        self.alive = True
        self.food_colour = (200,200,200)
        self.score = -1
        self.lock = True
        self.starting_size = 3
        self.obstical_list = []
        self.num_obsticals = 4 
        #----SETTINGS----#
        self.fps_clock = pygame.time.Clock()
        #self.fps_clock.tick(self.max_fps)

    def setup(self):
        self.food()
        self.obsticals()
        self.render()
        self.running_loop()

    def render(self):
        for x in range(self.starting_size):
            new_segment = Snake_Segments(self.seg_x_pos+(self.size+1)*x, self.seg_y_pos, self.size)
            self.snake_segments_list.append(new_segment)
            self.snake_segments.add(new_segment)
        self.test1 = Snake_Segments(map_width, map_height, self.size)
        self.snake_segments.add(self.test1)
        self.snake_segments.update()

    def food(self):
        #self.food = pygame.Rect(0,0,15,15)
        #pygame.draw.rect(self.screen,(255,255,255),(100,100,100,100))
        self.food_x_pos, self.food_y_pos = (random.randint(0,67)*16)+1,(random.randint(0,44)*16)+1
        self.food_peramiters = (self.food_x_pos, self.food_y_pos,self.size,self.size)
        #self.food_peramiters = (1,1,self.size,self.size)
        self.score += 1
        if self.lock != True:
            new_segment = Snake_Segments(self.seg_x_pos+16, self.seg_y_pos+16, self.size)
            self.snake_segments_list.append(new_segment)
        else: self.lock = False
        self.max_fps += 1

    def obsticals(self):
        seg_chg_x_list, seg_chg_y_list = [0,16,0,16], [0,0,16,16]
        for _ in range(random.randint(0,5)):
            self.obstical_x_pos, self.obstical_y_pos = (random.randint(0,66)*16)+1,(random.randint(0,43)*16)+1
            for z in range(self.num_obsticals):
                self.obstical_peramiters = (self.obstical_x_pos+seg_chg_x_list[z], self.obstical_y_pos+seg_chg_y_list[z])
                #self.obstical_peramiters_list = 
                self.obstical_peramiters_list.append(self.obstical_peramiters)
                #print(self.obstical_peramiters)
                #print(self.obstical_peramiters_list)
                #pygame.draw.rect(self.screen,(255,255,255),self.obstical_peramiters)
                #self.all_obstical_list.append(new_obstical) # appends it to the snake 

                #self.obstical_peramiters = (self.obstical_x_pos+seg_chg_x_list[z], self.obstical_y_pos+seg_chg_y_list[z],self.size,self.size)
                #self.obstical_list.append(self.obstical_peramiters)
            

        

    def running_loop(self):
        global seg_chg
        # 
        def key_detection_thread():
            global seg_chg
            while True:
                if keyboard.is_pressed("up_arrow") and seg_chg != 2: seg_chg = -2
                if keyboard.is_pressed("left_arrow") and seg_chg != 1: seg_chg = -1
                if keyboard.is_pressed("down_arrow") and seg_chg != -2: seg_chg = 2
                if keyboard.is_pressed("right_arrow") and seg_chg != -1: seg_chg = 1
        _thread.start_new_thread(key_detection_thread,())

        while self.running:
            pygame.display.update() #Updates(displays) the drawn segments onto the screen
            for event in pygame.event.get():
                    if event.type == pygame.QUIT: self.running = False
            if self.alive:
                self.screen.fill((0, 0, 0))
                if seg_chg == 1: self.seg_x_pos += 16
                if seg_chg == -1: self.seg_x_pos += -16
                if seg_chg == 2: self.seg_y_pos += 16
                if seg_chg == -2: self.seg_y_pos += -16
                #collide any or the wall
                if pygame.sprite.spritecollideany(self.snake_segments_list[0], self.snake_segments_list[1:-1]) or self.seg_x_pos > 1089 or self.seg_x_pos < 0 or self.seg_y_pos > 721 or self.seg_y_pos < 0: self.alive = False
                #eat food (Collision)
                if self.seg_x_pos == self.food_x_pos and self.seg_y_pos == self.food_y_pos: self.food()
                #obstical collision
                for index in range(len(self.obstical_peramiters_list)):
                    if self.seg_x_pos == self.obstical_peramiters_list[index][0] and self.seg_y_pos == self.obstical_peramiters_list[index][1]: 
                        self.alive = 0
                #snake segments drawring                
                if seg_chg != 0:
                    new_segment = Snake_Segments(self.seg_x_pos, self.seg_y_pos,self.size)
                    self.snake_segments_list.insert(0, new_segment)
                    self.snake_segments.remove(self.snake_segments_list.pop())
                    self.snake_segments.add(new_segment)
                    self.snake_segments.update()
               #obstical rect drawring
                for index in range(len(self.obstical_peramiters_list)):
                    value = self.obstical_peramiters_list[index]
                    value1 = value[0],value[1],self.size,self.size
                    #print(value1)
                    pygame.draw.rect(self.screen,(255,100,1),value1) 
                #food rect drawring
                pygame.draw.rect(self.screen,(255,255,255),self.food_peramiters)
                #for x in range(len(self.obstical_list)): pygame.draw.rect(self.screen,(255,0,255),self.obstical_list[x])
                #self.pygmae.draw.rect(self.screen,(255,255,255),self.food)
                self.snake_segments.draw(self.screen) #Creates the segments on screen
                #self.obstical_segments.draw(self.screen)
                #print(self.score)
                #print(self.food_peramiters)
                self.fps_clock.tick(self.max_fps)
            elif not self.alive: self.screen.fill((0,0,0))


map_width, map_height = 1089, 721 # n = 16 (size plus gap)+1(gap on the end) 69*45
test_run = Snake_Game(map_width, map_height)
test_run.setup() 