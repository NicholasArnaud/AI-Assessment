'''Entry Point'''
import Astar
from Graph import Graph
import pathfinding

#graph = Graph([6, 6])

#startnode = graph.nodelist[1]
#endnode = graph.nodelist[35]

#graph.nodelist[14].walkable = False
#graph.nodelist[28].walkable = False
#graph.nodelist[29].walkable = False
#Astar.astar(startnode, endnode, graph)

#pathfinding.testfunc(Astar.astar)
failcount = 0
passcount = 0
for _ in range(10):
    res = pathfinding.testfunc(Astar.astar)
    if res:
        passcount += 1
    else:
        failcount += 1
print str.format('fails {0}, passes {1}', failcount, passcount)
