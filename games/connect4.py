import pygame
import sys
import numpy as np
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from game import Game

class Connect4(Game) :
    def __init__(self):
        super().__init__()
        self.board = np.zeros((7,7), dtype = int)
        self.x = self.yf = 0
        self.y = -55
        self.coin = None
        self.falling = False
        self.turn_i = None
        self.turn_j = None

    def turn(self):
        if self.falling:
            return
        for i in range(7):
            if self.rect[i].collidepoint(pygame.mouse.get_pos()):
                for j in range(6, -1, -1):
                    if self.board[i][j] == 0:
                        self.x = 156 + 75.5*i
                        self.y = -55
                        self.yf = 158 + 64*j
                        self.falling = True
                        self.turn_i = i
                        self.turn_j = j

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
        b = self.board
        p = self.last_player

        if p is None:
            return 0
        if np.any((b[: ,:-3]==p) & (b[: ,1:-2]==p) & (b[: ,2:-1]==p) & (b[: ,3:]==p)): 
            return p        
        elif np.any((b[:-3, :]==p) & (b[1:-2, :]==p) & (b[2:-1, :]==p) & (b[3: , :]==p)):
            return p        
        elif np.any((b[:-3, :-3]==p) & (b[1:-2, 1:-2]==p) & (b[2:-1, 2:-1]==p) & (b[3:, 3:]==p)):
            return p        
        elif np.any((b[3:, :-3]==p) & (b[2:-1, 1:-2]==p) & (b[1:-2, 2:-1]==p) & (b[:-3, 3:]==p)):
            return p
        else:
            return 0

    def run(self):
        self.initialisation("Connect4")
        self.pl1 = pygame.image.load(str("Ref_Images/C4_Red.png")).convert_alpha()
        self.pl1 = pygame.transform.scale(self.pl1, (51, 55))
        self.pl2 = pygame.image.load(str("Ref_Images/C4_Blue.png")).convert_alpha()
        self.pl2 = pygame.transform.scale(self.pl2, (51, 55))
        self.bgi = pygame.image.load(str("Ref_Images/C4_bg.png")).convert()
        self.bgi = pygame.transform.scale(self.bgi, self.screen.get_size())
        self.bgi1 = pygame.image.load(str("Ref_Images/C4_bg_cutout.png")).convert_alpha()
        self.bgi1 = pygame.transform.scale(self.bgi1, self.screen.get_size())
        self.rect = []
        for i in range(7):
            self.rect.append(pygame.Rect(156 + 76*i, 155, 52, 440))

        clock = pygame.time.Clock()

        while True:
            self.screen.fill('black')
            if self.falling:
                self.y += 7.5
                if self.y >= self.yf:
                    self.y = self.yf
                    self.falling = False
                    self.board[self.turn_i][self.turn_j] = self.last_player
                    if self.win() != 0:
                        return self.win()
                    self.turn_i = None
                    self.turn_j = None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.win() == 0 :
                        self.turn()

            self.screen.blit(self.bgi, (0,0))

            if self.falling:
                self.screen.blit(self.coin, (self.x, self.y))

            for i in range(7):
                for j in range(7):
                    if self.board[i][j] == 1 :
                        self.screen.blit(self.pl1, (156 + 75.5*i, 158 + 64*j))
                    elif self.board[i][j] == 2 :
                        self.screen.blit(self.pl2, (156 + 75.5*i, 158 + 64*j))

            self.screen.blit(self.bgi1, (0,0))
            pygame.display.update()
            clock.tick(60)