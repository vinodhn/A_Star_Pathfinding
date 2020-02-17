# A* Pathfinding Algorithm
# Created by Vinodh N.
# Based on the code by Nicholas Swift

from tkinter import *
from tkinter import messagebox
import AStar

class GUI(Frame):

    def __init__(self):
        super().__init__()

        self.set_start_node = False
        self.set_end_node = False
        self.set_wall_node = False

        self.start_node = None
        self.end_node = None
        self.wall_nodes = []

        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.initUI()

    def initUI(self):

        self.master.title("A* Pathfinding - Vinodh N.")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self, width=500, height=500)
        self.draw_grid()
        self.canvas.grid(column=0, row=0, sticky="nsew")
        self.canvas.bind("<Button 1>", self.set_nodes)

    def draw_grid(self):
        x,y = 0,0
        for row in range(10):
            for col in range(10):
                x1 = col * 50
                x2 = x1 + 50
                y1 = row * 50
                y2 = y1 + 50
                self.canvas.create_rectangle(x1,y1,x2,y2, fill="white")

    def draw_path(self, path = None):
        for point in path:
            x1, y1 = point
            x1 = x1 * 50
            y1 = y1 * 50
            x2 = x1 + 50
            y2 = y1 + 50
            if point == self.start_node:
                self.canvas.create_rectangle(x1,y1,x2,y2, fill = "blue")
            elif point == self.end_node:
                self.canvas.create_rectangle(x1,y1,x2,y2, fill = "red")
            else:
                self.canvas.create_rectangle(x1,y1,x2,y2, fill = "purple")

    def set_nodes(self, event):
        x_rollover = event.x % 50
        y_rollover = event.y % 50

        box_x = event.x - x_rollover
        box_y = event.y - y_rollover
        
        if self.set_start_node == True and self.start_node == None:
            self.canvas.create_rectangle(box_x,box_y,box_x + 50,box_y + 50, fill="blue")
            self.start_node = (int(box_x/50), int(box_y/50))
            self.set_start_node = False

        elif self.set_end_node == True and self.end_node == None:
            self.canvas.create_rectangle(box_x,box_y,box_x + 50,box_y + 50, fill="red")
            self.end_node = (int(box_x/50), int(box_y/50))
            self.set_end_node = False

        elif self.set_wall_node == True:
            self.canvas.create_rectangle(box_x,box_y,box_x + 50,box_y + 50, fill="black")
            self.wall_nodes.append((int(box_x/50), int(box_y/50)))


    def start_algorithm(self):
        print("START")
        self.create_path()

    def set_start_nodes(self):
        if self.start_node == None:
            self.set_start_node = True
            self.set_end_node = False
            self.set_wall_node = False

    def set_end_nodes(self):
        if self.end_node == None:
            self.set_start_node = False
            self.set_end_node = True
            self.set_wall_node = False
    
    def set_wall_nodes(self):
        self.set_start_node = False
        self.set_end_node = False
        self.set_wall_node = True


    def create_path(self):
        if self.start_node == None or self.end_node == None:
            messagebox.showerror(title="Error", message="Error: You need both a Start Node and End Node")
        else:
            for node in self.wall_nodes:
                self.grid[node[0]][node[1]] = 1

            path = AStar.pathfind(self.grid, self.start_node, self.end_node)
            if path is not None:
                self.draw_path(path)
            else:
                messagebox.showerror(title="Error", message="Error: Couldn't find a path from start to finish")

    def reset_board(self):
        self.set_start_node = False
        self.set_end_node = False
        self.set_wall_node = False

        self.start_node = None
        self.end_node = None
        self.wall_nodes = []

        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        self.draw_grid()

def main():

    root = Tk()
    ex = GUI()

    frame = Frame(root)
    frame.pack()
    start_button = Button(frame, text="Start", fg="green", command=ex.start_algorithm)
    start_button.pack(side=LEFT, fill='x')
    quit_button = Button(frame, text="Reset", fg="red", command=ex.reset_board)
    quit_button.pack(side=LEFT, fill='x')
    set_start_button = Button(frame, text="Set start node", command=ex.set_start_nodes)
    set_start_button.pack(side=LEFT, fill='x')
    set_end_button = Button(frame, text="Set end node", command=ex.set_end_nodes)
    set_end_button.pack(side=LEFT, fill='x')
    set_walls_button = Button(frame, text="Set wall nodes", command=ex.set_wall_nodes)
    set_walls_button.pack(side=LEFT, fill='x')
    root.mainloop()


if __name__ == '__main__':
    main()