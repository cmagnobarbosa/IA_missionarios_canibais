# encoding:utf-8
from collections import defaultdict


class espaco_de_busca():
    """Armazena o espaço de Busca"""

    def __init__(self):
        self.grafo = defaultdict(list)

    def addEdge(self, v, a):
        """Adiciona um elemnto no grafo"""
        self.grafo[v].append(a)

    def gera_espaco_de_busca(self):
        """Gera o Espaço de Busca"""
        #-----------------------------
        self.addEdge((3, 3, 1), (2, 2, 0))
        self.addEdge((3, 3, 1), (2, 3, 0))
        self.addEdge((3, 3, 1), (1, 3, 0))
        self.addEdge((3, 3, 1), (3, 2, 0))
        self.addEdge((3, 3, 1), (3, 1, 0))

        #-----------------------------
        self.addEdge((2, 2, 0), (2, 3, 1))
        self.addEdge((2, 2, 0), (3, 2, 1))

        # #----------------------------
        self.addEdge((3, 2, 1), (1, 2, 0))
        self.addEdge((3, 2, 1), (2, 1, 0))
        self.addEdge((3, 2, 1), (3, 0, 0))

        #-------------------------------------
        self.addEdge((3, 0, 0), (3, 1, 1))

        #------------------------------
        self.addEdge((3, 1, 1), (1, 1, 0))
        self.addEdge((3, 1, 1), (2, 0, 0))

        #------------------------------
        self.addEdge((1, 1, 0), (2, 2, 1))
        self.addEdge((1, 1, 0), (2, 1, 1))
        self.addEdge((1, 1, 0), (1, 2, 1))
        self.addEdge((1, 1, 0), (1, 3, 1))

        # #--------------------------------
        self.addEdge((2, 2, 1), (0, 2, 0))
        self.addEdge((0, 2, 0), (0, 3, 1))

        #--------------------------------

        self.addEdge((0, 3, 1), (1, 2, 1))
        self.addEdge((0, 3, 1), (0, 1, 0))

        #--------------------------------
        self.addEdge((0, 1, 0), (1, 1, 1))
        self.addEdge((0, 1, 0), (0, 2, 1))
        #--------------------------------
        self.addEdge((0, 2, 1), (0, 0, 0))
        #-------------------------------
        self.addEdge((1, 1, 1), (0, 0, 0))
        #--------------------------------
