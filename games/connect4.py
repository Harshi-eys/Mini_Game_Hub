import pygame
import sys
import numpy as np
from game import Game

class Connect4(Game) :
    def __init__(self):
        super().__init__()
        # Initialize 7x7 board and animation variables
        self.board = np.zeros((7,7), dtype = int)
        self.x = self.yf = 0
        self.y = -55
        self.coin = None
        self.falling = False
        self.turn_i = None
        self.turn_j = None

    def turn(self):
        # Finding the lowest empty row in a column and displaying the fall animation accordingly.
        if self.falling:
            return
        self.draw_turn_text()
        for i in range(7):
            if self.rect[i].collidepoint(pygame.mouse.get_pos()):
                # Scanning from bottom to top to find the first empty cell for the coin
                for j in range(6, -1, -1):
                    if self.board[i][j] == 0:
                        # set coordinates for start and end of fall
                        self.x = 156 + 75.5*i
                        self.y = -55
                        self.yf = 158 + 64*j
                        self.falling = True
                        self.turn_i = i
                        self.turn_j = j
                        # Assign coin values and swap players
                        if self.player == 1:
                            self.last_player = 1
                            self.player = 2
                            self.coin = self.pl1
                            break

                        else:
                            self.last_player = 2
                            self.player = 1
                            self.coin = self.pl2
                            break
                return
            
       
        
    def win(self):
        # check for 4 coins in-a-row horizontally, vertically, or diagonally.
        b = self.board
        p = self.last_player

        if p is None:
            return 0
        #horizontal check
        if np.any((b[: ,:-3]==p) & (b[: ,1:-2]==p) & (b[: ,2:-1]==p) & (b[: ,3:]==p)): 
            return p  
        #vertical check      
        elif np.any((b[:-3, :]==p) & (b[1:-2, :]==p) & (b[2:-1, :]==p) & (b[3: , :]==p)):
            return p 
        #main diagonal check       
        elif np.any((b[:-3, :-3]==p) & (b[1:-2, 1:-2]==p) & (b[2:-1, 2:-1]==p) & (b[3:, 3:]==p)):
            return p   
        #anti_diagonal check     
        elif np.any((b[3:, :-3]==p) & (b[2:-1, 1:-2]==p) & (b[1:-2, 2:-1]==p) & (b[:-3, 3:]==p)):
            return p
        else:
            return 0
        
    def draw_turn_text(self):
        #display the current turn status on the banner.
        if self.win() == 0 :
            name = "Red" if self.player == 1 else "Blue"
            text_content = f"{name}'s turn"   
            banner_rect = self.banner.get_rect(topleft=(235, 410))
            self.screen.blit(self.banner, banner_rect)
            #using player-specific colors for text
            if name == "Red" :
                text_surface = self.font.render(text_content, True, (160, 0, 0))
            else:
                text_surface = self.font.render(text_content, True, (24, 41, 88))
            self.screen.blit(text_surface, (310,710))              

    def run(self):
        self.initialisation("Connect4")
        self.font = pygame.font.SysFont("palatinolinotype", 40)
        #load and scale game pieces, background, and other reference images
        self.pl1 = pygame.image.load(str("Ref_Images/C4_Red.png")).convert_alpha()
        self.pl1 = pygame.transform.scale(self.pl1, (51, 55))
        self.pl2 = pygame.image.load(str("Ref_Images/C4_Blue.png")).convert_alpha()
        self.pl2 = pygame.transform.scale(self.pl2, (51, 55))
        self.bgi = pygame.image.load(str("Ref_Images/C4_bg.png")).convert()
        self.bgi = pygame.transform.scale(self.bgi, self.screen.get_size())
        self.bgi1 = pygame.image.load(str("Ref_Images/C4_bg_cutout.png")).convert_alpha()
        self.bgi1 = pygame.transform.scale(self.bgi1, self.screen.get_size())
        self.banner = pygame.image.load(str("Ref_Images/banner1.png")).convert_alpha()
        self.banner = pygame.transform.scale(self.banner, (350, 701))
        self.red_win = pygame.image.load(str("Ref_Images/red_win.png")).convert_alpha()
        self.red_win = pygame.transform.scale(self.red_win, (390, 437))
        self.blue_win = pygame.image.load(str("Ref_Images/blue_win.png")).convert_alpha()
        self.blue_win = pygame.transform.scale(self.blue_win, (390, 437))
        self.stats = pygame.image.load(str("Ref_Images/stats.png")).convert_alpha()
        self.stats = pygame.transform.scale(self.stats, (290, 180))
        self.dragon = pygame.image.load(str("Ref_Images/green_dragon.png")).convert_alpha()
        self.dragon = pygame.transform.scale(self.dragon, (220, 220))
        self.girl = pygame.image.load(str("Ref_Images/warrior_girl1.png")).convert_alpha()
        self.girl = pygame.transform.scale(self.girl, (95, 167))
        self.music = pygame.image.load(str("Ref_Images/music.png")).convert_alpha()
        self.music = pygame.transform.scale(self.music, (500, 340))
        self.off_music = pygame.image.load(str("Ref_Images/off_music.png")).convert_alpha()
        self.off_music = pygame.transform.scale(self.off_music, (500, 340))
        self.music_rect = pygame.Rect(723, -0.5, 70, 70)
        self.stats_rect = pygame.Rect(293, 550, 235, 146)
        self.home = pygame.image.load(str("Ref_Images/home.png"))
        self.home = pygame.transform.scale(self.home, (500, 340))
        self.home_rect = pygame.Rect(650, -0.5, 70, 70)
        #create rectangles for column selection
        self.rect = []
        music_on = True
        for i in range(7):
            self.rect.append(pygame.Rect(156 + 76*i, 155, 52, 440))

        clock = pygame.time.Clock()

        while True:
            self.screen.blit(self.bgi, (0,0))
            #handle coin drop animation
            if self.falling:
                self.y += 7.5
                if self.y >= self.yf:
                    self.y = self.yf
                    self.falling = False
                    self.board[self.turn_i][self.turn_j] = self.last_player
                    self.turn_i = None
                    self.turn_j = None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #audio control
                    if self.music_rect.collidepoint(pygame.mouse.get_pos()):
                        if music_on == True:
                            pygame.mixer.music.pause()  
                            music_on = False
                        else:
                            pygame.mixer.music.unpause()
                            music_on = True
                    if self.win() == 0 :
                        self.turn()
                    if self.home_rect.collidepoint(pygame.mouse.get_pos()):
                        return None

            #Draw background and current animated coin
            self.screen.blit(self.bgi, (0,0))
            if self.falling:
                self.screen.blit(self.coin, (self.x, self.y))
            #draw placed pieces
            for i in range(7):
                for j in range(7):
                    if self.board[i][j] == 1 :
                        self.screen.blit(self.pl1, (156 + 75.5*i, 158 + 64*j))
                    elif self.board[i][j] == 2 :
                        self.screen.blit(self.pl2, (156 + 75.5*i, 158 + 64*j))
            #Foreground elements display
            self.screen.blit(self.bgi1, (0,0))
            self.draw_turn_text()
            self.screen.blit(self.bgi1, (0,0))
            #music icon toggle 
            if music_on:
                self.screen.blit(self.music, (725, 0))
            else:
                self.screen.blit(self.off_music, (727, 1.5))
            
            self.screen.blit(self.dragon, (551,445))
            self.screen.blit(self.girl, (425,530))

            if self.win() != 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.stats_rect.collidepoint(pygame.mouse.get_pos()):
                        return self.win()
                if self.last_player == 1 :       
                    self.screen.blit(self.red_win, (215,140))
                else:
                    self.screen.blit(self.blue_win, (215,140))
                self.screen.blit(self.stats, (293,550))
            
            self.screen.blit(self.home, (650,1.5))
            pygame.display.update()
            #setting 60 fps
            clock.tick(60)
