from cell import Cell
from graphics import Window, Point, Line
import time
import random
class Maze():
    def __init__(
        self, x1, y1,
        num_rows, num_cols,
        cell_size_x, cell_size_y,
        win=None, seed=None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []

        if seed is not None:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_visited()

    def __create_cells(self):
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self.__cells.append(col_cells)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)
    
    def __draw_cell(self, i, j):
        if self.__win is None:
            return
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.02)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols-1][self.__num_rows-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols-1, self.__num_rows-1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            to_visit = []
            #LEFT
            if i > 0 and not self.__cells[i-1][j].visited:
                to_visit.append((i-1, j))
            #RIGHT
            if i < self.__num_cols - 1 and not self.__cells[i+1][j].visited:
                to_visit.append((i+1, j))
            #UP
            if j > 0 and not self.__cells[i][j-1].visited:
                to_visit.append((i, j-1))
            #DOWN
            if j < self.__num_rows -1 and not self.__cells[i][j+1].visited:
                to_visit.append((i, j+1))

            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return
            
            random_side = random.randrange(len(to_visit))
            next_cell = to_visit[random_side]

            if next_cell[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[next_cell[0]][next_cell[1]].has_left_wall = False   

            if next_cell[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[next_cell[0]][next_cell[1]].has_right_wall = False  

            if next_cell[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[next_cell[0]][next_cell[1]].has_top_wall = False

            if next_cell[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[next_cell[0]][next_cell[1]].has_bottom_wall = False

            self.__break_walls_r(next_cell[0], next_cell[1])    
    
    def __reset_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False

    def _solve_r(self, i, j):
        self.__animate()
        self.__cells[i][j].visited = True
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True
        #LEFT
        if i > 0 and not self.__cells[i-1][j].visited and not self.__cells[i][j].has_left_wall:
            self.__cells[i][j].draw_move(self.__cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i-1][j], undo=True)
        #RIGHT
        if i < self.__num_cols - 1 and not self.__cells[i+1][j].visited and not self.__cells[i][j].has_right_wall:
            self.__cells[i][j].draw_move(self.__cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i+1][j], undo=True)
        #UP
        if j > 0 and not self.__cells[i][j-1].visited and not self.__cells[i][j].has_top_wall:
            self.__cells[i][j].draw_move(self.__cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j-1], undo=True)
        #DOWN
        if j < self.__num_rows - 1 and not self.__cells[i][j+1].visited and not self.__cells[i][j].has_bottom_wall:
            self.__cells[i][j].draw_move(self.__cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j+1], undo=True)

        return False
        
    def solve(self):
        return self._solve_r(0, 0)