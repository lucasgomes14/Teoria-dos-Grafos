from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        dic = set()

        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if j < i:
                    if self.M[j][i] == {}:
                        dic.add("{}-{}".format(self.N[i], self.N[j]))
                elif j > i:
                    if self.M[i][j] == {}:
                        dic.add("{}-{}".format(self.N[i], self.N[j]))


        return dic

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.M)):
            if len(self.M[i][i]) > 0:
                return True
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        contador = 0

        if V not in self.N:
            raise VerticeInvalidoException

        index = self.N.index(V)

        for i in range(len(self.M)):
            if i < index:
                contador += len(self.M[i][index])
            elif i == index:
                contador += len(self.M[index][i]) * 2
            else:
                contador += len(self.M[index][i])

        return contador

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.M)):
            for j in range(i, len(self.M)):
                if len(self.M[i][j]) >= 2:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in  self.N:
            raise VerticeInvalidoException

        dic = set()

        index = self.N.index(V)

        for i in range(len(self.M)):
            if self.M[i][index] != {}:
                if i < index:
                    aresta = self.M[i][index]
                    for j in aresta:
                        dic.add("{}".format(j))
                else:
                    aresta = self.M[index][i]
                    for j in aresta:
                        dic.add("{}".format(j))

        return dic

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if len(self.vertices_nao_adjacentes()) == 0 and not self.ha_laco() and not self.ha_paralelas():
            return True
        return False