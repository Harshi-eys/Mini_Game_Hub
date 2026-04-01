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

def turn(board, p):
    global player
    for i in range(9):
        if board[i].collidepoint(pygame.mouse.get_pos()):
            if player == sys.argv[1]:
                pad = 12.5
                pygame.draw.line(screen, 'White', (board[i].left + pad, board[i].top + pad), (board[i].right - pad, board[i].bottom - pad), 5)
                pygame.draw.line(screen, 'White', (board[i].left + pad, board[i].bottom - pad), (board[i].right - pad, board[i].top + pad), 5)
                player = sys.argv[2]

            else :
                pygame.draw.circle(screen, 'white', board[i].center, 37.5, 5)
                player = sys.argv[1]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            turn(board,player)

    pygame.draw.line(screen, 'Red', (145.5, 41), (145.5, 359), 9)
    pygame.draw.line(screen, 'Red', (254.5, 41), (254.5, 359), 9)
    pygame.draw.line(screen, 'Red', (41, 145.5), (359, 145.5), 9)
    pygame.draw.line(screen, 'Red', (41, 254.5), (359, 254.5), 9)

    
    pygame.display.update()