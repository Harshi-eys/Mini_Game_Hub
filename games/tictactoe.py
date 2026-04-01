import pygame
import sys 

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Game")
players = {sys.argv[1] : 'X', sys.argv[2] : 'O'}
board=[]
player = sys.argv[1]

for i in range(3):
    for j in range(3):
        board.append(pygame.Rect(41 + 109*j, 41 + 109*i, 100, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.line(screen, 'Red', (145.5, 41), (145.5, 359), 9)
    pygame.draw.line(screen, 'Red', (254.5, 41), (254.5, 359), 9)
    pygame.draw.line(screen, 'Red', (41, 145.5), (359, 145.5), 9)
    pygame.draw.line(screen, 'Red', (41, 254.5), (359, 254.5), 9)

    
    pygame.display.update()



