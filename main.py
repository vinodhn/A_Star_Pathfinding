# A* Pathfinding Algorithm
# By Vinodh N.

from tkinter import *
import astar

class GUI(Frame):

    def __init__(self):
        super().__init__()

        self.set_start_node = False
        self.set_end_node = False
        self.set_wall_node = False

        self.start_node = None
        self.end_node = None
        self.wall_nodes = []

        self.initUI()

    def initUI(self):

        self.master.title("A* Pathfinding - Vinodh N.")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self, width=500, height=500)
        self.draw_grid()
        self.canvas.grid(column=0, row=0, sticky="nsew")
        self.canvas.bind("<Button 1>", self.print_mouse_coords)

    def draw_grid(self):
        x,y = 0,0
        for row in range(10):
            for col in range(10):
                x1 = col * 50
                x2 = x1 + 50
                y1 = row * 50
                y2 = y1 + 50
                self.canvas.create_rectangle(x1,y1,x2,y2, fill="white")

    def print_mouse_coords(self, event):
        x_rollover = event.x % 50
        y_rollover = event.y % 50

        box_x = event.x - x_rollover
        box_y = event.y - y_rollover
        
        if self.set_start_node == True and self.start_node == None:
            self.canvas.create_rectangle(box_x,box_y,box_x + 50,box_y + 50, fill="blue")
            print("START NODE")
            self.start_node = (int(box_x/50), int(box_y/50))
            self.set_start_node = False

        elif self.set_end_node == True and self.end_node == None:
            self.canvas.create_rectangle(box_x,box_y,box_x + 50,box_y + 50, fill="red")
            print("END NODE")
            self.end_node = (int(box_x/50), int(box_y/50))
            self.set_end_node = False

        elif self.set_wall_node == True:
            self.canvas.create_rectangle(box_x,box_y,box_x + 50,box_y + 50, fill="black")
            print("WALL NODE")
            self.wall_nodes.append((int(box_x/50), int(box_y/50)))


    def start_algorithm(self):
        print("START")
        self.create_grid()

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


    def create_grid(self):
        if self.start_node == None or self.end_node == None:
            print("You need a start node AND end node.")
        else:
            grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            
            for node in self.wall_nodes:
                grid[node[0]][node[1]] = 1

def main():

    root = Tk()
    ex = GUI()

    frame = Frame(root)
    frame.pack()
    start_button = Button(frame, text="Start", fg="green", command=ex.start_algorithm)
    start_button.pack(side=LEFT, fill='x')
    quit_button = Button(frame, text="Quit", fg="red", command=quit)
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