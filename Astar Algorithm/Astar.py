'''Alorithm for A*'''
import pathfinding

# setup your search area
def astar(start, goal, grid):
    '''The legendary A* algorithm'''
    camefrom = []
    openlist = []
    closedlist = []
    currentnode = start
    openlist.append(currentnode)
    while len(openlist) != 0:

        #sortlist sorts the node list from grid by the 'f' score
        sort_list(grid)
        #assigns the current node to the first node in openlist
        currentnode = openlist[0]
        #checks if the current node is at the goal and follows parent path
        if currentnode == goal:
            camefrom = retrace(currentnode)
            return camefrom
        #removes that node from the open list
        openlist.remove(currentnode)
        #adds the new current node into the closed list
        closedlist.append(currentnode)

        #gets the neighbors for the current node in the grid given
        #getneighbors(currentnode, grid)
        pathfinding.getneighbors(currentnode, grid)

        #loops through the adjacent nodes to check if they found the goal node
        for neighbor in currentnode.neighbors:
            if neighbor in closedlist or not neighbor.walkable:
                continue
            tentative_gscore = currentnode.gscore + currentnode.sgscore(neighbor)
            #if the searched node is not in the open list yet it adds it to be checked
            if neighbor not in openlist:
                openlist.append(neighbor)
            elif tentative_gscore >= neighbor.gscore:
                continue
            #updates all the node's f,g,h scores in the grid
            neighbor.parent = currentnode
            neighbor.gscore = tentative_gscore
            neighbor.updatescores(goal)

    return camefrom


def retrace(node):
    '''reconstructs the path'''
    final_path = []
    parentednode = node
    while parentednode is not None:
        final_path.append(parentednode)
        parentednode = parentednode.parent
    return final_path


def sort_list(grid):
    '''Sorts the open and closed lists'''
    for node in grid:
        for nodes in grid:
            if node.f < nodes.f:
                tempnode = node
                node = nodes
                nodes = tempnode

def getneighbors(node, graph):
    '''Looks for the node's neighbors'''
    right = [node[0]+1, node[1]]
    topleft = [node[0]-1, node[1] + 1]
    top = [node[0], node[1] + 1]
    topright = [node[0]+1, node[1] + 1]
    left = [node[0]-1, node[1]]
    downleft = [node[0]-1, node[1] - 1]
    down = [node[0], node[1] - 1]
    downright = [node[0] + 1, node[1] - 1]
    dirs = [right, topright, top, topleft, left, downleft, down, downright]
    for nodee in graph:
        for position in dirs:
            if nodee[0] == position[0] and nodee[1] == position[1]:
                node.neighbors.append(nodee)
    return node.neighbors
