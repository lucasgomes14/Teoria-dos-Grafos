from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        vna = set()

        for v1 in self.N:
            for v2 in self.N:
                achei = False
                for i in self.A:
                    if v1 != v2:
                        if(v1 == self.A[i].getV1() and v2 == self.A[i].getV2()) or \
                          (v2 == self.A[i].getV1() and v1 == self.A[i].getV2()):
                            achei = True
                if not achei and v1 != v2:
                    vna.add("{}-{}".format(v1, v2))

        return vna

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in self.A:
            if self.A[i].getV1() == self.A[i].getV2():
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        cont = 0
        tvertice = False

        for i in self.N:
            if i == V:
                tvertice = True

                for j in self.A:
                    if i == self.A[j].getV1() and i == self.A[j].getV2():
                        cont += 2
                    elif i == self.A[j].getV1() or i == self.A[j].getV2():
                        cont += 1

        if cont == 0 and tvertice == False:
            raise VerticeInvalidoException
        else:
            return cont

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

        saida = False
        for i1 in self.A:
            cont = -1
            for i2 in self.A:
                if (self.A[i1].getV1() == self.A[i2].getV1()) or (self.A[i1].getV1() == self.A[i2].getV2()):
                    if (self.A[i1].getV2() == self.A[i2].getV1()) or (self.A[i1].getV2() == self.A[i2].getV2()):
                        cont += 1

            if cont > 0:
                saida = True

        return saida

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        existe = False
        saida = set()

        for i1 in self.N:
            if V == i1:
                existe = True
            for i2 in self.A:
                if V == self.A[i2].getV1() or V == self.A[i2].getV2():
                    saida.add("{}". format(i2))

        if existe == False:
            raise VerticeInvalidoException

        else:
            return saida

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        tem_laco = self.ha_laco()
        tem_paralela = self.ha_paralelas()
        e_completo = False
        tamanho = len(self.N)
        cont_e_completo = 0

        for i1 in self.N:
            for i2 in self.A:
                if i1 == self.A[i2].getV1() or i1 == self.A[i2].getV2():
                    if i1 != self.A[i2].getV1() or i1 != self.A[i2].getV2():
                        cont_e_completo += 1

        if cont_e_completo == ((tamanho - 1) * tamanho):
            e_completo = True

        if tem_laco == True or tem_paralela == True:
            e_completo = False

        return e_completo

    def dfs(self, V=""):
        grafo_dfs = GrafoListaAdjacencia()

        listaVertices = []
        listaAresta = []
        contadorWhile = 0
        laco = self.ha_laco()

        for j in self.N:
            if j == V:
                listaVertices.append(j)
                grafo_dfs.adicionaVertice(j)
                break

        for x in self.A:
            contadorWhile += 1

        for z in range(contadorWhile):
            for i1 in self.N:
                if i1 == V:

                    for i2 in self.A:
                        paralela = 0
                        if i1 == self.A[i2].getV1():
                            contador = 0
                            for i3 in listaVertices:
                                if i3 == self.A[i2].getV2():
                                    contador += 1
                                    break
                            if contador == 0:
                                listaVertices.append(self.A[i2].getV2())
                                grafo_dfs.adicionaVertice(self.A[i2].getV2())
                                grafo_dfs.adicionaAresta(
                                    i2, i1, self.A[i2].getV2())
                                if (self.ha_paralelas() == True) and (self.grau(V) == 2):
                                    V = self.A[i2].getV2()
                                    paralela = 1
                                    break
                                else:
                                    V = self.A[i2].getV2()
                                    break
                            if paralela == 0:
                                contadorVoltar = 0
                                for i5 in self.A:
                                    if (V == self.A[i5].getV1() or V == self.A[i5].getV2()):
                                        for i6 in listaVertices:
                                            if i6 == self.A[i5].getV1() or i6 == self.A[i5].getV2():
                                                contadorVoltar += 1
                                if contadorVoltar/2 == self.grau(V):
                                    V = self.A[i2].getV2()

                        elif i1 == self.A[i2].getV2():
                            contador = 0
                            for i4 in listaVertices:
                                if i4 == self.A[i2].getV1():
                                    contador += 1
                                    break
                            if contador == 0:
                                listaVertices.append(self.A[i2].getV1())
                                grafo_dfs.adicionaVertice(self.A[i2].getV1())
                                grafo_dfs.adicionaAresta(
                                    i2, self.A[i2].getV1(), i1)
                                contadorAresta = 0

                                if (self.ha_paralelas() == True) and (self.grau(V) == 2):
                                    paralela = 1
                                    V = self.A[i2].getV2()
                                    break
                                else:
                                    V = self.A[i2].getV1()
                                    break
                            if paralela == 0:
                                contadorVoltar = 0
                                for i5 in self.A:
                                    if (V == self.A[i5].getV1() or V == self.A[i5].getV2()):
                                        for i6 in listaVertices:
                                            if i6 == self.A[i5].getV1() or i6 == self.A[i5].getV2():
                                                contadorVoltar += 1
                                if contadorVoltar/2 == self.grau(V):
                                    V = self.A[i2].getV1()

        return grafo_dfs

	def bfs(self, V=""):
        listaVertices = []
        ultimaAresta = ''
        contadorDeIndices = 0
        contadorArestas = 0
        contadorVertices = 0
        laco = self.ha_laco()
        grafo_bfs = GrafoListaAdjacencia()

        for k in self.A:
            ultimaAresta = k
            contadorArestas += 1

        for j in self.N:
            contadorVertices += 1
            if j == V:
                listaVertices.append(j)
                grafo_bfs.adicionaVertice(j)

        for i in range(contadorArestas):
            for i1 in self.N:
                if i1 == V:
                    for i2 in self.A:
                        if i1 == self.A[i2].getV1():
                            contadorLista = 0

                            for i3 in listaVertices:
                                if self.A[i2].getV2() == i3:
                                    contadorLista = 1
                                    break

                            if contadorLista == 0:
                                listaVertices.append(self.A[i2].getV2())
                                grafo_bfs.adicionaVertice(self.A[i2].getV2())
                                grafo_bfs.adicionaAresta(
                                    i2, i1, self.A[i2].getV2())

                        elif i1 == self.A[i2].getV2():
                            contadorLista = 0

                            for i3 in listaVertices:
                                if self.A[i2].getV1() == i3:
                                    contadorLista = 1
                                    break
                            if contadorLista == 0:
                                listaVertices.append(self.A[i2].getV1())
                                grafo_bfs.adicionaVertice(self.A[i2].getV1())
                                grafo_bfs.adicionaAresta(
                                    i2, self.A[i2].getV1(), i1)

                        if len(listaVertices) == contadorVertices:
                            break

                        if i2 == ultimaAresta:
                            contadorDeIndices += 1
                            V = listaVertices[contadorDeIndices]

        return grafo_bfs

	def dijkstra_drone(self, vi, vf, carga: int, carga_max: int, pontos_recarga: list()):
        pass
