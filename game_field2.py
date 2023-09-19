import consts2
import random

board = []


def build_board():
    global board

    board = []
    for i in range(consts2.ROW_NUM):
        row = []
        for j in range(consts2.COL_NUM):
            row.append(consts2.EMPTY)
        board.append(row)


def add_object(obj, num_of_objects, size, shadow):
    for cnt in range(num_of_objects):
        found_empty_pos = False
        while not found_empty_pos:
            x = random.randint(0, consts2.COL_NUM - 1 - size[0])
            y = random.randint(0, consts2.ROW_NUM - 1 - size[1])
            occupied = False
            for i in range(x, x + size[0]):
                for j in range(y, y + size[1]):
                    if board[j][i] != consts2.EMPTY:
                        occupied = True
            if occupied:
                continue
            found_empty_pos = True
            for i in range(x, x + size[0]):
                for j in range(y, y + size[1]):
                    board[j][i] = shadow
            board[y][x] = obj


def add_mines():
    add_object(consts2.MINE, consts2.NUM_OF_MINES, consts2.MINE_SIZE, consts2.MINE_SHADOW)


def add_grass():
    add_object(consts2.GRASS, consts2.NUM_OF_GRASS, consts2.GRASS_SIZE, consts2.GRASS_SHADOW)


def add_flag():
    x = consts2.COL_NUM - consts2.FLAG_SIZE[0] - 1
    y = consts2.ROW_NUM - consts2.FLAG_SIZE[1] - 1
    for i in range(consts2.FLAG_SIZE[0]):
        for j in range(consts2.FLAG_SIZE[1]):
            board[y + j][x + i] = consts2.FLAG_SHADOW
    board[y][x] = consts2.FLAG


def soldier_on_mine(x, y):
    if board[y + 3][x] == consts2.MINE or board[y+3][x] == consts2.MINE_SHADOW:
        return True
    if board[y + 3][x+1] == consts2.MINE or board[y+3][x+1] == consts2.MINE_SHADOW:
        return True
    return False


def soldier_on_flag(x, y):
    if board[y + 3][x] == consts2.FLAG or board[y+3][x] == consts2.FLAG_SHADOW:
        return True
    if board[y + 3][x+1] == consts2.FLAG or board[y+3][x+1] == consts2.FLAG_SHADOW:
        return True
    return False
