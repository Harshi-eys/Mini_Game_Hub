import pygame
from pyvidplayer2 import Video
import sys
import os

# --- 1. Initialization ---
pygame.init()
SIZE = 800
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Mini Game Hub")
clock = pygame.time.Clock()

# --- 2. Load Assets (Updated Paths) ---

# Path to Video
video_path = os.path.join("Ref_Videos", "menu2.mp4")
intro_video = Video(video_path)
intro_video.set_volume(50) 

# Path to Image
image_path = os.path.join("Ref_Images", "menu_bg.png")
menu_img = pygame.image.load(image_path)
menu_img = pygame.transform.scale(menu_img, (SIZE, SIZE))

# Path to Audio
audio_path = os.path.join("Ref_Audios", "bg_music.mp3")
pygame.mixer.music.load(audio_path)
pygame.mixer.music.play(-1)

# --- 3. The Main Loop ---
is_intro = True
running = True

while running:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and not is_intro:
            # Check coordinates for your 3 games here
            x, y = mouse_pos
            if 250 < x < 550:
                if 280 < y < 360:
                    print("Launching Tic-Tac-Toe...")
                elif 370 < y < 450:
                    print("Launching Othello...")
                elif 460 < y < 540:
                    print("Launching Connect4...")

    if is_intro:
        intro_video.draw(screen, (0, 0))
        if not intro_video.active:
            is_intro = False
            intro_video.close()
    else:
        screen.blit(menu_img, (0, 0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()