import pygame
import sys
import numpy as np
from pathlib import Path
from game import Game

class TicTacToe(Game):
    def __init__(self):
        super().__init__()
        self.board = np.zeros((10,10), dtype = int)

    def turn(self):
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
        b = self.board
        p = 3 - self.player
        
        if np.any((b[:,:-4] == p) & (b[:,1:-3] == p) & (b[:,2:-2] == p) & (b[:,3:-1] == p) & (b[:,4:] == p) ):
            return p
        elif np.any((b[:-4,:] == p) & (b[1:-3,:] == p) & (b[2:-2,:] == p) & (b[3:-1,:] == p) & (b[4:,:] == p) ):
            return p 
        elif np.any((b[:-4,:-4] == p) & (b[1:-3,1:-3] == p) & (b[2:-2,2:-2] == p) & (b[3:-1,3:-1] == p) & (b[4:,4:] == p) ):
            return p
        elif np.any((b[4:,:-4] == p) & (b[3:-1,1:-3] == p) & (b[2:-2,2:-2] == p) & (b[1:-3,3:-1] == p) & (b[:-4,4:] == p) ):
            return p   
        else:
            return 0

    def run(self):
        self.initialisation("Tic Tac Toe")
        self.bg = pygame.image.load(str("Ref_Images/TTT_bg.png")).convert()
        self.bg = pygame.transform.scale(self.bg, self.screen.get_size())
        self.X = pygame.image.load(str("Ref_Images/TTT_X.png")).convert_alpha()
        self.X = pygame.transform.scale(self.X, (55, 55))
        self.O = pygame.image.load(str("Ref_Images/TTT_O.png")).convert_alpha()
        self.O = pygame.transform.scale(self.O, (55, 55))
        self.rect =[]
        for i in range(10):
            for j in range(10):
                self.rect.append(pygame.Rect(70 + 68*j, 70 + 68*i, 55, 55))

        while True:
            self.screen.blit(self.bg, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.win() == 0:
                        self.turn()
                        if self.win() != 0:
                            return self.win()

            self.screen.blit(self.bg, (0,0))
            for i in range(100):
                if self.board[i//10][i%10] == 1:
                    self.screen.blit(self.X, self.rect[i])
                elif self.board[i//10][i%10] == 2:
                    self.screen.blit(self.O, self.rect[i])
            pygame.display.update()