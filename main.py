from constants import *
from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)

    maze = Maze(
        BORDER, BORDER,
        NUM_ROWS, NUM_COLS,
        CELL_SIZE_X, CELL_SIZE_Y,
        win=win,
    )
    maze.solve()

    win.wait_for_close()

main()