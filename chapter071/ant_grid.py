class AntGrid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rows = []
        self.clear()

    def clear(self):
        self.rows = []
        for col_no in range(self.height):
            new_row = []
            self.rows.append(new_row)
            for row_no in range(self.width):
                new_row.append(False)

    def swap(self, x, y):
        self.rows[y][x] = not self.rows[y][x]

    def get(self, x, y):
        return self.rows[y][x]

    def render(self, surface, colors, square_size):
        w, h = square_size
        # 背景を塗りつぶす
        surface.fill(colors[0])

        for y, row in enumerate(self.rows):
            rect_y = y * h
            for x, state in enumerate(row):
                if state:
                    surface.fill(colors[1], (x * w, rect_y, w, h))
