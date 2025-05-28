from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width, height):
        self.__root = Tk()
        self.__root.title("Maze Generator and Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)
    

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.__isRunning = True
        while self.__isRunning:
            self.redraw()
    

    def close(self):
        self.__isRunning = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


    def draw(self, canvas, fill_color):
        canvas.create_line(self.start.x, self.start.y,
                            self.end.x, self.end.y
                            , fill=fill_color, width=2)