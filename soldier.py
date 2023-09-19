import pygame
import consts
import game_field


def create_soldier(soldier_img):
    soldier = pygame.image.load(soldier_img)
    sized_soldier = pygame.transform.scale(soldier, (
        2 * consts.SQUARE_LEN, 4 * consts.SQUARE_LEN))
    return sized_soldier


def soldier_on_mine(x, y):
    if game_field.board[y + 3][x] == consts.MINE or game_field.board[y+3][x] == consts.MINE_SHADOW:
        return True
    if game_field.board[y + 3][x+1] == consts.MINE or game_field.board[y+3][x+1] == consts.MINE_SHADOW:
        return True
    return False
