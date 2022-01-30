from random import randrange as rnd
from itertools import cycle
from random import choice
from tracemalloc import start
import pygame as pg
import time
from resources import *
from tools import *
from Qtools import *

pg.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 300
FPS = 120
speed = 4
status = 0     #0 = Alive | 1 = Death
height = 110

"""
///////////////////////////////////////////////////////////
   QUANTUM ENGINE
///////////////////////////////////////////////////////////
"""

class GateManager():
    def __init__(self):
        self.gates = []
        self.qc = QuantumCircuit(1)

    def push_gates(self,gate):
        self.gates.append(gate)
        add_gate(self.qc,gate,0)
    
    def get_gates(self):
        return self.gates

    def get_qc(self):
        return self.qc.draw()

    def measure(self):
        self.qc.measure_all()
        sim = Aer.get_backend('aer_simulator')
        x = measuring(self.qc,sim,1)
        k = list(x.keys())
        self.gates.clear()
        self.qc = QuantumCircuit(1)
        if k[0]=='1':
            self.qc.x(0)
        return k[0]

class ObstacleManager():
    def __init__(self):
        self.obstacles = [noise_w_s, noise_w_l]
        self.obs_height = 140
        self.obs1 = (rnd(600, 600+500), self.obs_height)
        self.obs2 = (rnd(600+100+500, 1200+500), self.obs_height)
        self.obast1 = choice(self.obstacles)
        self.obast2 = choice(self.obstacles)
        if self.obast1 in [noise_w_s, noise_w_l]:self.obs1 = (self.obs1[0], 115)
        if self.obast2 in [noise_w_s, noise_w_l]:self.obs2 = (self.obs2[0], 115)

    def update_items(self, screen):
        global height
        screen.blit(pg.image.fromstring(self.obast1.tobytes(), self.obast1.size, 'RGBA'), self.obs1)
        screen.blit(pg.image.fromstring(self.obast2.tobytes(), self.obast2.size, 'RGBA'), self.obs2)
        
        if self.obs1[0]<=-50:
            self.obs1 = (rnd(600, 600+500), self.obs_height)
            self.obast1 = choice(self.obstacles)
            if self.obast1 in [noise_w_s, noise_w_l]:self.obs1 = (self.obs1[0], 115)
        if self.obs2[0]<=-50:
            self.obs2 = (rnd(600+100+500, 1200+500), self.obs_height)
            self.obast2 = choice(self.obstacles)
            if self.obast2 in [noise_w_s, noise_w_l]:self.obs2 = (self.obs2[0], 115)

        self.player_stading_cub = (5, height, 5+43, height+46)

    def display_obstacle(self):
        self.obs1 = (self.obs1[0]-speed, self.obs1[1])
        self.obs2 = (self.obs2[0]-speed, self.obs2[1])
        
        self.obs1_cub = (self.obs1[0], self.obs1[1], self.obs1[0] + self.obast1.size[0], self.obs1[1] + self.obast1.size[1])
        self.obs2_cub = (self.obs2[0], self.obs2[1], self.obs2[0] + self.obast2.size[0], self.obs2[1] + self.obast2.size[1])
        
        if self.obs1_cub[0]<=self.player_stading_cub[2]-10<=self.obs1_cub[2] and self.obs1_cub[1]<=self.player_stading_cub[3]-10<=self.obs1_cub[3]-5:
            return False
        if self.obs2_cub[0]<=self.player_stading_cub[2]-10<=self.obs2_cub[2] and self.obs2_cub[1]<=self.player_stading_cub[3]-10<=self.obs2_cub[3]-5:
            return False

        return True



"""
///////////////////////////////////////////////////////////
   GAME ENGINE
///////////////////////////////////////////////////////////
"""
class Game(object):
    def __init__(self):
        self.player_sprite = player_w
        self.lock = False
        self.bg = (0, 150)
        self.bg1 = (600, 150)
        self.start = False
        self.jumping = False

    def process_events(self):
        for event in pg.event.get():
            #Quit game
            if event.type == pg.QUIT:
                return True

            #Press a key
            if event.type==pg.KEYDOWN:
                self.start = True
                if event.key == pg.K_SPACE:
                    if height >= 110: self.jumping = True
                return False

    def display_frame(self, screen, obstacles):
        print(self.start)
        global height
        player = self.player_sprite if type(self.player_sprite) != cycle else next(self.player_sprite)
        
        #Floor
        screen.blit(pg.image.fromstring(ground_w.tobytes(), ground_w.size, 'RGBA'), self.bg)
        screen.blit(pg.image.fromstring(ground_w.tobytes(), ground_w.size, 'RGBA'), self.bg1)
        
        #Jump
        if self.jumping:
            if height >= 110-100:
                height -= 3
            if height <= 110-100:
                self.jumping = False
        if height < 110 and not self.jumping:
            height += 3
        player = screen.blit(pg.image.fromstring(player.tobytes(), player.size, 'RGBA'), (5,height))
        
        obstacles.update_items(screen)
        
        if height > 110:
            self.start=True
        if self.start:
            # if not self.lock:
            #     self.bg = (self.bg[0]-speed, self.bg[1])
            #     if self.bg[0]<=-(600):
            #         lock = 1
            # if -self.bg[0]>=600 and self.lock:
            #     self.bg1 = (self.bg1[0]-speed, self.bg1[1])
            #     self.bg = (self.bg[0]-speed, self.bg[1])
            #     if -self.bg1[0]>=600:self.bg = (600,150)
            # if -self.bg1[0]>=600 and self.lock:
            #     self.bg = (self.bg[0]-speed, self.bg1[1])
            #     self.bg1 = (self.bg1[0]-speed, self.bg1[1])
            #     if -self.bg[0]>=600:self.bg1 = (600,150)
            self.player_sprite = player_w
            self.start = obstacles.display_obstacle()
        else:
            self.player_sprite = player_b

class Menu():
    def __init__(self, screen):
        self.screen = screen
        # self.back_btn = Button(back,back_glow,(0,0),(50,50),"Back")
        # self.input_box1 = InputBox(100, 100, 140, 32)
        # self.input_boxes = []

        # self.input_boxes.append(self.input_box1)
        pg.display.set_caption('Stranger Ducks')

        #Launch app
        self.game_runtime()


    def process_events(self,button_list):
        pos = pg.mouse.get_pos()

        for event in pg.event.get():
            #Quit game
            if event.type == pg.QUIT:
                pg.mixer.music.stop()
                return True
            
            #Click on screen
            #(Button implementation)
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in button_list:
                    if button.isOver(pos):
                        self.menu_open(button)
            
            #Hover effects trigger
            if event.type == pg.MOUSEMOTION:
                for button in button_list:
                    if button.isOver(pos):
                        button.hover_effects()
            
            #Input boxes
            for box in self.input_boxes:
                box.handle_event(event)


    def main_menu(self):
        done = False

        button_list = []

        button_list.append(Button(play, play_glow, (-15,100),(200,100),'Play'))
        button_list.append(Button(leaderboard, leaderboard_glow, (0,200),(350,80),'Leaderboard'))
        button_list.append(Button(howtoplay, howtoplay_glow, (0,280),(300,65),'How to Play'))
        button_list.append(Button(options, options_glow, (0,350),(200,65),'Options'))
        button_list.append(Button(cred, cred_glow, (440,530),(150,80),'Credits'))

        while not done:
            done = self.process_events(button_list)
            
            #Display elements
            self.screen.fill(WHITE)
            #self.screen.blit(main_menu_bg,(0,0))
            for button in button_list:
                button.draw(self.screen)

            pg.display.flip()
    

    def game_runtime(self):
        clock = pg.time.Clock()
        done = False
        game = Game()
        obstacles = ObstacleManager()
        #items = ItemManager()

        while not done:
            done = game.process_events()
            self.screen.fill(WHITE)
            game.display_frame(self.screen, obstacles)
            pg.display.flip()
            clock.tick(FPS)

    def howtoplay(self):
        done = False

        button_list = []
        
        button_list.append(self.back_btn)

        while not done:
            done = self.process_events(button_list) #or back_btn_Pressed()

            #Display elements
            self.screen.fill(BLACK)
            #self.screen.blit(credits_bg,(0,0))
            for button in button_list:
                button.draw(self.screen)

            pg.display.flip()

    def options(self):
        done = False

        button_list = []
        
        button_list.append(self.back_btn)

        while not done:
            done = self.process_events(button_list) #or back_btn_Pressed()

            #Display elements
            self.screen.fill(BLACK)
            #self.screen.blit(credits_bg,(0,0))
            for button in button_list:
                button.draw(self.screen)

            pg.display.flip()

    def credits(self):
        done = False

        button_list = []
        
        button_list.append(self.back_btn)

        while not done:
            done = self.process_events(button_list) #or back_btn_Pressed()

            #Display elements
            self.screen.fill(BLACK)
            #self.screen.blit(credits_bg,(0,0))
            for button in button_list:
                button.draw(self.screen)

            pg.display.flip()
    
    def game_over(self):
        done = False
        player_name = ""

        button_list = []
        
        button_list.append(self.back_btn)

        while not done:
            done = self.process_events(button_list)# or back_btn_Pressed()

            #Display elements
            self.screen.fill(WHITE)
            #self.screen.blit(credits_bg,(0,0))
            for button in button_list:
                button.draw(self.screen)
            for box in self.input_boxes:
                    box.update()

            for box in self.input_boxes:
                box.draw(self.screen)
                player_name = box.text

            message_to_screen(self.screen,"GAME OVER",BLACK,(300,50),80)
            #message_to_screen(self.screen,"SCORE: " + str(SCORE),WHITE,(300,500),80)

            pg.display.flip()

        
        return player_name

    def menu_open(self,button):
        callback = button.callback
        if callback == 'Play':
            self.game_runtime()
        elif callback == 'Leaderboard':
            self.leaderboard()
        elif callback == 'How to Play':
            self.howtoplay()
        elif callback == 'Options':
            self.options()
        elif callback == 'Credits':
            self.credits()
        elif callback == 'Back':
            self.main_menu()


"""
///////////////////////////////////////////////////////////
   RUN
///////////////////////////////////////////////////////////
"""

def main():
    pg.init()

    screen = pg.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

    Menu(screen)

    pg.quit()


if __name__ == "__main__":
	main()
