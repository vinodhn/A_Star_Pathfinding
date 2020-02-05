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
        for row in range(0,10):
            for col in range(0,10):
                print(grid[row][col])
                if grid[row][col] == 1:
                    canvas.create_rectangle(x,y,50,50, outline="black", fill="black", width=1)
                    x = x + 50
                else:
                    canvas.create_rectangle(x,y,50,50, outline="black", fill="white", width=1)
                    x = x + 50
            print("")
            y = y + 50
            x = 0

def create(grid = None, path = None):
    
    root = Tk()
    win = Window()
    win.initUI(grid, path)
    root.geometry("700x700")
    root.mainloop()