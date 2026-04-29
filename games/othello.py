import pygame
import sys
import numpy as np
from game import Game

class Othello(Game):
    # Initialize 8x8 board and set starting pieces in the center
    def __init__(self):
        super().__init__()
        self.board = np.zeros((8,8), dtype = int)
        self.board[3][3] = 2 #white
        self.board[3][4] = 1 #black
        self.board[4][3] = 1 #black
        self.board[4][4] = 2 #white
        self.font = pygame.font.SysFont("Arial", 30)

    def turn(self):
        for i in range(64):
            if self.rect[i].collidepoint(pygame.mouse.get_pos()):
                r = i//8
                c = i%8
                #check if the cell is empty and the move results in a flip
                if self.board[r][c] == 0:
                    if self.valid_flip(r, c, self.player, False):
                        self.board[r][c] = self.player
                        self.valid_flip(r, c, self.player, True) #flips
                        self.player = 3 - self.player #switch turns
                        #if next player has no moves, skip their turn
                        if not self.any_valid(self.player):
                            self.player = 3 - self.player
    
    def valid_flip(self, r, c, p, flip):
        valid = False
        opp = 3 - p
        #checks and then flips in all 8 directions (horizontal, vertical, diagonal)
        #vertical-down check
        if r+1 < 8 and self.board[r+1][c] == opp:
            for i in range(r+2, 8):
                if self.board[i][c] == 0: break
                if self.board[i][c] == p: 
                    if flip:
                        for j in range(r+1,i):
                            self.board[j][c] = p
                    valid = True
                    break
        #manual checks for vertical-up, horizontal-right, and horizontal-left
        if r-1 >= 0 and self.board[r-1][c] == opp:
            for i in range(r-2, -1, -1):
                if self.board[i][c] == 0: break
                if self.board[i][c] == p: 
                    if flip:
                        for j in range(r-1,i,-1):
                            self.board[j][c] = p
                    valid = True
                    break

        if c+1 < 8 and self.board[r][c+1] == opp:
            for i in range(c+2, 8):
                if self.board[r][i] == 0: break
                if self.board[r][i] == p: 
                    if flip:
                        for j in range(c+1,i):
                            self.board[r][j] = p
                    valid = True
                    break
        if c-1 >= 0 and self.board[r][c-1] == opp:
            for i in range(c-2, -1, -1):
                if self.board[r][i] == 0: break
                if self.board[r][i] == p: 
                    if flip:
                        for j in range(c-1,i,-1):
                            self.board[r][j] = p
                    valid = True
                    break
        #diagonal checks: down-right, up-left, down-left, up-right      
        if r+1 < 8 and c+1 < 8 and self.board[r+1][c+1] == opp:
            for i in range(2, min(8-r, 8-c)):
                if self.board[r+i][c+i] == 0: break
                if self.board[r+i][c+i] == p:
                    if flip: 
                        for j in range(1,i):
                            self.board[r+j][c+j] = p
                    valid = True
                    break
        if r-1 >= 0 and c-1 >= 0 and self.board[r-1][c-1] == opp:
            for i in range(2, min(r+1, c+1)):
                if self.board[r-i][c-i] == 0: break
                if self.board[r-i][c-i] == p: 
                    if flip:
                        for j in range(1,i):
                            self.board[r-j][c-j] = p
                    valid = True
                    break
                
        if r+1 < 8 and c-1 >= 0 and self.board[r+1][c-1] == opp:
            for i in range(2, min(8-r, c+1)):
                if self.board[r+i][c-i] == 0: break
                if self.board[r+i][c-i] == p: 
                    if flip:
                        for j in range(1,i):
                            self.board[r+j][c-j] = p
                    valid = True
                    break
        if r-1 >= 0 and c+1 < 8 and self.board[r-1][c+1] == opp:
            for i in range(2, min(r+1, 8-c)):
                if self.board[r-i][c+i] == 0: break
                if self.board[r-i][c+i] == p: 
                    if flip:
                        for j in range(1,i):
                            self.board[r-j][c+j] = p
                    valid = True
                    break
        return valid
    
    def any_valid(self, p):
        #checks if the given player has any valid moves left on the board.
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 0:
                    if self.valid_flip(i, j, p, False):
                        return True
        return False

    def win(self):
        #determines if the game is over and calculates the winner based on coin count.
        if np.all(self.board != 0) or (not self.any_valid(1) and not self.any_valid(2)):
            num_bla = np.sum(self.board == 1)
            num_whi = np.sum(self.board == 2)

            if num_bla > num_whi:
                self.screen.blit(self.black_win, (173,140))
                #displaying stats UI and counts for black coin
                self.screen.blit(self.stats, (5, 5))
                self.screen.blit(self.banner, (242,476))
                text_1 = f"= {num_bla}"
                text_2 = f"= {num_whi}"   
                text_surface1 = self.font.render(text_1, True, (0, 0, 0))
                text_surface2= self.font.render(text_2, True, (0, 0, 0))
                self.screen.blit(text_surface1, (391, 580))                
                self.screen.blit(text_surface2, (391, 620))
                self.screen.blit(self.black_small, (331,570))
                self.screen.blit(self.white_small, (331,615))
                return 1
            elif num_bla < num_whi:
                self.screen.blit(self.white_win, (173,140))
                #displaying stats UI and counts for white coin
                self.screen.blit(self.stats, (5, 5))
                self.screen.blit(self.banner, (242,476))
                text_2 = f"= {num_bla}"
                text_1 = f"= {num_whi}"   
                text_surface1 = self.font.render(text_1, True, (0, 0, 0))
                text_surface2= self.font.render(text_2, True, (0, 0, 0))
                self.screen.blit(text_surface1, (391, 580))                
                self.screen.blit(text_surface2, (391, 620))
                self.screen.blit(self.white_small, (331,570))
                self.screen.blit(self.black_small, (331,615))
                return 2
            else:
                self.screen.blit(self.stats, (5, 5))
                return 0 #draw
        return -1
    
    def draw_turn_text(self):
        #displays whose turn it is in the corner of the screen.
        if self.win() == -1:
            if self.player == 1 :
                self.screen.blit(self.black_turn, (-5,-5))
            if self.player == 2 :
                self.screen.blit(self.white_turn, (-5,-6))

    def run(self):
        #main game loop and variables management.
        self.initialisation("Othello")
        self.font = pygame.font.SysFont("palatinolinotype", 40)
        #load and scale images
        self.bg = pygame.image.load(str("Ref_Images/Oth_bg.png")).convert()
        self.bg = pygame.transform.scale(self.bg, self.screen.get_size())
        self.black = pygame.image.load(str("Ref_Images/Oth_Black.png")).convert_alpha()
        self.black = pygame.transform.scale(self.black, (60,60))
        self.black_small = pygame.transform.scale(self.black, (45,45))
        self.white = pygame.image.load(str("Ref_Images/Oth_White.png")).convert_alpha()
        self.white = pygame.transform.scale(self.white, (60,60))
        self.white_small = pygame.transform.scale(self.white, (45,45))
        self.bg1 = pygame.image.load(str("Ref_Images/Oth_cutout.png")).convert_alpha()
        self.bg1 = pygame.transform.scale(self.bg1, (535,400))
        self.black_turn = pygame.image.load(str("Ref_Images/black_turn.png")).convert_alpha()
        self.black_turn = pygame.transform.scale(self.black_turn, (248, 233))
        self.white_turn = pygame.image.load(str("Ref_Images/white_turn.png")).convert_alpha()
        self.white_turn = pygame.transform.scale(self.white_turn, (248, 233))
        self.black_win = pygame.image.load(str("Ref_Images/black_win.png")).convert_alpha()
        self.black_win = pygame.transform.scale(self.black_win, (450,484))
        self.white_win = pygame.image.load(str("Ref_Images/white_win.png")).convert_alpha()
        self.white_win = pygame.transform.scale(self.white_win, (450,484)) 
        self.stats = pygame.image.load(str("Ref_Images/stats.png")).convert_alpha()
        self.stats = pygame.transform.scale(self.stats, (290, 180))
        self.banner = pygame.image.load(str("Ref_Images/banner3.png")).convert_alpha()
        self.banner = pygame.transform.scale(self.banner, (330, 320))
        self.replay_rect = pygame.Rect(345, 470, 70, 70)
        self.home_rect = pygame.Rect(405, 470, 70, 70)
        self.music = pygame.image.load(str("Ref_Images/music.png")).convert_alpha()
        self.music = pygame.transform.scale(self.music, (500, 340))
        self.off_music = pygame.image.load(str("Ref_Images/off_music.png")).convert_alpha()
        self.off_music = pygame.transform.scale(self.off_music, (500, 340))
        self.music_rect = pygame.Rect(723, -0.5, 70, 70)
        self.stats_rect = pygame.Rect(5, 5, 235, 146)
        #generate board grid rectangles
        self.rect = []
        music_on = True
        for i in range(8):
            for j in range(8):
                self.rect.append(pygame.Rect(120 + 70.75*j, 145 + 65.5*i, 64.75, 61))

        while True:
            self.screen.blit(self.bg, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #toggle music
                    if self.music_rect.collidepoint(pygame.mouse.get_pos()):
                        if music_on == True:
                            pygame.mixer.music.pause()  
                            music_on = False
                        else:
                            pygame.mixer.music.unpause()
                            music_on = True
                    #gameplay or return to stats
                    if self.win() == -1:
                        self.turn()
                    if self.win() ==1 or self.win() ==2 or self.win() ==0:
                        if self.stats_rect.collidepoint(pygame.mouse.get_pos()):
                            return self.win()
           
            self.screen.blit(self.bg, (0,0))
            #displaying board state
            for i in range(64):
                if self.board[i//8][i%8] == 1:
                    self.screen.blit(self.black, self.rect[i])
                elif self.board[i//8][i%8] == 2:
                    self.screen.blit(self.white, self.rect[i])
            #some more interface images
            self.screen.blit(self.bg1, (275,-40))
            self.draw_turn_text()
            if music_on:
                self.screen.blit(self.music, (725, 0))
            else:
                self.screen.blit(self.off_music, (727, 1.5))
            pygame.display.update()
            
