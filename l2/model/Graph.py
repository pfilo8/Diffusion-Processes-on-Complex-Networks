import matplotlib.pyplot as plt
import networkx as nx
import sys

from .Queue import Queue
from .Vertex import Vertex


class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVerticies = 0

    def addVertex(self, key):
        if key not in self:
            self.numVerticies += 1
            newVertex = Vertex(key)
            self.vertList[key] = newVertex
            return newVertex
        else:
            raise ValueError('This Vertex is in this Graph.')

    def addVerticesFromList(self, vertexList):
        for vert in vertexList:
            self.addVertex(vert)

    def addEdge(self, u, v, weight=1):
        if u not in self.vertList.keys():
            self.addVertex(u)
        if v not in self.vertList.keys():
            self.addVertex(v)
        self.vertList[u].addNeighbour(self.vertList[v], weight)
        self.vertList[v].addNeighbour(self.vertList[u], weight)

    def addEdgesFromList(self, edgesList):
        for u, v in edgesList:
            self.addEdge(u, v)

    def getVertex(self, vert):
        return self.vertList.get(vert, None)

    def getVertices(self):
        return list(self.vertList.values())

    def getEdges(self):
        return [(vertex, neighbor) for vertex in self.getVertices() for neighbor in vertex.getNeighbors()]

    def getNeighbors(self, v):
        return self.vertList[v].getNeighbors()

    def __contains__(self, v):
        return v in self.vertList.keys()

    def saveGraph(self, filename):
        with open(filename, "w+") as f:
            f.write("graph {")
            f.write('\n')
            for u, v in self.getEdges():
                row = "{u} -- {v}".format(u=u.id, v=v.id)
                f.write(row)
                f.write('\n')
            f.write("}")

    def getShortestPath(self, vert, reset=True):
        results = self.__countPaths(vert)
        if reset:
            self.__resetGraph()
        return results

    def __iter__(self):
        for el in self.vertList.values():
            yield el

    def __repr__(self):
        return str(self.vertList)

    def __getitem__(self, key):
        return self.vertList[key]

    def __countPaths(self, vertex):
        self.__bfs(vertex)
        results = {
            vert.id: vert.distance
            for vert in self
        }
        return results

    def __bfs(self, vertex):
        vertex = self[vertex]
        vertex.distance = 0
        vertex.pred = None
        vertKolejka = Queue()
        vertKolejka.push(vertex)
        while (len(vertKolejka) > 0):
            currentVert = vertKolejka.pop()
            for nbr in currentVert.getConnections():
                if nbr.color == 'white':
                    nbr.color = 'gray'
                    nbr.distance = currentVert.distance + 1
                    nbr.pred = currentVert
                    vertKolejka.push(nbr)
            currentVert.color = 'black'

    def traverse(self, vertex):
        x = self[vertex]
        while (x.pred != None):
            print(x.id)
            x = x.pred
        print(x.id)

    def __resetGraph(self):
        for vert in self:
            vert.color = 'white'
            vert.dist = sys.maxsize
            vert.pred = None
            vert.fin = 0
            vert.disc = 0

# TODO:
# - bfs
# - dijkstra algorithm
# - dfs
# - node degree
# - clustering, betweeness ..
# - set weight
