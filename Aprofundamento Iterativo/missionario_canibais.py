# encoding: utf-8
"""
Busca em Profundidade Iterativa
Carlos Magno, Lucas Félix, Matheus Reis, Samuel Ribeiro
IA - Missionarios e Canibais
"""
from grafo import espaco_de_busca


class aprofundamento():
    """Aprofundamento Iterativo"""

    def __init__(self):
        self.espaco = espaco_de_busca()
        self.espaco.gera_espaco_de_busca()
        self.caminho = []

    def verifica_estado(self, origem, alvo):
        """Verifica o estado objetivo"""
        for i in range(0, len(origem)):
            if(origem[i] is not alvo[i]):
                return False
        return True

    def dfs_iterativo(self, origem, max_profundidade, alvo):
        """Limita a profundidade"""
        for profundidade in range(0, max_profundidade):
            elemento = self.dfs(origem, profundidade, alvo)
            if elemento is not None:
                return elemento

    def dfs(self, origem, profundidade, alvo):
        """Aplica o DFS"""
        # print origem
        self.caminho.append(origem)
        if profundidade is 0 and self.verifica_estado(origem, alvo):
            return origem
        if profundidade > 0:
            for no in self.espaco.grafo[origem]:
                # print no, deep
                elemento = self.dfs(no, profundidade - 1, alvo)
                if elemento is not None:
                    return elemento
        return None

    def main(self):
        elemento = self.dfs_iterativo((3, 3, 1), 12, (0, 0, 0))
        if(elemento is None):
            print "Elemento não encontrado."
        else:
            print "Iniciando a Pesquisa..."
            print "Pesquisa Iniciada do elemento: ", (3, 3, 1)
            print "Elemento encontrado: ", elemento
            print "Caminho da Pesquisa:"
            print self.caminho
if __name__ == '__main__':
    dsf = aprofundamento()
    dsf.main()
