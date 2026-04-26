import pygame
import sys
import os
from pathlib import Path
import pygame

pygame.init()
pygame.mixer.init()
size = 800
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("Mini Game Hub")
clock = pygame.time.Clock()

Mini = Path(__file__).parent.parent
pygame.mixer.music.load(str(Mini / "Mini_Game_Hub/Ref_Audios/bg_music.mp3"))
pygame.mixer.music.play(-1) 

menu = pygame.image.load(str(Mini / "Mini_Game_Hub/Ref_Images/game_bg.png")).convert()
menu = pygame.transform.scale(menu, screen.get_size())

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else : continue

    screen.blit(menu, (0, 0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()