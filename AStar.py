# A* Pathfinding Algorithm
# By Vinodh N.
import window
import math

# Node Class
class Node():

    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position

        self.gCost = 0
        self.hCost = 0
        self.fCost = 0

    def __eq__(self, other):
        return self.position == other.position

# Main A* Pathfinding Loop
def pathfind(grid, start, end):

    start_node = Node(None, start)
    end_node = Node(None, end)
    
    start_node.gCost = start_node.hCost = start_node.fCost = 0
    end_node.gCost = end_node.hCost = end_node.fCost = 0

    open_nodes = []
    closed_nodes = []

    surround_spots = [(-1,-1), (0,-1), (1,-1),(-1,0), (0,0), (1,0), (-1,1), (0,1), (1,1)]

    open_nodes.append(start_node)

    max_iterations = 2000
    current_iteration = 0

    while len(open_nodes) > 0:

        if current_iteration >= max_iterations:
            print("Couldn't find a path, was taking too long")
            print("Here's what I got so far")
            print(get_path(current_node))
            break
        
        sort_by_fcost(open_nodes)
        current_node = open_nodes[0]

        # Move node from open to closed
        open_nodes.pop(0)
        closed_nodes.append(current_node)

        # Check if we're at goal
        if current_node.position == end_node.position:
            return get_path(current_node)
            break

        surround_nodes = []

        # See if surrounding spots are valid walking spots
        for position in surround_spots:

            if position == surround_spots[1][1]:
                continue
            
            spot_to_check = (current_node.position[0] + position[0], current_node.position[1] + position[1])

            if spot_to_check[0] < 0 or spot_to_check[0] > len(grid) -1 or spot_to_check[1] < 0 or spot_to_check[1] > (len(grid[len(grid)-1]) -1):
                continue 

            if grid[spot_to_check[1]][spot_to_check[0]] == 1:
                continue       

            test_node = Node(current_node, spot_to_check)
            surround_nodes.append(test_node)

        # Check surrounding nodes
        for node in surround_nodes:
            # Check if node is closed already:
            for closed_node in closed_nodes:
                if node == closed_node:
                    break

            node.gCost = node.parent.gCost + 1
            node.hCost = math.sqrt(((node.position[0] - end_node.position[0]) ** 2) + ((node.position[1] - end_node.position[1]) ** 2))
            node.fCost = node.gCost + node.hCost

            for open_node in open_nodes:
                if node == open_node:
                    if node.gCost > open_node.gCost:
                        continue
            
            open_nodes.append(node)
            current_iteration += 1

def sort_by_fcost(nodes):
    swapped_elements = True
    while swapped_elements:
        swapped_elements = False
        for i in range(len(nodes) - 1):
            if nodes[i].fCost > nodes[i+1].fCost:
                nodes[i], nodes[i+1] = nodes[i+1], nodes[i]
                swapped_elements = True

def get_path(currentNode):
    path = []
    current = currentNode
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]     

def main():
    
    # MUST BE 10 x 10 grid
    grid = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

    start = (1, 1)
    end = (8, 6)

    path = pathfind(grid, start, end)
    #print(path)

    window.create(grid, path, start, end)

if __name__ == '__main__':
    main()