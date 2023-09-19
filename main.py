import pygame
import time

import consts
import game_field
import screen
import soldier

soldier_x = 0
soldier_y = 0


def init_board():
    game_field.build_board()
    game_field.add_flag()
    game_field.add_mines()
    game_field.add_grass()


def main():
    global soldier_x
    global soldier_y

    pygame.init()
    init_board()

    game_over = False
    show_mines = False
    explode = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
            elif event.type == pygame.KEYDOWN and not explode:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                elif event.key == pygame.K_DOWN:
                    soldier_y += 1
                elif event.key == pygame.K_UP:
                    soldier_y -= 1
                elif event.key == pygame.K_LEFT:
                    soldier_x -= 1
                elif event.key == pygame.K_RIGHT:
                    soldier_x += 1
                elif event.key == pygame.K_RETURN:
                    show_mines = True
                    start_show = time.time()
        if show_mines and time.time() > start_show + 1:
            show_mines = False

        if soldier_x < 0:
            soldier_x = 0
        elif soldier_x > consts.COL_NUM - consts.SOLDIER_SIZE[0]:
            soldier_x = consts.COL_NUM - consts.SOLDIER_SIZE[0]

        if soldier_y < 0:
            soldier_y = 0
        elif soldier_y > consts.ROW_NUM - consts.SOLDIER_SIZE[1]:
            soldier_y = consts.ROW_NUM - consts.SOLDIER_SIZE[1]

        if not explode and soldier.soldier_on_mine(soldier_x, soldier_y):
            explode = True
            explosion_time = time.time()

        if explode and time.time() > explosion_time + 3:
            game_over = True

        screen.draw_game(game_field.board, (soldier_y, soldier_x), show_mines, explode)
        if explode:
            screen.draw_game_over('You Lost')

        pygame.display.flip()


if __name__ == '__main__':
    main()
