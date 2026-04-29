import pygame
import sys
from pathlib import Path
import subprocess
import csv

usr1 = sys.argv[1]
usr2 = sys.argv[2]
sys.path.append(str(Path(__file__).resolve().parent.parent))

pygame.init()
pygame.mixer.init()
size = 800
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("Mini Game Hub")

pygame.mixer.music.load(str("Ref_Audios/bg_music.mp3"))
pygame.mixer.music.play(-1) 

menu = pygame.image.load(str("Ref_Images/game_bg.png")).convert()
menu = pygame.transform.scale(menu, screen.get_size())
settings = pygame.image.load(str("Ref_Images/settings.png")).convert_alpha()
settings = pygame.transform.scale(settings, (500, 340))
music = pygame.image.load(str("Ref_Images/music.png")).convert_alpha()
music = pygame.transform.scale(music, (500, 340))
off_music = pygame.image.load(str("Ref_Images/off_music.png")).convert_alpha()
off_music = pygame.transform.scale(off_music, (500, 340))
rect1 = pygame.Rect(255, 225, 310, 75)
rect2 = pygame.Rect(255, 343, 310, 75)
rect3 = pygame.Rect(255, 463, 310, 75)
music_rect = pygame.Rect(723, -0.5, 70, 70)

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
    
music_on = True
def main():
    global music_on
    while True:
        screen.blit(menu, (0,0))
        if rect1.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, "#FF9900", (255, 225, 310, 75), width=2, border_radius= 10)
        if rect2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, "#FF9900", (255, 343, 310, 75), width=2, border_radius= 10)
        if rect3.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, "#FF9900", (255, 463, 310, 75), width=2, border_radius= 10)

        if music_on:
            screen.blit(music, (725, 0))
        else:
            screen.blit(off_music, (727, 1.5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect1.collidepoint(pygame.mouse.get_pos()):
                    from games.tictactoe import TicTacToe
                    replaying = True
                    while replaying:
                        game = TicTacToe()
                        result = game.run()
                        if result == "replay" : 
                            pass
                        elif result == "home" : 
                            replaying = False
                    #subprocess.run(["sh", "leaderboard.sh"])

                elif rect2.collidepoint(pygame.mouse.get_pos()):
                    from games.othello import Othello
                    replaying = True
                    while replaying:
                        game = Othello()
                        result = game.run()
                        if result == "replay" : 
                            pass
                        elif result == "home" : 
                            replaying = False
                    #subprocess.run(["sh", "leaderboard.sh"])
                    
                elif rect3.collidepoint(pygame.mouse.get_pos()):
                    from games.connect4 import Connect4
                    replaying = True
                    while replaying:
                        game = Connect4()
                        result = game.run()
                        if result == "replay" : 
                            pass
                        elif result == "home" : 
                            replaying = False
                    #subprocess.run(["sh", "leaderboard.sh"])
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if music_rect.collidepoint(pygame.mouse.get_pos()):
                    if music_on == True:
                        pygame.mixer.music.pause()  
                        music_on = False
                    else:
                        pygame.mixer.music.unpause()
                        music_on = True

        if music_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, "#FF9900", (723, -0.5, 70, 70), width=2, border_radius= 10)
        pygame.display.update()

if __name__ == "__main__":
    main()
