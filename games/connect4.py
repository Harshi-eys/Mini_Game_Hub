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

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    screen.blit(bgi, (0,0))
    screen.blit(bgi1, (0,0))
    pygame.display.update()
