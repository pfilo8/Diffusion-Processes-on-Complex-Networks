import sys


class Vertex:
    """ Class representing Vertex. """

    def __init__(self, key):
        self.id = key
        self.connectedTo = dict()
        self.color = 'white'
        self.pred = None  # poprzednik(predecessor)
        self.dist = sys.maxsize
        self.disc = 0  # discovery time
        self.fin = 0  # finish time

    def addNeighbour(self, nbr, weight=1):
        self.connectedTo[nbr] = weight
        
    def removeNeighbour(self, nbr):
        for k in self.connectedTo.keys():
            if k.id == nbr:
                self.connectedTo.pop(k)
                return
        raise ValueError(f"{nbr} is not connected to {self.id}")

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def __repr__(self):
        return str(self.id)

    def getConnections(self):
        return self.connectedTo

    def getNeighbors(self):
        return list(self.connectedTo.keys())

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __getitem__(self, key):
        return self.connectedTo[key]
