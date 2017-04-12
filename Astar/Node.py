'''Node creator'''

class Node(object):
    '''Creates Nodes '''
    def __init__(self, guid, positional):
        '''Node Constuctor'''

        self.xpos = positional[0]
        self.ypos = positional[1]
        self.g = 0
        self.h = 0
        self.f = 0
        self.neighbors = []
        self.parent = None
        self.walkable = True

    def get_neighbors(self, graph):
        '''Looks for the node's neighbors'''
        right = [self.xpos+1, self.ypos]
        topleft = [self.xpos-1, self.ypos + 1]
        top = [self.xpos, self.ypos + 1]
        topright = [self.xpos+1, self.ypos + 1]
        left = [self.xpos-1, self.ypos]
        downleft = [self.xpos-1, self.ypos - 1]
        down = [self.xpos, self.ypos - 1]
        downright = [self.xpos + 1, self.ypos - 1]
        dirs = [right, top, left, down, topleft, topright, downleft, downright]
        for node in graph.nodelist:
            for position in dirs:
                if node.xpos == position[0] and node.ypos == position[1]:
                    self.neighbors.append(node)

    def manhattan(self, goal):
        '''Returns the distance'''
        self.h = (abs(goal.xpos - self.xpos) + abs(goal.ypos - self.ypos))* 10
        return  self.h


    def costtomove(self, start, neighbor):
        '''Gets gscore'''
        if neighbor.xpos == start.xpos or neighbor.ypos == start.ypos:
            return 10
        else:
            return 14

    def sfscore(self):
        '''sets the f score'''
        self.f = self.g + self.h
        return self.f

    def updatescores(self, goal):
        '''sets h, and f'''
        self.manhattan(goal)
        self.sfscore()

    def printnode(self):
        '''prints node cooridinates'''
        print str(str(self.xpos)+","+str(self.ypos))
