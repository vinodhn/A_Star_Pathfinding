# A* Pathfinding Algorithm
# By Vinodh N.

# Node Class
class Node():

    def init(self, parent = None, position = None):
        self.parent = parent
        self.position = position

        self.gCost = 0
        self.hCost = 0
        self.fCost = 0

    def eq(self, other):
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
