import pygame
import sys 

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Game")
board=[]
player = sys.argv[1]

pygame.draw.line(screen, 'Red', (145.5, 41), (145.5, 359), 9)
pygame.draw.line(screen, 'Red', (254.5, 41), (254.5, 359), 9)
pygame.draw.line(screen, 'Red', (41, 145.5), (359, 145.5), 9)
pygame.draw.line(screen, 'Red', (41, 254.5), (359, 254.5), 9)

for i in range(3):
    for j in range(3):
        board.append(pygame.Rect(41 + 109*j, 41 + 109*i, 100, 100))

value = []
for i in range(9):
    value.append(0)

def turn(board):
    global player
    for i in range(9):
        if board[i].collidepoint(pygame.mouse.get_pos()):
            if value[i] != 0:
                return
            
            if player == sys.argv[1]:
                pad = 12.5
                pygame.draw.line(screen, 'White', (board[i].left + pad, board[i].top + pad), (board[i].right - pad, board[i].bottom - pad), 5)
                pygame.draw.line(screen, 'White', (board[i].left + pad, board[i].bottom - pad), (board[i].right - pad, board[i].top + pad), 5)
                player = sys.argv[2]
                value[i] = 'X'
                win(board)

            else :
                pygame.draw.circle(screen, 'white', board[i].center, 37.5, 5)
                player = sys.argv[1]
                value[i] = 'O'
                win(board)

def win(board):

    for i in range(3):
        if value[i] == value[i+3] and value[i] == value[i+6] and value[i] != 0:
            pygame.draw.line(screen, 'orange', (board[i].centerx, board[i].centery - 40), (board[i+6].centerx, board[i+6].centery + 40), 4)
            return 1
        
    for i in {0, 3, 6}:
        if value[i] == value[i+1] and value[i] == value[i+2] and value[i] != 0:
            pygame.draw.line(screen, 'orange', (board[i].centerx - 40, board[i].centery ), (board[i+2].centerx + 40, board[i+2].centery), 4)
            return 1
        
    if value[0] == value[4] and value[0] == value[8] and value[0] != 0:
        pygame.draw.line(screen, 'orange', (board[0].centerx - 40, board[0].centery - 40), (board[8].centerx + 40, board[8].centery + 40), 4)
        return 1
    
    elif value[2] == value[4] and value[2] == value[6] and value[2] != 0:
        pygame.draw.line(screen, 'orange', (board[2].centerx + 40, board[2].centery - 40), (board[6].centerx - 40, board[6].centery + 40), 4)
        return 1
    
    return 0

    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not win(board):
                turn(board)

    pygame.display.update()
