import pygame

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

money = pygame.mixer.Sound('sounds/money.mp3')
jackpot = pygame.mixer.Sound('sounds/jackpot.mp3')
roll = pygame.mixer.Sound('sounds/roll.mp3')

# 볼륨 조정
money.set_volume(.03)
jackpot.set_volume(.03)
roll.set_volume(.03)

def play_sound(winningX):
        if 0 < winningX < 5:
            money.play()
            return
        if winningX > 5:
            jackpot.play()
            return

def roll_sound():
    roll.play()