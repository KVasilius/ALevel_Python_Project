import pygame
from pygame.locals import *
import _thread
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
    def __init__(self,map_width, map_height):
        global seg_chg
        #----SETTINGS----#
        self.running = True
        self.speed = 100
        self.change = 15
        self.size = map_width, map_height #int(input("Enter width: ")), int(input("Enter hight: ")) # place keepers
        self.max_fps = 30
        self.seg_x_pos = map_height / 2
        self.seg_y_pos = map_width / 2
        self.screen = pygame.display.set_mode((map_width, map_height)) # imported from tkinter
        seg_chg = 0
        self.x_pos_counter = 0
        #----SETTINGS----#
        self.fps_clock = pygame.time.Clock()
        self.fps_clock.tick(self.max_fps)
        
        #self.rect = pygame.draw.rect(self.screen, (255,255,255),(150,150,15,15)) #xpos,ypos,width,height
        #pygame.display.update()

    def setup(self):
        #self.snake_segments()
        self.render()
        self.running_loop()

    def render(self):
        self.all_segments_list = []
        self.all_segments = pygame.sprite.Group()
        for x in range(7):
            new_segment = Snake_Segments(self.seg_x_pos+(self.change+1)*x, self.seg_y_pos)
            self.all_segments_list.append(new_segment)
            self.all_segments.add(new_segment)
        self.test1 = Snake_Segments(map_width, map_height)
        self.all_segments.add(self.test1)
        self.all_segments.update()

    def running_loop(self):
        import keyboard
        global seg_chg
        def key_detection():
            global seg_chg
            while True:
                if keyboard.is_pressed("up_arrow"):
                    seg_chg = -2
                if keyboard.is_pressed("down_arrow"):
                    seg_chg = 2
                if keyboard.is_pressed("left_arrow"):
                    seg_chg = -1
                if keyboard.is_pressed("right_arrow"):
                    seg_chg = 1
        
        """def running_thread():
            try:
                while self.running:
                    
                        self.keys = pygame.key.get_pressed()
                        if self.keys[pygame.K_LEFT]: print("w")#self.seg_chg = -1
                        if self.keys[pygame.K_RIGHT]: print("w")#self.seg_chg = 1
                        if self.keys[pygame.K_UP]: print("w")#self.seg_chg = -2
                        if self.keys[pygame.K_DOWN]: print("w")#self.seg_chg = 2"""
        _thread.start_new_thread(key_detection)
        while self.running:
            self.seg_chg = seg_chg
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            #pygame.event.wait()
            #def running_thread(self)
            """if self.keys[pygame.K_LEFT]: self.seg_chg = -1
            if self.keys[pygame.K_RIGHT]: self.seg_chg = 1
            if self.keys[pygame.K_UP]: self.seg_chg = -2
            if self.keys[pygame.K_DOWN]: self.seg_chg = 2
            self.screen.fill((0, 0, 0))"""
            #pygame.display.flip()
            self.screen.fill((0, 0, 0))
            if self.seg_chg == 1:
                self.seg_x_pos += 16
                #new_segment = Snake_Segments(self.seg_x_pos+(self.change+1)
                    # *x, self.seg_y_pos)
                    #self.all_segments_list.append(new_segment)
                    #self.all_segments.add(new_segment)
                    #new_segment = Snake_Segments(self.x_pos_counter, self.seg_y_pos)
                    #self.all_segments_list.insert(0, new_segment)
                    #self.all_segments.remove(self.all_segments_list.pop())
                    #self.all_segments.add(new_segment)
                    #self.all_segments.add(new_segment)
                    #self.all_segments.update()
                    #print(self.all_segments_list)
            if self.seg_chg == -1:
                self.seg_x_pos += -16
            if self.seg_chg == 2:
                self.seg_y_pos += 16
            if self.seg_chg == -2:
                self.seg_y_pos += -16
                    #self.all_segments.update()
                #pygame.display.update()
            new_segment = Snake_Segments(self.seg_x_pos, self.seg_y_pos)
            self.all_segments_list.insert(0, new_segment)
            self.all_segments.remove(self.all_segments_list.pop())
            self.all_segments.add(new_segment)
                #self.all_segments.add(new_segment)
            self.all_segments.update()
            self.all_segments.draw(self.screen) #Creates the segments on screen
            pygame.display.update() #Updates(displays) the drawn segments onto the screen
            pygame.time.delay(self.speed)
            #if self.all_segments_list[0].collidelist(self.all_segments_list) != -1: print("collide")
            #pygame.time.delay(self.speed)
            print(self.seg_chg)
                #if __name__ == '__main__':
                #Process(target=self.running_thread()).start()


                #print("s")
                #pygame.display.update()
        #_thread.start_new_thread(main_thread)
map_width, map_height = 1080, 720
#print(map_height)
test_run = Snake_Game(map_width, map_height)
test_run.setup()
#screen = test_run.render()