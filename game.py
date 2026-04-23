import pygame
import sys 
import numpy as np
from pathlib import Path
import subprocess
import csv

usr1 = sys.argv[1]
usr2 = sys.argv[2]
sys.path.append(str(Path(__file__).resolve().parent.parent))

pygame.init()
pygame.display.set_caption("Connect4")
screen = pygame.display.set_mode((800,800))
bg = pygame.image.load(str("Ref_Images/game_bg.png")).convert()
bg = pygame.transform.scale(bg, screen.get_size())
rect1 = pygame.Rect(260, 235, 300, 50)
rect2 = pygame.Rect(260, 350, 250, 50)
rect3 = pygame.Rect(260, 475, 290, 50)

class Game:
    def __init__(self):
        self.player = 1
        self.last_player = None
        self.board = None

    def initialisation(self, title):
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode((800,800))
        
    def run(self):
        raise NotImplementedError

    def turn(self):
        raise NotImplementedError
    
    def win(self):
        raise NotImplementedError

def main():
    while True:
        screen.blit(bg, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect1.collidepoint(pygame.mouse.get_pos()):
                    from games.tictactoe import TicTacToe
                    game = TicTacToe()
                    game.run()
                    subprocess.run(["sh", "leaderboard.sh"])
                    sys.exit()

                elif rect2.collidepoint(pygame.mouse.get_pos()):
                    from games.othello import Othello
                    game = Othello()
                    game.run()
                    subprocess.run(["sh", "leaderboard.sh"])
                    sys.exit()
                    
                elif rect3.collidepoint(pygame.mouse.get_pos()):
                    from games.connect4 import Connect4
                    game = Connect4()
                    game.run()
                    subprocess.run(["sh", "leaderboard.sh"])
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main()