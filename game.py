import pygame
import sys
from pathlib import Path
import subprocess
import csv
from datetime import date
import matplotlib.pyplot as plt

# Get usernames from command line arguments
usr1 = sys.argv[1]
usr2 = sys.argv[2]

# Ensure the parent directory is in the path for module imports
sys.path.append(str(Path(__file__).resolve().parent))

# Initialize pygame and audio
pygame.init()
pygame.mixer.init()
size = 800
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("Mini Game Hub")

# Load and play background music indefinitely
pygame.mixer.music.load(str("Ref_Audios/bg_music.mp3"))
pygame.mixer.music.play(-1) 

# Load and scale menu background and icons
menu = pygame.image.load(str("Ref_Images/game_bg.png")).convert()
menu = pygame.transform.scale(menu, screen.get_size())
music = pygame.image.load(str("Ref_Images/music.png")).convert_alpha()
music = pygame.transform.scale(music, (500, 340))
off_music = pygame.image.load(str("Ref_Images/off_music.png")).convert_alpha()
off_music = pygame.transform.scale(off_music, (500, 340))

# Define rectangles for game selection buttons and music toggle
rect1 = pygame.Rect(255, 225, 310, 75)
rect2 = pygame.Rect(255, 343, 310, 75)
rect3 = pygame.Rect(255, 463, 310, 75)
music_rect = pygame.Rect(723, -0.5, 70, 70)

class Game:
    # Base class for individual games (TicTacToe, Othello, Connect4).
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
    # Main menu loop: handles hover effects, music toggle, and game launching.
    global music_on
    while True:
        screen.blit(menu, (0,0))
        
        # Draw hover borders for game selection buttons
        mouse_pos = pygame.mouse.get_pos()
        if rect1.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "#FF9900", (255, 225, 310, 75), width=2, border_radius=10)
        if rect2.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "#FF9900", (255, 343, 310, 75), width=2, border_radius=10)
        if rect3.collidepoint(mouse_pos):
            pygame.draw.rect(screen, "#FF9900", (255, 463, 310, 75), width=2, border_radius=10)

        # Draw music toggle icon based on current state
        if music_on:
            screen.blit(music, (725, 0))
        else:
            screen.blit(off_music, (727, 1.5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                global winner, match
                # Launch Tic Tac Toe
                if rect1.collidepoint(mouse_pos):
                    from games.tictactoe import TicTacToe
                    game = TicTacToe()
                    match = "Tic Tac Toe"
                    winner = game.run() # Game returns the winner (1 or 2)
                    post_game()
                    return

                # Launch Othello
                elif rect2.collidepoint(mouse_pos):
                    from games.othello import Othello
                    game = Othello()
                    match = "Othello"
                    winner = game.run()
                    post_game()
                    return
                
                # Launch Connect4
                elif rect3.collidepoint(mouse_pos):
                    from games.connect4 import Connect4
                    game = Connect4()
                    match = "Connect4"
                    winner = game.run()
                    post_game()
                    return
        
                # Music toggle 
                if music_rect.collidepoint(mouse_pos):
                    if music_on:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    music_on = not music_on

        # Draw hover border for music button
        if music_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, "#FF9900", (723, -0.5, 70, 70), width=2, border_radius=10)
        
        pygame.display.update()

def post_game():
    #Logs game results to CSV and executes the leaderboard shell script.
    global win, loss, today
    # Determine which user won based on player number returned by the game
    if winner == 1: 
        win, loss = usr1, usr2
    elif winner == 2: 
        win, loss = usr2, usr1
    
    # Append match result to history file
    with open("history.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        today = date.today()
        writer.writerow([win, loss, match, today])
    
    # Run the shell script to update leaderboard
    subprocess.run(["sh", "leaderboard.sh"])
    # return to main menu
    with open("history.csv", 'r') as f:
        history = list(csv.DictReader(f))
    games = {}
    play_win = {}
    for i in history:
        if i['Game'] not in games:
            games.update({i['Game'] : 1})
        else : games[i['Game']] += 1

        if i['Winner'] not in play_win:
            play_win.update({i['Winner'] : 1})
        else : play_win[i['Winner']] += 1

    plt.subplot(1, 2, 1)
    plt.bar(play_win.keys(), play_win.values(), width=0.8, color = "#9C4905")
    plt.xlabel("Player Names")
    plt.ylabel("Winning frequency")
    plt.subplot(1, 2, 2)
    plt.pie(games.values(), labels = games.keys())
    plt.tight_layout()
    plt.show() 

    main()


if __name__ == "__main__":
    main()