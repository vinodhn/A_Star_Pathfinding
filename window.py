from tkinter import Tk, Canvas, Frame, BOTH

class Window(Frame):
    
    def __init__(self):
        super().__init__()
    
    def initUI(self, grid, path, start, end):
        self.master.title("A* Pathfinding - Vinodh N.")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        self.draw_grid(grid,canvas)
        self.draw_path(path, canvas)
        self.draw_start_end(start,end,canvas)
        canvas.pack(fill=BOTH, expand=1)

    def draw_grid(self, grid = None, canvas = None):
        x,y = 0,0
        for row in range(10):
            for col in range(10):
                x1 = col * 50
                x2 = x1 + 50
                y1 = row * 50
                y2 = y1 + 50
                if grid[row][col] == 0:
                    canvas.create_rectangle(x1,y1,x2,y2, fill="white")
                elif grid[row][col] == 1:
                    canvas.create_rectangle(x1,y1,x2,y2, fill="black")
    
    def draw_start_end(self, start = None, end = None, canvas = None):
        startX, startY = start
        startSqX = (startX * 50) + 50
        startSqY = (startY * 50) + 50
        endX, endY = end
        endSquareX = (endX * 50) + 50
        endSquareY = (endY * 50) + 50
        canvas.create_rectangle(startX * 50, startY * 50, startSqX, startSqY, fill="blue")
        canvas.create_rectangle(endX * 50, endY * 50, endSquareX, endSquareY, fill="red")
        
    def draw_path(self, path = None, canvas = None):
        for point in path:
            x1, y1 = point
            x1 = x1 * 50
            y1 = y1 * 50
            x2 = x1 + 50
            y2 = y1 + 50
            canvas.create_rectangle(x1,y1,x2,y2, fill = "purple")
            

def create(grid = None, path = None, start = None, end = None):
    
    root = Tk()
    win = Window()
    win.initUI(grid, path, start, end)
    root.geometry("500x500")
    root.mainloop()