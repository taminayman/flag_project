import consts

game_field = []
def create():
    global game_field
    bubbles_grid = [
        create_field_row(row, row_start=0, row_length=consts.COL_NUM)
        for row in
        range(consts.BUBBLE_GRID_START_ROWS)]

    # Create an empty row for future bubbles
    last_row = consts.BUBBLE_GRID_START_ROWS
    bubbles_grid.append(create_empty_row(last_row))


def create_bubble_row(row_index, row_start, row_length):
    return [Bubble.create(Bubble.calc_center_x(col, row_index, row_start),
                          Bubble.calc_center_y(row_index),
                          random.choice(consts.bubble_colors)) for col in
            range(row_length)]