# A* Pathfinding Algorithm
# Created by Vinodh N.
# Based on the code by Nicholas Swifts

import math
import heapq

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

    # Need to define these for the heap queue
    def __lt__(self, other):
        return self.fCost < other.fCost

    def __gt__(self, other):
        return self.fCost > other.fCost

# Main A* Pathfinding Loop
def pathfind(grid, start, end):

    start_node = Node(None, start)
    end_node = Node(None, end)
    
    start_node.gCost = start_node.hCost = start_node.fCost = 0
    end_node.gCost = end_node.hCost = end_node.fCost = 0

    open_nodes = []
    closed_nodes = []

    heapq.heapify(open_nodes)
    heapq.heappush(open_nodes, start_node)

    surround_spots = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)

    max_iterations = (len(grid[0]) * len(grid) // 2) # Add stop condition proportional to grid
    current_iteration = 0

    while len(open_nodes) > 0:

        current_iteration += 1

        if current_iteration >= max_iterations:
            print("Couldn't find a path, was taking too long")
            print("Here's what I got so far")
            print(get_path(current_node))
            break

        # Get current node and move to closed
        current_node = heapq.heappop(open_nodes)
        closed_nodes.append(current_node)

        # Check if we're at goal
        if current_node == end_node:
            return get_path(current_node)

        surround_nodes = []

        # See if surrounding spots are valid walking spots
        for position in surround_spots:
            
            # Get spot we're checking
            spot_to_check = (current_node.position[0] + position[0], current_node.position[1] + position[1])

            # Make sure we're within the grid
            if spot_to_check[0] < 0 or spot_to_check[0] > len(grid) -1 or spot_to_check[1] < 0 or spot_to_check[1] > (len(grid[len(grid)-1]) -1):
                continue 

            # Make sure we can actually walk through the area
            if grid[spot_to_check[0]][spot_to_check[1]] == 1:
                continue       

            test_node = Node(current_node, spot_to_check)
            surround_nodes.append(test_node)

        # Check surrounding nodes
        for node in surround_nodes:

            # Check if node is closed already:
            if len([closed_node for closed_node in closed_nodes if closed_node == node]) > 0:
                continue

            node.gCost = node.parent.gCost + 1
            node.hCost = math.sqrt(((node.position[0] - end_node.position[0]) ** 2) + ((node.position[1] - end_node.position[1]) ** 2))
            node.fCost = node.gCost + node.hCost

            if len([open_node for open_node in open_nodes if node.position == open_node.position and node.gCost > open_node.gCost]) > 0:
                continue
            
            heapq.heappush(open_nodes, node)

    print("Couldn't get path to end node")
    return None

def get_path(currentNode):
    path = []
    current = currentNode
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]     
