import consts

game_field = []
def create():
    global game_field
    game_field = [
        create_field_row(row, row_start=0, row_length=consts.COL_NUM)
        for row in
        range(consts.ROW_NUM)]




def create_field_row(row_index, row_start, row_length):
    return [Bubble.create(Bubble.calc_center_x(col, row_index, row_start),
                          Bubble.calc_center_y(row_index),
                          random.choice(consts.bubble_colors)) for col in
            range(row_length)]