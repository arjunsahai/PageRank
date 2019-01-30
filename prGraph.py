class prGraph:
    """
    WebGraph implementation designed for page-ranking algorithm
    """
    def __init__(self, numNodes):
        self.nodes = {}
        self.pageRank = {}
        self.numNodes = numNodes
        self.initialPageRank = 1 / numNodes

    def add(self, id):
        node = Node(id)
        self.nodes[id] = node
        self.pageRank[id] = self.initialPageRank

    def addEdge(self, id1, id2):
        """
        Creates an edge from node1 to node2
        Assumes id1 and id2 already exist in the graph
        """
        node1 = self.nodes[id1]
        node2 = self.nodes[id2]
        node1.numOutgoingEdges += 1
        node2.incomingEdges.append(id1)

    def getIncomingEdges(self, id):
        return self.nodes[id].incomingEdges

    def size(self):
        return self.numNodes

    def contains(self, id):
        return id in self.nodes

    def getOutgoingDegree(self, id):
        return self.nodes[id].numOutgoingEdges

    def getPageRankDistribution(self):
        return self.pageRank

    def updatePageRankDistribtion(self, distribution):
        self.pageRank = distribution

    def getPageRank(self, id):
        return self.pageRank[id]


class Node:
    """Represents each Node in the graph"""
    def __init__(self, id):
        self.incomingEdges = []
        self.numOutgoingEdges = 0
        self.id = id
    def numOutgoingEdges(self):
        return self.numOutgoingEdges
