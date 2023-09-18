import pygame
import consts
import time


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

time.sleep(5)


# import soldier

#
#
# screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
#
#
# def draw_screen():
#     pygame.display.set_caption("The Flag")
#     screen.fill(consts.SCREEN_COLOR)
#     return screen
#
#
# def put_soldier_in_place():
#     screen.blit(soldier.create_soldier(consts.SOLDIER_IMG), (0, 0))
#     return screen
#
#
# draw_screen()
# put_soldier_in_place()
# pygame.display.flip()
