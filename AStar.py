# A* Pathfinding Algorithm
# By Vinodh N.

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

    startNode = Node(None, start)
    startNode.gCost = startNode.h = startNode.f = 0

    endNode = Node(None, end)
    endNode.gCost = endNode.hCost = endNode.fCost = 0

    # Main lists that will contain the nodes
    openNodesList = []
    closedNodesList = []

    openNodesList.append(startNode)

    while len(openNodesList) > 0:
        
        currentNode = openNodesList[0]
        currentIndex = 0

        # Find node with lowest f cost and work on that first
        for index, item in enumerate(openNodesList):
            if item.fCost < currentNode.fCost :
                currentNode = item
                currentIndex = index

        # Move current node from open list to closed list
        openNodesList.pop(currentIndex)
        closedNodesList.append(currentNode)

        # If current node is the end goal
        if currentNode == endNode:
            # Create list for nodes in path
            path = []
            current = currentNode

            while current is not None:
                path.append(current.position)
                current = current.parent

            # Once processed, return the reversed list of nodes
            return path[::-1]

        # Check surrounding nodes
        children = []
        for pos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:      
            # Get the position of the node
            nodePos = (currentNode.position[0] + pos[0], currentNode.position[1] + pos[1])

            # Then make sure it is within the grid
            if nodePos[0] > (len(grid) - 1) or nodePos[0] < 0 or nodePos[1] > (len(grid[len(grid) -1]) -1) or nodePos[1] < 0:
                continue

            if grid[nodePos[0]][nodePos[1]] != 0:
                continue

            # Then create a new node to add to children
            newChildNode = Node(currentNode, nodePos)

            children.append(newChildNode)

         
        # Then check the children
        for child in children:

            # See if the child is closed already
            for closed in closedNodesList:
                if child == closed:
                    continue
                
            # Calculate the three costs
            child.gCost = currentNode.gCost + 1
            child.hCost = ((child.position[0] - endNode.position[0]) ** 2) + ((child.position[1] - endNode.position[1]) ** 2)
            child.fCost = child.gCost + child.hCost

            # See if child is open already
            for open in openNodesList:
                if child == open and child.gCost > open.gCost:
                    continue
        
            # Add to open list once evaluated
            openNodesList.append(child)

def main():

    grid = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = pathfind(grid, start, end)
    print(path)

if __name__ == '__main__':
    main()