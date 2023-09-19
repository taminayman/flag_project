import pygame
import time
# import soldier
import consts2
import game_field2
import screen2

soldier_x = 0
soldier_y = 0


def init_board():
    game_field2.build_board()
    game_field2.add_flag()
    game_field2.add_mines()
    game_field2.add_grass()
    screen2.draw_game_start("Welcome to The Flag game. /n"
                           "Have Fun!")


def main():
    global soldier_x
    global soldier_y

    pygame.init()
    init_board()

    game_over = False
    show_mines = False
    explode = False
    win = False

    while not game_over:
        # handle user events
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
                # if the user presses "enter" he can see the mines for the first second after pressing
                elif event.key == pygame.K_RETURN:
                    show_mines = True
                    start_show = time.time()
        if show_mines and time.time() > start_show + 1:
             show_mines = False
        while show_mines and time.time() <= start_show + 1:
            soldier_x = soldier_x
            soldier_y = soldier_y

        # making sure that the soldier stays on the board
        if soldier_x < 0:
            soldier_x = 0
        elif soldier_x > consts2.COL_NUM - consts2.SOLDIER_SIZE[0]:
            soldier_x = consts2.COL_NUM - consts2.SOLDIER_SIZE[0]

        if soldier_y < 0:
            soldier_y = 0
        elif soldier_y > consts2.ROW_NUM - consts2.SOLDIER_SIZE[1]:
            soldier_y = consts2.ROW_NUM - consts2.SOLDIER_SIZE[1]

        # if solider explodes: display the screen announcing he lost for 3 seconds before shutting down the game
        # 'if not explode': so that the user wouldn't move after dying
        if not explode and game_field2.soldier_on_mine(soldier_x, soldier_y):
            explode = True
            explosion_time = time.time()

        if explode and time.time() > explosion_time + 3:
            game_over = True

        screen2.draw_game(game_field2.board, (soldier_y, soldier_x), show_mines, explode)
        if explode:
            screen2.draw_game_over('You Lost')

        if not win and game_field2.soldier_on_flag(soldier_x, soldier_y):
            win = True
            victory_time = time.time()

        if win and time.time() > victory_time + 3:
            game_over = True

        screen2.draw_game(game_field2.board, (soldier_y, soldier_x), show_mines, explode)
        if win:
            screen2.draw_game_over('You won')

        pygame.display.flip()


if __name__ == '__main__':
    main()
