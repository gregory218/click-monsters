import pygame
from main import X
from main import Y
pygame.init()
display_surface = pygame.display.set_mode((X, Y))

story_rect = pygame.image.load("assets/story_rect.png")
story_rect.set_alpha(100)
srr = story_rect.get_rect()
srr.center = (X // 2, 400)
display_surface.blit(story_rect, srr)