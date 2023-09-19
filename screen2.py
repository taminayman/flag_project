
import consts2
import pygame

import soldier2

screen = pygame.display.set_mode(
    (consts2.WINDOW_WIDTH, consts2.WINDOW_HEIGHT))


def init_image(filename, size):
    img = pygame.image.load(filename)
    return pygame.transform.scale(img, (consts2.SQUARE_LEN * size[0], consts2.SQUARE_LEN * size[1]))


def draw_grass(x, y):
    screen.blit(grass_image, (x * consts2.SQUARE_LEN, y * consts2.SQUARE_LEN))


def draw_flag(x, y):
    screen.blit(flag_image, (x * consts2.SQUARE_LEN, y * consts2.SQUARE_LEN))


def draw_mine(x, y):
    screen.blit(mine_image, (x * consts2.SQUARE_LEN, y * consts2.SQUARE_LEN))


def draw_soldier(soldier):
    y = soldier[0]
    x = soldier[1]
    screen.blit(soldier_image, (x * consts2.SQUARE_LEN, y * consts2.SQUARE_LEN))


def draw_explode(soldier):
    y = soldier[0]
    x = soldier[1]
    screen.blit(explotion_image, (x * consts2.SQUARE_LEN, y * consts2.SQUARE_LEN))


def draw_game_over(msg):
    font = pygame.font.SysFont(consts2.FONT_NAME, consts2.FONT_SIZE)
    txt_image = font.render(msg, True, consts2.FONT_COLOR)
    txtRect = txt_image.get_rect()
    txtRect.center = (consts2.WINDOW_WIDTH // 2, consts2.WINDOW_HEIGHT // 2)
    screen.blit(txt_image, txtRect)


def draw_game_start(msg):
    font = pygame.font.SysFont(consts2.FONT_NAME, consts2.FONT_SIZE)
    txt_image = font.render(msg, True, consts2.FONT_COLOR)
    txtRect = txt_image.get_rect()
    txtRect.center = (consts2.WINDOW_WIDTH-50, 38)
    screen.blit(txt_image, txtRect)


dark_screen = pygame.display.set_mode((consts2.WINDOW_WIDTH, consts2.WINDOW_HEIGHT))


def draw_dark_screen():
    pygame.display.set_caption("The Flag")
    dark_screen.fill(consts2.BLACK)
    for x in range(0, consts2.WINDOW_WIDTH, consts2.SQUARE_LEN):
        for y in range(0, consts2.WINDOW_HEIGHT, consts2.SQUARE_LEN):
            rect = pygame.Rect(x, y, consts2.SQUARE_LEN, consts2.SQUARE_LEN)
            pygame.draw.rect(dark_screen, consts2.LIGHT_GREEN, rect, 1)
    return dark_screen


def draw_game(board, soldier, show_mines, explode):
    screen.fill(consts2.BACKGROUND_COLOR)
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == consts2.GRASS:
                draw_grass(x, y)
            elif board[y][x] == consts2.FLAG:
                draw_flag(x, y)
            if show_mines and board[y][x] == consts2.MINE:
                screen = draw_dark_screen()
                soldier = soldier2.create_dark_soldier()
                draw_mine(x, y)

    if explode:
        draw_explode(soldier)
    else:
        draw_soldier(soldier)


grass_image = init_image(consts2.IMG_GRASS, consts2.GRASS_SIZE)
flag_image = init_image(consts2.IMG_FLAG, consts2.FLAG_SIZE)
mine_image = init_image(consts2.IMG_MINE, consts2.MINE_SIZE)
soldier_image = init_image(consts2.IMG_SOLDIER, consts2.SOLDIER_SIZE)
explosion_image = init_image(consts2.IMG_EXPLODE, consts2.SOLDIER_SIZE)
