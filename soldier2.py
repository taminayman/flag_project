import consts
import pygame


def create_dark_soldier(dark_soldier_img):
    dark_soldier = pygame.image.load(dark_soldier_img)
    sized_soldier = pygame.transform.scale(dark_soldier, (
        2 * consts.SQUARE_LEN, 4 * consts.SQUARE_LEN))
    return sized_soldier
