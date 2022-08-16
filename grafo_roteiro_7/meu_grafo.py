from copy import deepcopy

from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from sys import maxsize

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
                if (self.A[i1].getV1() == self.A[i2].getV1()) and (self.A[i1].getV2() == self.A[i2].getV2()) or \
                        (self.A[i1].getV1() == self.A[i2].getV2()) and (self.A[i1].getV2() == self.A[i2].getV1()):
                    cont += 1

            if cont > 0:
                saida = True
                break

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


    def dfs(self, V = ""):
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
                                grafo_dfs.adicionaAresta(i2, i1, self.A[i2].getV2())
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
                                grafo_dfs.adicionaAresta(i2,self.A[i2].getV1(), i1)
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
        para = 0
        if V == self.N[0]:
            para = 1
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
                                grafo_bfs.adicionaAresta(i2, i1, self.A[i2].getV2())


                        elif i1 == self.A[i2].getV2():
                            contadorLista = 0

                            for i3 in listaVertices:
                                if self.A[i2].getV1() == i3:
                                    contadorLista = 1
                                    break
                            if contadorLista == 0:
                                listaVertices.append(self.A[i2].getV1())
                                grafo_bfs.adicionaVertice(self.A[i2].getV1())
                                grafo_bfs.adicionaAresta(i2, self.A[i2].getV1(), i1)

                        if len(listaVertices) == contadorVertices:
                            break

                        if i2 == ultimaAresta:
                            contadorDeIndices += 1
                            if contadorArestas - 1 == i:
                                return grafo_bfs
                            if para == 1 and i1 == self.N[-1]:
                                return grafo_bfs
                            if len(listaVertices) == contadorDeIndices:
                                return grafo_bfs
                            V = listaVertices[contadorDeIndices]

        return grafo_bfs

    def vertice_adjacente(self, V=''):
        lista = []

        for i in self.N:
            if V == i:
                for j in self.A:
                    condicao = False
                    if i == self.A[j].getV1():
                        for i2 in range(len(lista)):
                            if lista[i2] == self.A[j].getV2():
                                condicao = True
                        if condicao == False:
                            lista.append(self.A[j].getV2())
                    elif i == self.A[j].getV2():
                        for i2 in range(len(lista)):
                            if lista[i2] == self.A[j].getV1():
                                condicao = True
                        if condicao == False:
                            lista.append(self.A[j].getV1())

        return lista

    def se_tem_ciclo(self, V=''):
        lista = []

        if self.ha_laco():
            for i in self.A:
                if self.A[i].getV1() == self.A[i].getV2():
                    lista.append(self.A[i].getV1())
                    lista.append(i)
                    lista.append(self.A[i].getV2())
                    return lista

        elif self.ha_paralelas():
            for i in self.N:
                if i == V:
                    for i1 in self.A:
                        cont = 0
                        for i2 in self.A:
                            if self.A[i1].getV1() == self.A[i2].getV1() or self.A[i1].getV1() == self.A[i1].getV2():
                                if self.A[i1].getV2() == self.A[i1].getV1() or self.A[i1].getV2() == self.A[i1].getV2():
                                    if cont > 0:
                                        lista.append(self.A[i1].getV1())
                                        lista.append(i1)
                                        if self.A[i1].getV1() == lista[0]:
                                            lista.append(self.A[i1].getV2())
                                        else:
                                            lista.append(self.A[i1].getV1())
                                        lista.append(i2)
                                        lista.append(self.A[i1].getV1())
                                        return lista
                                    cont += 1
            return False

        elif self.grau(V) >= 2:
            return True
        return False

    def aux_ciclo(self, V = ''):
        listaVertice = [V]
        listaAresta = []
        lista = []

        for i in range(len(self.N)):
            if self.se_tem_ciclo(V) == True:
                a = self.vertice_adjacente(V)
                for i1 in range(len(a)):
                    condicao = 0
                    for i2 in range(len(listaVertice)):
                        if listaVertice[i2] == a[i1]:
                            condicao = 1
                            break
                    if self.grau(a[i1]) >= 2 and a[i1] != listaVertice[i2] and condicao == 0:
                        V = a[i1]
                        listaVertice.append(a[i1])
                        for i3 in self.A:
                            if self.A[i3].getV1() == listaVertice[-2] or self.A[i3].getV2() == listaVertice[-2]:
                                if self.A[i3].getV1() == listaVertice[-1] or self.A[i3].getV2() == listaVertice[-1]:
                                    listaAresta.append(i3)
                                    break
                        break
                    elif self.grau(a[i1]) >= 2 and a[i1] == listaVertice[0] and i != 1:
                        listaVertice.append(a[i1])
                        for i3 in self.A:
                            if self.A[i3].getV1() == listaVertice[-2] or self.A[i3].getV2() == listaVertice[-2]:
                                if self.A[i3].getV1() == listaVertice[-1] or self.A[i3].getV2() == listaVertice[-1]:
                                    listaAresta.append(i3)
                        for j in range(len(listaAresta)):
                            lista.append(listaVertice[j])
                            lista.append(listaAresta[j])

                        lista.append(listaVertice[-1])
                        return lista

        return False

    def ha_ciclo(self):
        for i in self.N:
            a = self.se_tem_ciclo(i)
            if a == False:
                continue

            elif a == True:
                x = self.aux_ciclo(i)
                if x == False:
                    continue
                return x
            else:
                return a
        return False

    def __gerarVerticesAdjacencentes(self):

        verticesAdjacentes = {}

        for aresta in self.A:
            arestaAtual = self.A[aresta]
            if arestaAtual.getV1() not in verticesAdjacentes:
                verticesAdjacentes[arestaAtual.getV1()] = [(arestaAtual.getV2(), aresta)]
            else:
                verticesAdjacentes[arestaAtual.getV1()].append((arestaAtual.getV2(), aresta))

            if arestaAtual.getV2() not in verticesAdjacentes:
                verticesAdjacentes[arestaAtual.getV2()] = [(arestaAtual.getV1(), aresta)]
            else:
                verticesAdjacentes[arestaAtual.getV2()].append((arestaAtual.getV1(), aresta))

        return verticesAdjacentes

    def __dfs_melhor_proximo_caminho(self, V, distancias, verticesAdjacentes):

        if V not in verticesAdjacentes: return

        for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[V]:
            if verticeAdjacente not in distancias:
                distancias[verticeAdjacente] = distancias[V] + 1
                self.__dfs_melhor_proximo_caminho(verticeAdjacente, distancias, verticesAdjacentes)

    def __dfs_caminho(self, V, visitados, caminho, verticesAdjacentes):
        maiorCaminho = -1
        melhorVertice = None
        arestaMelhorVertice = None

        novoGrafo = deepcopy(self)
        for v in visitados:
            if novoGrafo.existeVertice(v):
                novoGrafo.removeVertice(v)

        verticesAdjNovoGrafo = novoGrafo.__gerarVerticesAdjacencentes()

        for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[V]:
            if verticeAdjacente not in visitados:
                distancias = {verticeAdjacente: 0}
                novoGrafo.__dfs_melhor_proximo_caminho(verticeAdjacente, distancias, verticesAdjNovoGrafo)

                distanciaMaxima = -1
                for key, value in distancias.items():
                    if value > distanciaMaxima: distanciaMaxima = value

                if distanciaMaxima > maiorCaminho:
                    maiorCaminho = distanciaMaxima
                    melhorVertice = verticeAdjacente
                    arestaMelhorVertice = rotuloAresta

        if melhorVertice != None:
            visitados.add(melhorVertice)

            caminho.append(arestaMelhorVertice)
            caminho.append(melhorVertice)

            self.__dfs_caminho(melhorVertice, visitados, caminho, verticesAdjacentes)

    def caminho(self, n):

        if n <= 0: return False

        verticesAdjacentes = self.__gerarVerticesAdjacencentes()

        for v in self.N:
            if v not in verticesAdjacentes: continue

            visitados = set([v])
            caminho = [v]
            self.__dfs_caminho(v, visitados, caminho, verticesAdjacentes)

            if n < len(visitados):
                return caminho[:2 * n + 1]

        return False

    def conexo(self):
        bfs = self.bfs(self.N[0])
        quantidadeVerticeBFS = len(bfs.N)
        quantidadeVerticeGrafoOriginal = len(self.N)

        if quantidadeVerticeBFS == quantidadeVerticeGrafoOriginal:
            return True
        return False

    def dijkstra_drone(self, U = '', V = ''):
        listaMenorCaminho = []
        listaVisitados = []
        listaAntecessor = []
        W = U
        listaArestas = []

        indiceZero = self.N.index(U)

        for i in range(len(self.N)):
            listaVisitados.insert(i, 0)
            listaMenorCaminho.insert(i, maxsize)
            listaAntecessor.append(0)

        for i1 in range(len(self.N)):
            for i2 in self.A:
                if self.A[i2].getV1() == W:
                    indiceVertice = self.N.index(self.A[i2].getV2())
                    listaVisitados[self.N.index(W)] = 1
                    if i1 == 0:
                        listaMenorCaminho[indiceVertice] = self.A[i2].getPeso()
                        listaAntecessor[indiceVertice] = self.A[i2].getV1()

                    elif listaVisitados[indiceVertice] == 0 and \
                            (self.A[i2].getPeso() + listaMenorCaminho[self.N.index(W)]) < listaMenorCaminho[indiceVertice]:
                        listaMenorCaminho[indiceVertice] = self.A[i2].getPeso() + listaMenorCaminho[self.N.index(W)]
                        listaAntecessor[indiceVertice] = self.A[i2].getV1()

                elif self.A[i2].getV2() == W:
                    indiceVertice = self.N.index(self.A[i2].getV1())
                    listaVisitados[self.N.index(W)] = 1

                    if i1 == 0:
                        listaMenorCaminho[indiceVertice] = self.A[i2].getPeso()
                        listaAntecessor[indiceVertice] = self.A[i2].getV2()

                    elif listaVisitados[indiceVertice] == 0 and \
                            (self.A[i2].getPeso() + listaMenorCaminho[self.N.index(W)]) < listaMenorCaminho[indiceVertice]:
                        listaMenorCaminho[indiceVertice] = self.A[i2].getPeso() + listaMenorCaminho[self.N.index(W)]
                        listaAntecessor[indiceVertice] = self.A[i2].getV2()

            menorCaminho = maxsize

            for i3 in range(len(listaMenorCaminho)):
                if listaMenorCaminho[i3] < menorCaminho and listaVisitados[i3] == 0:
                    indiceMenorCaminho = i3
                    menorCaminho = listaMenorCaminho[i3]

            W = self.N[indiceMenorCaminho]

            if W == V:
                break
        listaVertices = []
        posicaoV = self.N.index(V)

        for j in range(len(self.N)):
            if posicaoV == self.N.index(U):
                listaVertices.append(V)
                break

            listaVertices.insert(0, listaAntecessor[posicaoV])
            posicaoV = self.N.index(listaAntecessor[posicaoV])

        for j1 in range(len(listaVertices) - 1):
            for j2 in self.A:
                if (self.A[j2].getV1() == listaVertices[j1] and self.A[j2].getV2() == listaVertices[j1 + 1]) \
                    or (self.A[j2].getV2() == listaVertices[j1] and self.A[j2].getV1() == listaVertices[j1 + 1]):
                    listaArestas.append(j2)
                    break

        listaFinal = []

        for j3 in range(len(listaVertices)):
            listaFinal.append(listaVertices[j3])
            if j3 < len(listaArestas):
                listaFinal.append(listaArestas[j3])

        return listaFinal