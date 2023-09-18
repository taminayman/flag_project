import pygame
import consts
import time
import soldier



screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_screen():
    pygame.display.set_caption("The Flag")
    screen.fill(consts.SCREEN_COLOR)
    return screen


def put_soldier_in_place():
    screen.blit(soldier.create_soldier(consts.SOLDIER_IMG), (0, 0))
    return screen


draw_screen()
put_soldier_in_place()
pygame.display.flip()
