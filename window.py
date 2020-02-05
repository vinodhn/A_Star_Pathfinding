from tkinter import Tk, Canvas, Frame, BOTH

class Window(Frame):
    
    def __init__(self):
        super().__init__()
    
    def initUI(self, grid, path):
        self.master.title("A* Pathfinding - Vinodh N.")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        self.draw_grid(grid, path, canvas)
        canvas.pack(fill=BOTH, expand=1)

    def draw_grid(self, grid = None, path = None, canvas = None):
        x,y = 0,0
        for row in range(10):
            for col in range(10):
                x1 = col * 50
                x2 = x1 + 50
                y1 = row * 50
                y2 = y1 + 50
                if grid[row][col] == 0:
                    print("{0}  {1}  {2}  {3}".format(x1,y1,x2,y2))
                    canvas.create_rectangle(x1,y1,x2,y2, fill="white")
                elif grid[row][col] == 1:
                    canvas.create_rectangle(x1,y1,x2,y2, fill="black")

def create(grid = None, path = None):
    
    root = Tk()
    win = Window()
    win.initUI(grid, path)
    root.geometry("700x700")
    root.mainloop()