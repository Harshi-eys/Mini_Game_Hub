import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Connect4")
player = sys.argv[1]

p1 = pygame.image.load("./Ref_Images/C4_Red.png").convert_alpha()
p1 = pygame.transform.scale(p1, (51, 55))
p2 = pygame.image.load("./Ref_Images/C4_Blue.png").convert_alpha()
p2 = pygame.transform.scale(p2, (51, 55))

bgi = pygame.image.load("./Ref_Images/C4_bg.png").convert()
bgi = pygame.transform.scale(bgi, screen.get_size())
screen.blit(bgi, (0,0))

board = {}
for i in range(7):
    rect = pygame.Rect(156 + 76*i, 155, 52, 440)
    board[i] = {'rect':rect, 'cell':[0, 0, 0, 0, 0, 0, 0]}
#    pygame.draw.rect(screen, 'white', board[i])

bgi1 = pygame.image.load("./Ref_Images/C4_bg_cutout.png").convert_alpha()
bgi1 = pygame.transform.scale(bgi1, screen.get_size())

x = yf = 0
y = -55
coin = None
falling = False

def turn(board):
    global player, x, y, yf, coin, falling

    if falling:
        return

    for i in range(7):
        if board[i]['rect'].collidepoint(pygame.mouse.get_pos()):
            for j in range(6, -1, -1):
                x = 156 + 76*i
                y = 0
                yf = 162 + 65*j
                falling = True

                if board[i]['cell'][j] == 0:
                    if player == sys.argv[1]:
                        player = sys.argv[2]
                        board[i]['cell'][j] = 1
                        coin = p1
                        break

                    else:
                        player = sys.argv[1]
                        board[i]['cell'][j] = 1
                        coin = p2
                        break

            return

clock = pygame.time.Clock()

while True:

    if falling:
        y +=10
        if y >= yf:
            y = yf
            falling = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(pygame.mouse.get_pos())
            turn(board)

    screen.blit(bgi, (0,0))
    if falling:
        screen.blit(coin, (x, y))
    screen.blit(bgi1, (0,0))
    pygame.display.update()
    clock.tick(60)