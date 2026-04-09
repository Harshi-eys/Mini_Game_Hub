import pygame
import sys 
import numpy as np

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Tic Tac Toe")

rect = []
for i in range(3):
    for j in range(3):
        rect.append(pygame.Rect(41 + 109*j, 41 + 109*i, 100, 100))

class Game :
    def __init__(self):
        self.board = np.zeros((3,3), dtype = int)
        self.player = 1

    def turn(self):
        for i in range(9):
            if rect[i].collidepoint(pygame.mouse.get_pos()):
                if self.board[i//3][i % 3] != 0:
                    return
                
                if self.player == 1:
                    self.player = 2
                    self.board[i//3][i%3] = 1

                else :
                    self.player = 1
                    self.board[i//3][i%3] = 2

    def win(self):
        for i in range(3):
            if self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i] and self.board[0][i] != 0:
                pygame.draw.line(screen, 'orange', (rect[i].centerx, rect[i].centery - 40), (rect[i+6].centerx, rect[i+6].centery + 40), 4)
                return self.board[0][i]
            
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2] and self.board[i][0] != 0:
                pygame.draw.line(screen, 'orange', (rect[i].centerx - 40, rect[i].centery ), (rect[i+2].centerx + 40, rect[i+2].centery), 4)
                return self.board[i][0]
            
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] != 0:
            pygame.draw.line(screen, 'orange', (rect[0].centerx - 40, rect[0].centery - 40), (rect[8].centerx + 40, rect[8].centery + 40), 4)
            return self.board[0][0]
        
        elif self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0] and self.board[0][2] != 0:
            pygame.draw.line(screen, 'orange', (rect[2].centerx + 40, rect[2].centery - 40), (rect[6].centerx - 40, rect[6].centery + 40), 4)
            return self.board[0][2]    
            
        return 0

game = Game()

while True:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.win() == 0:
                game.turn()

    winner = game.win()

    for i in range(9):
        if game.board[i//3][i%3] == 1:
            pad = 12.5
            pygame.draw.line(screen, 'White', (rect[i].left + pad, rect[i].top + pad), (rect[i].right - pad, rect[i].bottom - pad), 5)
            pygame.draw.line(screen, 'White', (rect[i].left + pad, rect[i].bottom - pad), (rect[i].right - pad, rect[i].top + pad), 5)
        elif game.board[i//3][i%3] == 2:
            pygame.draw.circle(screen, 'white', rect[i].center, 37.5, 5)

    pygame.draw.line(screen, 'Red', (145.5, 41), (145.5, 359), 9)
    pygame.draw.line(screen, 'Red', (254.5, 41), (254.5, 359), 9)
    pygame.draw.line(screen, 'Red', (41, 145.5), (359, 145.5), 9)
    pygame.draw.line(screen, 'Red', (41, 254.5), (359, 254.5), 9)
    pygame.display.update()
