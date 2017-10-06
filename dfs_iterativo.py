# encoding: utf-8
"""
Pseudo Código do DFS iterativo
function IDDFS(root,max_deep,goal)
    for depth from 0 to ∞
        found ← DLS(root, depth,goal)
        if found ≠ null
            return found

function DLS(node, depth,goal)
    if depth = 0 and node is a goal
        return node
    if depth > 0
        foreach child of node
            found ← DLS(child, depth−1)
            if found ≠ null
                return found
    return null
"""
from collections import defaultdict

# Estado Inicial
"""
(C,M,B)
(3,3,1)
Barco
1 - Esquerda
0- Direita

Estado Final
(0,0,0)

"""
# default dictionary to store graph
graph = defaultdict(list)

# function to add an edge to graph

caminho = []


def addEdge(u, v):
    graph[u].append(v)


def verifica_estado(origem, alvo):
    for i in range(0, len(origem)):
        if(origem[i] is not alvo[i]):
            return False
    return True


def dfs_iterativo(origem, max_deep, alvo):
    """Limita a profundidade"""
    for deep in range(0, max_deep):
        elemento = dfs(origem, deep, alvo)
        if elemento is not None:
            return elemento


def dfs(origem, deep, alvo):
    """Aplica o DFS"""
    if deep is 0 and verifica_estado(origem, alvo):
        return origem
    if deep > 0:
        for no in graph[origem]:
            # print no, deep
            elemento = dfs(no, deep - 1, alvo)
            if elemento is not None:
                return elemento
    return None

addEdge((3, 3, 1), (3, 2, 1))
addEdge((3, 3, 1), (4, 5, 6))
addEdge((3, 2, 1), (0, 0, 3))
addEdge((0, 0, 3), (0, 0, 0))
# print graph
print dfs_iterativo((3, 3, 1), 4, (0, 0, 0))
# print graph[(3, 3, 1)][0]
# print graph
