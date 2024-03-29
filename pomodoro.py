import pygame
import sys
from button import Button
 
pygame.init()
 
WIDTH, HEIGHT = 900, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro Timer")
 
CLOCK = pygame.time.Clock()
 
BACKDROP = pygame.image.load("assets/backdrop.png")
WHITE_BUTTON = pygame.image.load("assets/button.png")
 
FONT = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 120)
timer_text = FONT.render("25:00", True, "white")
timer_text_rect = timer_text.get_rect(center=(WIDTH/2, HEIGHT/2-25))
 
START_STOP_BUTTON = Button(WHITE_BUTTON, (WIDTH/2, HEIGHT/2+100), 170, 60, "START", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#c97676", "#9ab034")
POMODORO_BUTTON = Button(None, (WIDTH/2-150, HEIGHT/2-140), 120, 30, "Pomodoro", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#FFFFFF", "#9ab034")
SHORT_BREAK_BUTTON = Button(None, (WIDTH/2, HEIGHT/2-140), 120, 30, "Short Break", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#FFFFFF", "#9ab034")
LONG_BREAK_BUTTON = Button(None, (WIDTH/2+150, HEIGHT/2-140), 120, 30, "Long Break", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#FFFFFF", "#9ab034")
 
POMODORO_LENGTH = 1500 # 1500 secs / 25 mins
SHORT_BREAK_LENGTH = 300 # 300 secs / 5 mins
LONG_BREAK_LENGTH = 900 # 900 secs / 15 mins
 
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    SCREEN.fill("#ba4949")
    SCREEN.blit(BACKDROP, BACKDROP.get_rect(center=(WIDTH/2, HEIGHT/2)))
 
    pygame.display.update()
