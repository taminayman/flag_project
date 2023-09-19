
import consts2
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


def draw_mine(x, y):
    screen.blit(mine_image, (x * consts.SQUARE_LEN, y * consts.SQUARE_LEN))


def draw_soldier(soldier):
    y = soldier[0]
    x = soldier[1]
    screen.blit(soldier_image, (x * consts.SQUARE_LEN, y * consts.SQUARE_LEN))


def draw_explode(soldier):
    y = soldier[0]
    x = soldier[1]
    screen.blit(explotion_image, (x * consts.SQUARE_LEN, y * consts.SQUARE_LEN))


def draw_game_over(msg):
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    txt_image = font.render(msg, True, consts.FONT_COLOR)
    txtRect = txt_image.get_rect()
    txtRect.center = (consts.WINDOW_WIDTH // 2, consts.WINDOW_HEIGHT // 2)
    screen.blit(txt_image, txtRect)


def draw_game_start(msg):
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    txt_image = font.render(msg, True, consts.FONT_COLOR)
    txtRect = txt_image.get_rect()
    txtRect.center = (consts.WINDOW_WIDTH-50, 38)
    screen.blit(txt_image, txtRect)
#
# def draw_dark_soldier()


def draw_game(board, soldier, show_mines, explode):
    screen.fill(consts.BACKGROUND_COLOR)
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == consts.GRASS:
                draw_grass(x, y)
            elif board[y][x] == consts.FLAG:
                draw_flag(x, y)
            if show_mines and board[y][x] == consts.MINE:
                draw_mine(x, y)

    if explode:
        draw_explode(soldier)
    else:
        draw_soldier(soldier)


grass_image = init_image(consts.IMG_GRASS, consts.GRASS_SIZE)
flag_image = init_image(consts.IMG_FLAG, consts.FLAG_SIZE)
mine_image = init_image(consts.IMG_MINE, consts.MINE_SIZE)
soldier_image = init_image(consts.IMG_SOLDIER, consts.SOLDIER_SIZE)
explotion_image = init_image(consts.IMG_EXPLODE, consts.SOLDIER_SIZE)