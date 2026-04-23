import pygame
import sys
import numpy as np
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.SysFont("palatinolinotype", 40)

Hub = Path(__file__).resolve().parent.parent
bg = pygame.image.load(str(Hub / "Ref_Images/TTT_bg.png")).convert()
bg = pygame.transform.scale(bg, screen.get_size())
X = pygame.image.load(str(Hub / "Ref_Images/TTT_X.png")).convert_alpha()
X = pygame.transform.scale(X, (55, 55))
O = pygame.image.load(str(Hub / "Ref_Images/TTT_O.png")).convert_alpha()
O = pygame.transform.scale(O, (55, 55))
banner = pygame.image.load(str(Hub / "Ref_Images/banner2.png")).convert_alpha()
banner = pygame.transform.scale(banner, (250, 250))
x_win = pygame.image.load(str(Hub / "Ref_Images/x_win.png")).convert_alpha()
x_win = pygame.transform.scale(x_win, (450, 485))
o_win = pygame.image.load(str(Hub / "Ref_Images/o_win.png")).convert_alpha()
o_win = pygame.transform.scale(o_win, (450, 485))

rect =[]
for i in range(10):
    for j in range(10):
        rect.append(pygame.Rect(70 + 68*j, 70 + 68*i, 55, 55))

class Game:
    def __init__(self):
        self.board = np.zeros((10,10), dtype = int)
        self.player = 1
        self.last_player = None

    def turn(self):
        for i in range(100):
            if rect[i].collidepoint(pygame.mouse.get_pos()):
                r = i//10
                c = i%10
                if self.board[r][c] == 0:
                    if self.player == 1:
                        self.board[r][c] = 1
                        self.player = 2
                        self.last_player = 1
                    else:
                        self.board[r][c] = 2
                        self.player = 1
                        self.last_player = 2

    def win(self):
        b = self.board
        p = self.last_player
        if p == None:
            return 0
        elif np.any((b[:,:-4] == p) & (b[:,1:-3] == p) & (b[:,2:-2] == p) & (b[:,3:-1] == p) & (b[:,4:] == p) ):
            return p
        elif np.any((b[:-4,:] == p) & (b[1:-3,:] == p) & (b[2:-2,:] == p) & (b[3:-1,:] == p) & (b[4:,:] == p) ):
            return p 
        elif np.any((b[:-4,:-4] == p) & (b[1:-3,1:-3] == p) & (b[2:-2,2:-2] == p) & (b[3:-1,3:-1] == p) & (b[4:,4:] == p) ):
            return p
        elif np.any((b[4:,:-4] == p) & (b[3:-1,1:-3] == p) & (b[2:-2,2:-2] == p) & (b[1:-3,3:-1] == p) & (b[:-4,4:] == p) ):
            return p   
        else:
            return 0
        
    def draw_turn_text(self):
        if self.win() == 0 :
            name = "X" if self.player == 1 else "O"
            text_content = f"{name}'s turn"   
            banner_rect = banner.get_rect(topleft=(275, -100))
            screen.blit(banner, banner_rect)
            text_surface = font.render(text_content, True, (0, 0, 0))
            screen.blit(text_surface, (334, 16))

game = Game()
while True:
    screen.fill('Black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.win() == 0:
                game.turn()

    screen.blit(bg, (0,0))
    for i in range(100):
        if game.board[i//10][i%10] == 1:
            screen.blit(X, rect[i])
        elif game.board[i//10][i%10] == 2:
            screen.blit(O, rect[i])
    game.draw_turn_text()

    if game.win() != 0:
        if game.last_player == 1 :       
            screen.blit(x_win, (199,140))
        else:
            screen.blit(o_win, (199,140))
    pygame.display.update()