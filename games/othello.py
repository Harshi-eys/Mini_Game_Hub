import pygame
import sys
import numpy as np
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Othello')

Hub = Path(__file__).resolve().parent.parent
bg = pygame.image.load(str(Hub / "Ref_Images/Oth_bg.png")).convert()
bg = pygame.transform.scale(bg, screen.get_size())
black = pygame.image.load(str(Hub / "Ref_Images/Oth_Black.png")).convert_alpha()
black = pygame.transform.scale(black, (60,60))
white = pygame.image.load(str(Hub / "Ref_Images/Oth_White.png")).convert_alpha()
white = pygame.transform.scale(white, (60,60))
bg1 = pygame.image.load(str(Hub / "Ref_Images/Oth_cutout.png")).convert_alpha()
bg1 = pygame.transform.scale(bg1, (535,400)) 

rect = []
for i in range(8):
    for j in range(8):
        rect.append(pygame.Rect(120 + 70.75*j, 145 + 65.5*i, 64.75, 61))

class Game:
    def __init__(self):
        self.board = np.zeros((8,8), dtype = int)
        self.player = 1
        self.board[3][3] = 2
        self.board[3][4] = 1
        self.board[4][3] = 1
        self.board[4][4] = 2

    def turn(self):
        for i in range(64):
            if rect[i].collidepoint(pygame.mouse.get_pos()):
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
                return 1
            elif num_bla < num_whi:
                return 2
            else:
                return 0
        return -1

game = Game()
while True:
    screen.fill('Black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.win() == -1:
                game.turn()
                if game.win() != -1:
                    print(game.win())
                    break
            else:
                print(game.win())
                break
    
    screen.blit(bg, (0,0))
    for i in range(64):
        if game.board[i//8][i%8] == 1:
            screen.blit(black, rect[i])
        elif game.board[i//8][i%8] == 2:
            screen.blit(white, rect[i])
    screen.blit(bg1, (275,-40))
    pygame.display.update()
    