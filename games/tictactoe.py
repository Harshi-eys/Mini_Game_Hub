import pygame
import sys
import numpy as np
from game import Game

class TicTacToe(Game):
    def __init__(self):
        super().__init__()
        # Initialize 10x10 board with zeros
        self.board = np.zeros((10,10), dtype = int)

    def turn(self):
        # player move based on mouse click collision with grid rectangles.
        for i in range(100):
            if self.rect[i].collidepoint(pygame.mouse.get_pos()):
                r = i//10
                c = i%10
                if self.board[r][c] == 0:
                    if self.player == 1:
                        self.board[r][c] = 1
                        self.player = 2
                    else:
                        self.board[r][c] = 2
                        self.player = 1

    def win(self):
        # Check for 5 coins in-a-row using NumPy slicing.
        b = self.board
        p = 3 - self.player # The player who moved at the last turn 
        # horizontal check
        if np.any((b[:,:-4] == p) & (b[:,1:-3] == p) & (b[:,2:-2] == p) & (b[:,3:-1] == p) & (b[:,4:] == p) ):
            return p
        # vertical check
        elif np.any((b[:-4,:] == p) & (b[1:-3,:] == p) & (b[2:-2,:] == p) & (b[3:-1,:] == p) & (b[4:,:] == p) ):
            return p 
        # main diagonal check
        elif np.any((b[:-4,:-4] == p) & (b[1:-3,1:-3] == p) & (b[2:-2,2:-2] == p) & (b[3:-1,3:-1] == p) & (b[4:,4:] == p) ):
            return p
        # anti-diagonal check
        elif np.any((b[4:,:-4] == p) & (b[3:-1,1:-3] == p) & (b[2:-2,2:-2] == p) & (b[1:-3,3:-1] == p) & (b[:-4,4:] == p) ):
            return p   
        else:
            return 0

    def draw_turn_text(self):
        # Display the current player's turn on the top banner.
        if self.win() == 0 :
            name = "X" if self.player == 1 else "O"
            text_content = f"{name}'s turn"   
            banner_rect = self.banner.get_rect(topleft=(275, -100))
            self.screen.blit(self.banner, banner_rect)
            text_surface = self.font.render(text_content, True, (0, 0, 0))
            self.screen.blit(text_surface, (334, 16))    

    def run(self):
        self.initialisation("Tic Tac Toe")
        # specified font used on banner
        self.font = pygame.font.SysFont("palatinolinotype", 40)
        # load and scale the images used in the game
        self.bg = pygame.image.load(str("Ref_Images/TTT_bg.png")).convert()
        self.bg = pygame.transform.scale(self.bg, self.screen.get_size())
        self.X = pygame.image.load(str("Ref_Images/TTT_X.png")).convert_alpha()
        self.X = pygame.transform.scale(self.X, (55, 55))
        self.O = pygame.image.load(str("Ref_Images/TTT_O.png")).convert_alpha()
        self.O = pygame.transform.scale(self.O, (55, 55))
        self.banner = pygame.image.load(str("Ref_Images/banner2.png")).convert_alpha()
        self.banner = pygame.transform.scale(self.banner, (250, 250))
        self.x_win = pygame.image.load(str("Ref_Images/x_win.png")).convert_alpha()
        self.x_win = pygame.transform.scale(self.x_win, (450, 485))
        self.o_win = pygame.image.load(str("Ref_Images/o_win.png")).convert_alpha()
        self.o_win = pygame.transform.scale(self.o_win, (450, 485))
        self.stats = pygame.image.load(str("Ref_Images/stats.png")).convert_alpha()
        self.stats = pygame.transform.scale(self.stats, (290, 180))
        self.music = pygame.image.load(str("Ref_Images/music.png")).convert_alpha()
        self.music = pygame.transform.scale(self.music, (500, 340))
        self.off_music = pygame.image.load(str("Ref_Images/off_music.png")).convert_alpha()
        self.off_music = pygame.transform.scale(self.off_music, (500, 340))
        # define rectangles for UI click areas
        self.music_rect = pygame.Rect(723, -0.5, 70, 70)
        self.stats_rect = pygame.Rect(283, 600, 235, 146)
        music_on = True
        # generate the 10x10 grid of rectangles
        self.rect =[]
        for i in range(10):
            for j in range(10):
                self.rect.append(pygame.Rect(70 + 68*j, 70 + 68*i, 55, 55))

        while True:
            self.screen.blit(self.bg, (0,0))
            # handling the event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # toggling the music switch
                    if self.music_rect.collidepoint(pygame.mouse.get_pos()):
                        if music_on == True:
                            pygame.mixer.music.pause()  
                            music_on = False
                        else:
                            pygame.mixer.music.unpause()
                            music_on = True
                    if self.win() == 0:
                        self.turn()
                    else: # shows the statistics when clicked
                        if self.stats_rect.collidepoint(pygame.mouse.get_pos()):
                            return self.win()
                        
            self.screen.blit(self.bg, (0,0))
            # defining board pieces
            for i in range(100):
                if self.board[i//10][i%10] == 1:
                    self.screen.blit(self.X, self.rect[i])
                elif self.board[i//10][i%10] == 2:
                    self.screen.blit(self.O, self.rect[i])
            
            self.draw_turn_text()
            #changes the music icon
            if music_on:
                self.screen.blit(self.music, (725, 0))
            else:
                self.screen.blit(self.off_music, (727, 1.5))
            #display of winner banner
            if self.win() !=0 :
                if self.player == 2 :       
                    self.screen.blit(self.x_win, (199,140))
                else:
                    self.screen.blit(self.o_win, (199,140))
                self.screen.blit(self.stats, (283,600))
            pygame.display.update()

