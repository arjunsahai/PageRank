from importGraph import makeGraphFromFile

def calcPageRank():
    webGraph = makeGraphFromFile()
    damping = 0.85
    # print(webGraph.getPageRankDistribution())
    for i in range(100):
        newPageRankDistribution = {}
        distribution = webGraph.getPageRankDistribution()
        for id in distribution:
            newRank = 1 - damping
            incomingEdges = webGraph.getIncomingEdges(id)
            sum = 0
            for incoming in incomingEdges:
                pr = webGraph.getPageRank(incoming) / webGraph.getOutgoingDegree(incoming)
                sum += pr
            newRank = newRank + (damping * sum)
            newPageRankDistribution[id] = newRank
        webGraph.updatePageRankDistribtion(newPageRankDistribution)
    return webGraph.getPageRankDistribution()

if (__name__ == "__main__"):
    print(calcPageRank())
