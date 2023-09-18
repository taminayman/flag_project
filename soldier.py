# import pygame
# import consts
#
#
# def create_soldier(soldier_img):
#     soldier = pygame.image.load(soldier_img)
#     sized_soldier = pygame.transform.scale(soldier, (
#         2 * consts.SQUARE_LENGTH, 4 * consts.SQUARE_LENGTH))
#
#     soldier_box = pygame.Surface(
#             (2 * consts.SQUARE_LENGTH, 4 * consts.SQUARE_LENGTH), )
#     soldier_box.fill(consts.SCREEN_COLOR)
#     soldier_box.blit(sized_soldier, (0, 0))
#
#     return soldier_box
import consts
import pygame

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def init_image(filename, size):
    img = pygame.image.load(filename)
    return pygame.transform.scale(img, (consts.SQUARE_LEN * size[0], consts.SQUARE_LEN * size[1]))


def draw_grass(x, y):
    screen.blit(grass_image, (x * consts.SQUARE_LEN, y * consts.SQUARE_LEN))


def draw_flag(x, y):
    screen.blit(flag_image, (x * consts.SQUARE_LEN, y * consts.SQUARE_LEN))


def draw_soldier(soldier):
    y = soldier[0]
    x = soldier[1]
    screen.blit(soldier_image, (x * consts.SQUARE_LEN, y * consts.SQUARE_LEN))


def draw_game(board, soldier):
    screen.fill(consts.BACKGROUND_COLOR)
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == consts.GRASS:
                draw_grass(x, y)
            elif board[y][x] == consts.FLAG:
                draw_flag(x, y)

    draw_soldier(soldier)


grass_image = init_image(consts.IMG_GRASS, consts.GRASS_SIZE)
flag_image = init_image(consts.IMG_FLAG, consts.FLAG_SIZE)
mine_image = init_image(consts.IMG_MINE, consts.MINE_SIZE)
soldier_image = init_image(consts.IMG_SOLDIER, consts.SOLDIER_SIZE)