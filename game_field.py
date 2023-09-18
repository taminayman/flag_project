import consts
import random

board = []

def build_board():
    for i in range(consts.ROW_NUM):
        row = []
        for j in range(consts.COL_NUM):
            row.append(consts.EMPTY)
        board.append(row)

    board[consts.ROW_NUM - 1][consts.COL_NUM - 1] = consts.FLAG


def add_object(obj, num_of_objects):
    for i in range(num_of_objects):
        found_empty_pos = False
        while not found_empty_pos:
            x = random.randint(0, consts.COL_NUM - 1)
            y = random.randint(0, consts.ROW_NUM - 1)
            if board[y][x] == consts.EMPTY:
                found_empty_pos = True
                board[y][x] = obj


def add_mines():
    add_object(consts.MINE, consts.NUM_OF_MINES)


def add_grass():
    add_object(consts.GRASS, consts.NUM_OF_GRASS)

