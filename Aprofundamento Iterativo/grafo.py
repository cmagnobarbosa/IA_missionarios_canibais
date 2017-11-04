# encoding:utf-8
from collections import defaultdict
"""
Busca em Profundidade Iterativa
Carlos Magno, Lucas Félix, Matheus Reis, Samuel Ribeiro
IA - Missionarios e Canibais
"""


class espaco_de_busca():
    """Armazena o espaço de Busca"""

    def __init__(self):
        self.grafo = defaultdict(list)
        self.final = []
        self.m_esq = 3
        self.c_esq = 3
        self.m_dir = 0
        self.c_dir = 0
        self.b = 1
        self.sucesso = 0
        self.v_canibal = 1
        self.iteracoes = 10
        self.estados_validos = []

    def erro_numero(self, motivo):
        print "O numero de " + motivo + " é inferior a 0."

    def volta_canibal(self, numero):
        "Desloca o canibal da direita para esquerda.."
        if(self.c_dir >= 0):
            self.c_dir = self.c_dir - numero
            self.c_esq = self.c_esq + numero
            self.b = 1
            return self.regra_geral()
        self.erro_numero("canibais")
        return False

    def desloca_canibal(self, numero):
        "Desloca canibal da esquerda para a direita.."
        if((self.c_esq - numero) >= 0 and self.b is 1):
            self.c_esq = self.c_esq - numero
            self.c_dir = self.c_dir + numero
            self.b = 0
            return self.regra_geral()
        self.erro_numero("canibais")
        return False

    def volta_missionario(self, numero):
        "Retorna com o missionario..."
        if((self.m_dir - numero) >= 0):
            self.m_dir = self.m_dir - numero
            self.m_esq = self.m_esq + numero
            self.b = 1
            return self.regra_geral()
        self.erro_numero("missionarios")
        return False

    def volta_m_c(self, numero):
        "Desloca Missionário e Canibais"
        if((self.m_dir - numero) >= 0 and (self.c_esq - numero) >= 0):
            self.m_dir -= numero
            self.c_dir -= numero
            self.c_esq += numero
            self.m_dir += numero
            self.b = 1
            return self.regra_geral()
        self.erro_numero("Canibais e Missionários")
        return False

    def desloca_missionario(self, numero):
        "Desloca o missionario..."
        if((self.m_esq - numero) >= 0 and self.b is 1):
            self.m_esq = self.m_esq - numero
            self.m_dir = self.m_dir + numero
            self.b = 0
            return self.regra_geral()
        self.erro_numero("missionarios")
        return False

    def estado(self):
        "Retorna o estado atual de canibais e missionarios"
        return (self.c_esq, self.m_esq, self.b)

    def regra_geral(self):
        "Regra geral"
        if(((self.c_esq > self.m_esq) or (self.c_dir > self.m_dir))and self.m_dir > 0):
            if(self.m_esq > 0):
                print "Regra não respeitada. O número de canibais é superior a missionários"
                return False
        return True

    def atualiza_estados(self, estado):
        "Atualiza os estados.."
        self.c_esq = estado[0]
        self.m_esq = estado[1]
        self.b = estado[2]

    def salva_caminho(self, estado):
        "Verifica o caminho..."
        if(self.verifica_sucesso(estado)):
            if(estado not in self.estados_validos):
                self.estados_validos.append(estado)
            else:
                print "Caminho já verificado..", estado
                return False
        else:
            self.estados_validos.append(estado)

    def verifica_sucesso(self, estado):
        if((estado[0] + estado[1] + estado[2]) is 0):
            print "Estado de suceso encontrado."
            self.sucesso = 1
            return False
        return True

    def gera_estados(self):
        "Gera a arvore de estados.."
        max_d_canibal = 2
        max_d_missionario = 2
        retorno_padrao = 1
        estado = self.estado()
        print estado
        self.estados_validos.append(estado)
        "Realiza as iterações em busca da solução."
        for i in range(0, self.iteracoes):
            if(self.regra_geral() and self.sucesso is 0):
                if(self.v_canibal is 1):
                    if(self.desloca_canibal(max_d_canibal)):
                        estado = self.estado()
                        print estado
                        self.salva_caminho(estado)
                        self.volta_canibal(retorno_padrao)
                        estado = self.estado()
                        print estado
                        self.salva_caminho(estado)
                    else:
                        #
                        print "erro", self.estado()
                        max_d_canibal -= 1
                        self.v_canibal = 0
                        print "Vez do Missionário"
                elif(self.v_canibal is 0):
                    if(self.desloca_missionario(max_d_missionario)):
                        print self.estado()
                        self.salva_caminho(self.estado())
                        if(self.volta_missionario(retorno_padrao)):
                            print self.estado()
                            self.salva_caminho(self.estado())
                        else:
                            if(self.volta_m_c(retorno_padrao)):
                                print self.estado()
                                self.salva_caminho(self.estado())
                            if(self.regra_geral() is False):
                                # corrige o estado.
                                last = self.estados_validos[
                                    len(self.estados_validos) - 1]
                                self.atualiza_estados(last)
                                self.volta_canibal(max_d_canibal)
                            print "Estado", self.estado()
                    else:
                        self.v_canibal = 1
                        print "Vez do Canibal", i
                        max_d_canibal = 2
                        max_d_missionario -= 1
                        self.salva_caminho(self.estado())
            else:
                last = self.estados_validos[len(self.estados_validos) - 1]
                self.atualiza_estados(last)
        self.estados_validos.pop()
        print "Caminho ", self.estados_validos
        print "Os estados foram gerados."

    def addEdge(self, v, a):
        """Adiciona um elemnto no grafo"""
        self.grafo[v].append(a)

    def gera_arvore(self):
        """Gera à árvore de estados"""
        print "Gerando à árvore.."
        print "Número de estados", len(self.estados_validos)
        for i in range(0, len(self.estados_validos)):
            if(i + 1 < len(self.estados_validos)):
                self.addEdge(
                    (self.estados_validos[i]), (self.estados_validos[i + 1]))

    def gera_espaco_de_busca(self):
        """Gera o Espaço de Busca"""
        self.gera_estados()
        self.gera_arvore()
