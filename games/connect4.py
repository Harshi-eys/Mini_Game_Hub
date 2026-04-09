import pygame
import sys
import numpy as np

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Connect4")

p1 = pygame.image.load("./Ref_Images/C4_Red.png").convert_alpha()
p1 = pygame.transform.scale(p1, (51, 55))
p2 = pygame.image.load("./Ref_Images/C4_Blue.png").convert_alpha()
p2 = pygame.transform.scale(p2, (51, 55))

bgi = pygame.image.load("./Ref_Images/C4_bg.png").convert()
bgi = pygame.transform.scale(bgi, screen.get_size())

rect = []
for i in range(7):
    rect.append(pygame.Rect(156 + 76*i, 155, 52, 440))

bgi1 = pygame.image.load("./Ref_Images/C4_bg_cutout.png").convert_alpha()
bgi1 = pygame.transform.scale(bgi1, screen.get_size())

class Game :
    def __init__(self):
        self.board = np.zeros((7,7), dtype = int)
        self.player = 1
        self.x = self.yf = 0
        self.y = -55
        self.coin = None
        self.falling = False
        self.turn_i = None
        self.turn_j = None
        self.pend_player = None

    def turn(self):
        if self.falling:
            return
        for i in range(7):
            if rect[i].collidepoint(pygame.mouse.get_pos()):
                for j in range(6, -1, -1):
                    if self.board[i][j] == 0:
                        self.x = 156 + 75.5*i
                        self.y = -55
                        self.yf = 158 + 64*j
                        self.falling = True
                        self.turn_i = i
                        self.turn_j = j

                        if self.player == 1:
                            self.pend_player = 1
                            self.player = 2
                            self.coin = p1
                            break

                        else:
                            self.pend_player = 2
                            self.player = 1
                            self.coin = p2
                            break
                return
        
    def win(self):
        for i in range(7):
            for j in range(4):
                if self.board[i][j] == self.board[i][j+1] and self.board[i][j] == self.board[i][j+2] and self.board[i][j] == self.board[i][j+3] and self.board[i][j] != 0:
                    return self.board[i][j]

        for i in range(4):
            for j in range(7):
                if self.board[i][j] == self.board[i+1][j] and self.board[i][j] == self.board[i+2][j] and self.board[i][j] == self.board[i+3][j] and self.board[i][j] != 0:
                    return self.board[i][j]

        for i in range(0, 4, 1):
            for j in range(3, 7, 1):
                if self.board[i][j] == self.board[i+1][j-1] and self.board[i][j] == self.board[i+2][j-2] and self.board[i][j] == self.board[i+3][j-3] and self.board[i][j] != 0:
                    return self.board[i][j]
                
        for i in range(0, 4, 1):
            for j in range(0, 4, 1):
                if self.board[i][j] == self.board[i+1][j+1] and self.board[i][j] == self.board[i+2][j+2] and self.board[i][j] == self.board[i+3][j+3] and self.board[i][j] != 0:
                    return self.board[i][j]
        return 0

game = Game()
clock = pygame.time.Clock()

while True:

    if game.falling:
        game.y += 7.5
        if game.y >= game.yf:
            game.y = game.yf
            game.falling = False
            game.board[game.turn_i][game.turn_j] = game.pend_player
            game.turn_i = None
            game.turn_j = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.win() == 0 :
                game.turn()

    screen.blit(bgi, (0,0))

    if game.falling:
        screen.blit(game.coin, (game.x, game.y))

    for i in range(7):
        for j in range(7):
            if game.board[i][j] == 1 :
                screen.blit(p1, (156 + 75.5*i, 158 + 64*j))
            elif game.board[i][j] == 2 :
                screen.blit(p2, (156 + 75.5*i, 158 + 64*j))

    screen.blit(bgi1, (0,0))
    pygame.display.update()
    clock.tick(60)