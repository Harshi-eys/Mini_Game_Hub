import pygame
import sys
import numpy as np
from game import Game

class Othello(Game):
    def __init__(self):
        super().__init__()
        self.board = np.zeros((8,8), dtype = int)
        self.board[3][3] = 2
        self.board[3][4] = 1
        self.board[4][3] = 1
        self.board[4][4] = 2
        self.font = pygame.font.SysFont("Arial", 30)

    def turn(self):
        for i in range(64):
            if self.rect[i].collidepoint(pygame.mouse.get_pos()):
                r = i//8
                c = i%8
                if self.board[r][c] == 0:
                    if self.valid_flip(r, c, self.player, False):
                        self.board[r][c] = self.player
                        self.valid_flip(r, c, self.player, True)
                        self.player = 3 - self.player

                        if not self.any_valid(self.player):
                            self.player = 3 - self.player
    
    def valid_flip(self, r, c, p, flip):
        valid = False
        opp = 3 - p
        if r+1 < 8 and self.board[r+1][c] == opp:
            for i in range(r+2, 8):
                if self.board[i][c] == 0: break
                if self.board[i][c] == p: 
                    if flip:
                        for j in range(r+1,i):
                            self.board[j][c] = p
                    valid = True
                    break
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
            for i in range(2, min(r, c)):
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
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 0:
                    if self.valid_flip(i, j, p, False):
                        return True
        return False

    def win(self):
        if np.all(self.board != 0) or (not self.any_valid(1) and not self.any_valid(2)):
            num_bla = np.sum(self.board == 1)
            num_whi = np.sum(self.board == 2)
            if num_bla > num_whi:
                self.screen.blit(self.black_win, (173,150))
                return 1
            elif num_bla < num_whi:
                self.screen.blit(self.white_win, (173,150))
                return 2
            else:
                # screen.blit(draw, (300,400))
                return 0
        return -1
    
    def draw_turn_text(self):
        if self.win() == -1:
            if self.player == 1 :
                self.screen.blit(self.black_turn, (-5,-5))
            if self.player == 2 :
                self.screen.blit(self.white_turn, (-5,-6))

    def run(self):
        self.initialisation("Othello")
        self.font = pygame.font.SysFont("palatinolinotype", 40)
        self.bg = pygame.image.load(str("Ref_Images/Oth_bg.png")).convert()
        self.bg = pygame.transform.scale(self.bg, self.screen.get_size())
        self.black = pygame.image.load(str("Ref_Images/Oth_Black.png")).convert_alpha()
        self.black = pygame.transform.scale(self.black, (60,60))
        self.white = pygame.image.load(str("Ref_Images/Oth_White.png")).convert_alpha()
        self.white = pygame.transform.scale(self.white, (60,60))
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
        # draw = pygame.image.load(str(Hub / "Ref_Images/draw.png")).convert_alpha()
        # draw = pygame.transform.scale(draw, (535,400))
        self.rect = []
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
                    if self.win() == -1:
                        self.turn()                      
            
            self.screen.blit(self.bg, (0,0))
            for i in range(64):
                if self.board[i//8][i%8] == 1:
                    self.screen.blit(self.black, self.rect[i])
                elif self.board[i//8][i%8] == 2:
                    self.screen.blit(self.white, self.rect[i])
            self.screen.blit(self.bg1, (275,-40))
            self.draw_turn_text()
            pygame.display.update()
            
