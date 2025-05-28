import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells2(self):
        num_cols = 14
        num_rows = 11
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_cell_size(self):
        num_cols = 12
        num_rows = 10
        cell_size_x = 10
        cell_size_y = 10
        m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)
        self.assertEqual(
            m1._Maze__cell_size_x,
            cell_size_x,
        )
        self.assertEqual(
            m1._Maze__cell_size_y,
            cell_size_y,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        cell_size_x = 10
        cell_size_y = 10
        m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)
        self.assertFalse(m1._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m1._Maze__cells[num_cols-1][num_rows-1].has_bottom_wall)

    def test_maze_break_walls_r(self):
        num_cols = 10
        num_rows = 10
        cell_size_x = 10
        cell_size_y = 10
        m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)
        m1._Maze__break_walls_r(0, 0)
        self.assertTrue(m1._Maze__cells[0][0].visited)
        self.assertTrue(m1._Maze__cells[1][0].visited or m1._Maze__cells[0][1].visited)

    def test_maze_reset_visited(self):
        num_cols = 10
        num_rows = 10
        cell_size_x = 10
        cell_size_y = 10
        m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)
        m1._Maze__break_walls_r(0, 0)
        m1._Maze__reset_visited()
        self.assertFalse(m1._Maze__cells[0][0].visited)
        self.assertFalse(m1._Maze__cells[1][0].visited or m1._Maze__cells[0][1].visited)

if __name__ == "__main__":
    unittest.main()
