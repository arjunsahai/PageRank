from prGraph import *

def makeGraphFromFile():
    file = open("web-BerkStan.txt", "r")
    webGraph = None
    lineCount = 0
    for line in file:
        if (lineCount == 2):
            arr = line.split()
            webGraph = prGraph(int(arr[2]))
        elif (lineCount >= 4):
            nodes = line.split()
            id1 = int(nodes[0])
            id2 = int(nodes[1])
            # print(id1)
            # print(id2)
            # print(nodes)
            if not webGraph.contains(id1):
                webGraph.add(id1)
            if not webGraph.contains(id2):
                webGraph.add(id2)
            webGraph.addEdge(id1, id2)
        lineCount += 1
    return webGraph
