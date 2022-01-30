from random import randrange as rnd
from itertools import cycle
from random import choice
import pygame as pg
import time
from resources import *
#from tools import *

pg.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60
speed = 4

"""
///////////////////////////////////////////////////////////
   QUANTUM ENGINE
///////////////////////////////////////////////////////////
"""
class Obstacle():
    def __init__(self):
        self.obstacles = [obstacle1, obstacle2, obstacle3, obstacle4, obstacle5, obstacle6]
        self.obs1 = (rnd(600, 600+500), 130)
        self.obs2 = (rnd(600+100+500, 1200+500), 130)
        self.obs3 = (rnd(1700, 2000), 130)

    def get_asset(self):
        obast1 = choice(self.obstacles)
        if obast1 in [obstacle4, obstacle5, obstacle6]:obs1 = (self.obs1[0], 115)
        obast2 = choice(self.obstacles)
        if obast2 in [obstacle4, obstacle5, obstacle6]:obs2 = (self.obs2[0], 115)
        obast3 = choice(self.obstacles)
        if obast3 in [obstacle4, obstacle5, obstacle6]:obs3 = (self.obs3[0], 115)

"""
///////////////////////////////////////////////////////////
   GAME ENGINE
///////////////////////////////////////////////////////////
"""
class Game(object):
    def __init__(self):
        speed_identifier = lambda x: 2 if x >= 30 else 8 if x < 8 else 5
        cust_speed = speed_identifier(speed)
        self.running = cycle([player_frame_3]*cust_speed+[player_frame_31]*cust_speed)
        self.crouch = cycle([player_frame_5]*cust_speed+ [player_frame_6]*cust_speed)
        self.crouch_scope = [player_frame_5]+[player_frame_6]

        gameDisplay = pg.display.set_mode((600,200))
        pg.display.set_caption('Stranger Ducks')
        clock = pg.time.Clock()
        state = player_frame_1
        crashed = False
        lock = False
        bg = (0, 150)
        bg1 = (600,150)
        self.start = False
        self.height = 110
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
                    if self.height >= 110: self.jumping = True        

class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.back_btn = Button(back,back_glow,(0,0),(50,50),"Back")
        self.input_box1 = InputBox(100, 100, 140, 32)
        self.input_boxes = []

        self.input_boxes.append(self.input_box1)

        #Launch app
        self.main_menu()


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
            self.screen.fill(BLUE)
            self.screen.blit(main_menu_bg,(0,0))
            for button in button_list:
                button.draw(self.screen)

            pg.display.flip()
    

    def game_runtime(self):
        while not crashed:
        gameDisplay.fill((246,246,246))
        player = state if type(state) != cycle else next(state)
        #Background
        gameDisplay.blit(pg.image.fromstring(ground.tobytes(), ground.size, 'RGBA'), bg)
        gameDisplay.blit(pg.image.fromstring(ground.tobytes(), ground.size, 'RGBA'), bg1)
        
        #Jump
        if jumping:
            if height>=110-100:
                height -= 4
            if height <= 110-100:
                jumping = False
        if height<110 and not jumping:
            if slow_motion == True:
                height += 1.5
            else:height += 3
        player = gameDisplay.blit(pg.image.fromstring(player.tobytes(), player.size, 'RGBA'), (5,height))
        gameDisplay.blit(pg.image.fromstring(obast1.tobytes(), obast1.size, 'RGBA'), obs1)
        gameDisplay.blit(pg.image.fromstring(obast2.tobytes(), obast2.size, 'RGBA'), obs2)
        gameDisplay.blit(pg.image.fromstring(obast3.tobytes(), obast3.size, 'RGBA'), obs3)
        if obs1[0]<=-50:
            obs1 = (rnd(600, 600+500), 130)
            obast1 = choice(obstacles)
            if obast1 in [obstacle4, obstacle5, obstacle6]:obs1 = (obs1[0], 115)
        if obs2[0]<=-50:
            obs2 = (rnd(600+100+500, 1200+500), 130)
            obast2 = choice(obstacles)
            if obast2 in [obstacle4, obstacle5, obstacle6]:obs2 = (obs2[0], 115)
        if obs3[0]<=-50:
            obs3 = (rnd(1700, 2000), 130) 
            obast3 = choice(obstacles) 
            if obast3 in [obstacle4, obstacle5, obstacle6]:obs3 = (obs3[0], 115)
        player_stading_cub = (5, height, 5+43, height+46)
        if height< 100:
            start=True
        if start:
            obs1 = (obs1[0]-speed, obs1[1])
            obs2 = (obs2[0]-speed, obs2[1])
            obs3 = (obs3[0]-speed, obs3[1])
            obs1_cub = (obs1[0], obs1[1], obs1[0]+obast1.size[0],obs1[1]+obast1.size[1])
            obs2_cub = (obs2[0], obs2[1], obs2[0]+obast2.size[0],obs2[1]+obast2.size[1])
            obs3_cub = (obs3[0], obs3[1], obs3[0]+obast3.size[0],obs3[1]+obast3.size[1])
            if not lock:
                bg = (bg[0]-speed, bg[1])
                if bg[0]<=-(600):
                    lock = 1
            if -bg[0]>=600 and lock:
                bg1 = (bg1[0]-speed, bg1[1])
                bg = (bg[0]-speed, bg[1])
                if -bg1[0]>=600:bg = (600,150)
            if -bg1[0]>=600 and lock:
                bg = (bg[0]-speed, bg1[1])
                bg1 = (bg1[0]-speed, bg1[1])
                if -bg[0]>=600:bg1 = (600,150)

            if obs1_cub[0]<=player_stading_cub[2]-10<=obs1_cub[2] and obs1_cub[1]<=player_stading_cub[3]-10<=obs1_cub[3]-5:
                start=False
                state = player_frame_4
                crashed = True
            if obs2_cub[0]<=player_stading_cub[2]-10<=obs2_cub[2] and obs2_cub[1]<=player_stading_cub[3]-10<=obs2_cub[3]-5:
                start=False
                state = player_frame_4
                crashed = True
            if obs3_cub[0]<=player_stading_cub[2]-10<=obs3_cub[2] and obs3_cub[1]<=player_stading_cub[3]-10<=obs3_cub[3]-5:
                start=False
                state = player_frame_4
                crashed = True
        pg.display.update()
        clock.tick(120)

    def howtoplay(self):
        done = False

        button_list = []
        
        button_list.append(self.back_btn)

        while not done:
            done = self.process_events(button_list) #or back_btn_Pressed()

            #Display elements
            self.screen.fill(BLUE)
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
            self.screen.fill(RED)
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
            self.screen.fill(RED)
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

            message_to_screen(self.screen,"GAME OVER",RED,(300,50),80)
            message_to_screen(self.screen,"SCORE: " + str(SCORE),WHITE,(300,500),80)

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

"""
///////////////////////////////////////////////////////////
   RUN
///////////////////////////////////////////////////////////
"""
"""
def main():
    pg.init()

    screen = pg.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

    Game()

    pg.quit()


if __name__ == "__main__":
	main()

"""