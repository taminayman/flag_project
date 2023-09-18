import pygame
import consts


def create_soldier(soldier_img):
    soldier = pygame.image.load(soldier_img)
    sized_soldier = pygame.transform.scale(soldier, (
        2 * consts.SQUARE_LENGTH, 4 * consts.SQUARE_LENGTH))

    soldier_box = pygame.Surface(
            (2 * consts.SQUARE_LENGTH, 4 * consts.SQUARE_LENGTH), )
    soldier_box.fill(consts.SCREEN_COLOR)
    soldier_box.blit(sized_soldier, (0, 0))

    return soldier_box
