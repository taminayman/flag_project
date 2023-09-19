import pygame
import consts
import time
import soldier

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_screen():
    pygame.display.set_caption("The Flag")
    screen.fill(consts.GREEN)
    return screen


def init_image(filename, size):
    img = pygame.image.load(filename)
    return pygame.transform.scale(img, (consts.SQUARE_LEN * size[0], consts.SQUARE_LEN * size[1]))


def put_soldier_in_place():
    screen.blit(soldier.create_soldier(consts.SOLDIER_IMG), (0, 0))
    return screen


def create_flag(flag_img):
    flag = pygame.image.load(flag_img)
    sized_flag = pygame.transform.scale(flag, (
        consts.FLAG_SIZE[0] * consts.SQUARE_LEN, consts.FLAG_SIZE[1] * consts.SQUARE_LEN))
    return sized_flag


def put_flag_in_place():
    screen.blit(create_flag(consts.FLAG_IMG), (consts.WINDOW_WIDTH - consts.FLAG_SIZE[0] * consts.SQUARE_LEN, consts.WINDOW_HEIGHT - consts.FLAG_SIZE[1] * consts.SQUARE_LEN))
    return screen


# draw_screen()
# put_soldier_in_place()
# put_flag_in_place()
# pygame.display.flip()
#
# time.sleep(5)


grass_image = init_image(consts.GRASS_IMG, consts.GRASS_SIZE)
mine_image = init_image(consts.MINE, consts.MINE_SIZE)
explosion_image = init_image(consts.EXPLODE_IMG, consts.SOLDIER_SIZE)
flag_image = create_flag(consts.FLAG_IMG)
soldier_image = soldier.create_soldier(consts.SOLDIER_IMG)


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
    screen.blit(explosion_image, (x * consts.SQUARE_LEN, y * consts.SQUARE_LEN))


def draw_game_over(msg):
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    txt_image = font.render(msg, True, consts.FONT_COLOR)
    txtRect = txt_image.get_rect()
    txtRect.center = (consts.WINDOW_WIDTH // 2, consts.WINDOW_HEIGHT // 2)
    screen.blit(txt_image, txtRect)


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
