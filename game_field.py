import consts
import random

board = []

# creating the initial board
def build_board():
    for i in range(consts.ROW_NUM):
        row = []
        for j in range(consts.COL_NUM):
            row.append(consts.EMPTY)
        board.append(row)
    for i in range(consts.FLAG_HEIGHT):
        for j in range(consts.FLAG_WIDTH):
            board[consts.ROW_NUM - 1 - i][consts.COL_NUM - 1 - j] = consts.FLAG


def add_object(obj, num_of_objects, obj_width, obj_height):
    dx = 1
    dy = 0
    for i in range(num_of_objects):
        found_empty_position = False
        while not found_empty_position:
            x = random.randint(0, consts.COL_NUM - obj_width - 1)
            y = random.randint(0, consts.ROW_NUM - obj_height - 1)
            for i in range(obj_width):
                if board[y][x] == consts.EMPTY:
                    found_empty_position = True
                    board[y][x] = obj
                    x += dx
                    y += dy


def add_mines():
    add_object(consts.MINE, consts.NUM_OF_MINES, consts.MINE_WIDTH , consts.MINE_HEIGHT)

def add_grass():
    add_object(consts.GRASS, consts.NUM_OF_GRASS, consts.GRASS_WIDTH , consts.GRASS_HEIGHT)

build_board()
add_mines()
add_grass()
def visual_matrix(matrix):
    for row in matrix:
        for cell in row:
            print(cell, end=" ")
        print()

visual_matrix(board)

# def win_check():
#     for row in board:
#         for cell in row:
#             if :
#                 return False
#     return True