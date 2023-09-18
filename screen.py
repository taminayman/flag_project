import pygame
import consts
import soldier
import time


screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_screen():
    pygame.display.set_caption("The Flag")
    screen.fill(consts.SCREEN_COLOR)
    return screen


def put_soldier_in_place():
    screen.blit(soldier.create_soldier(consts.SOLDIER_IMG), (0, 0))
    return screen


def create_flag(flag_img):
    flag = pygame.image.load(flag_img)
    sized_soldier = pygame.transform.scale(flag, (
        consts.FLAG_WIDTH * consts.SQUARE_LENGTH, consts.FLAG_HEIGHT * consts.SQUARE_LENGTH))

    flag_box = pygame.Surface(
            (consts.FLAG_WIDTH * consts.SQUARE_LENGTH, consts.FLAG_HEIGHT * consts.SQUARE_LENGTH), )
    flag_box.fill(consts.SCREEN_COLOR)
    flag_box.blit(sized_soldier, (consts.WINDOW_WIDTH - consts.FLAG_WIDTH * consts.SQUARE_LENGTH, consts.WINDOW_HEIGHT - consts.FLAG_HEIGHT * consts.SQUARE_LENGTH))
    return flag_box


def put_flag_in_place():
    screen.blit(create_flag(consts.FLAG_IMG), (0, 0))
    return screen


draw_screen()
put_soldier_in_place()
put_flag_in_place()
pygame.display.flip()


time.sleep(5)
