import pygame
import sys
import numpy as np
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Connect4")
font = pygame.font.SysFont("palatinolinotype", 40)

Hub = Path(__file__).resolve().parent.parent
p1 = pygame.image.load(str(Hub / "Ref_Images/C4_Red.png")).convert_alpha()
p1 = pygame.transform.scale(p1, (51, 55))
p2 = pygame.image.load(str(Hub / "Ref_Images/C4_Blue.png")).convert_alpha()
p2 = pygame.transform.scale(p2, (51, 55))

bgi = pygame.image.load(str(Hub / "Ref_Images/C4_bg.png")).convert()
bgi = pygame.transform.scale(bgi, screen.get_size())
banner = pygame.image.load(str(Hub / "Ref_Images/banner1.png")).convert_alpha()
banner = pygame.transform.scale(banner, (350, 701))
red_win = pygame.image.load(str(Hub / "Ref_Images/red_win.png")).convert_alpha()
red_win = pygame.transform.scale(red_win, (390, 437))
blue_win = pygame.image.load(str(Hub / "Ref_Images/blue_win.png")).convert_alpha()
blue_win = pygame.transform.scale(blue_win, (390, 437))

rect = []
for i in range(7):
    rect.append(pygame.Rect(156 + 76*i, 155, 52, 440))

bgi1 = pygame.image.load(str(Hub / "Ref_Images/C4_bg_cutout.png")).convert_alpha()
bgi1 = pygame.transform.scale(bgi1, screen.get_size())

dragon = pygame.image.load(str(Hub / "Ref_Images/green_dragon.png")).convert_alpha()
dragon = pygame.transform.scale(dragon, (220, 220))

girl = pygame.image.load(str(Hub / "Ref_Images/warrior_girl1.png")).convert_alpha()
girl = pygame.transform.scale(girl, (95, 167))

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
        self.last_player = None

    def turn(self):
        if self.falling:
            return
        self.draw_turn_text()
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
                            self.last_player = 1
                            self.player = 2
                            self.coin = p1
                            break

                        else:
                            self.last_player = 2
                            self.player = 1
                            self.coin = p2
                            break
                return
            
       
        
    def win(self):
        b = self.board
        p = self.last_player

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
        
    def draw_turn_text(self):
        if self.win() == 0 :
            name = "Red" if self.player == 1 else "Blue"
            text_content = f"{name}'s turn"   
            banner_rect = banner.get_rect(topleft=(235, 410))
            screen.blit(banner, banner_rect)
            if name == "Red" :
                text_surface = font.render(text_content, True, (160, 0, 0))
            else:
                text_surface = font.render(text_content, True, (24, 41, 88))
            screen.blit(text_surface, (310,710))              

game = Game()
clock = pygame.time.Clock()

while True:
    screen.fill('black')
    if game.falling:
        game.y += 7.5
        if game.y >= game.yf:
            game.y = game.yf
            game.falling = False
            game.board[game.turn_i][game.turn_j] = game.last_player
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
    game.draw_turn_text()

    if game.falling:
        screen.blit(game.coin, (game.x, game.y))

    for i in range(7):
        for j in range(7):
            if game.board[i][j] == 1 :
                screen.blit(p1, (156 + 75.5*i, 158 + 64*j))
            elif game.board[i][j] == 2 :
                screen.blit(p2, (156 + 75.5*i, 158 + 64*j))

    screen.blit(bgi1, (0,0))
    screen.blit(dragon, (551,445))
    screen.blit(girl, (425,530))

    if game.win() != 0:
        if game.last_player == 1 :       
            screen.blit(red_win, (215,140))
        else:
            screen.blit(blue_win, (215,140)) 
    pygame.display.update()
    clock.tick(60)