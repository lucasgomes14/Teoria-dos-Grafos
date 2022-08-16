import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C', 1)
        self.g_p.adicionaAresta('a2', 'C', 'E', 1)
        self.g_p.adicionaAresta('a3', 'C', 'E', 3)
        self.g_p.adicionaAresta('a4', 'P', 'C', 2)
        self.g_p.adicionaAresta('a5', 'P', 'C', 5)
        self.g_p.adicionaAresta('a6', 'T', 'C', 2)
        self.g_p.adicionaAresta('a7', 'M', 'C', 1)
        self.g_p.adicionaAresta('a8', 'M', 'T', 1)
        self.g_p.adicionaAresta('a9', 'T', 'Z', 3)

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p2.adicionaAresta('a1', 'J', 'C')
        self.g_p2.adicionaAresta('a2', 'C', 'E')
        self.g_p2.adicionaAresta('a3', 'C', 'E')
        self.g_p2.adicionaAresta('a4', 'P', 'C')
        self.g_p2.adicionaAresta('a5', 'P', 'C')
        self.g_p2.adicionaAresta('a6', 'T', 'C')
        self.g_p2.adicionaAresta('a7', 'M', 'C')
        self.g_p2.adicionaAresta('a8', 'M', 'T')
        self.g_p2.adicionaAresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p3.adicionaAresta('a', 'J', 'C')
        self.g_p3.adicionaAresta('a2', 'C', 'E')
        self.g_p3.adicionaAresta('a3', 'C', 'E')
        self.g_p3.adicionaAresta('a4', 'P', 'C')
        self.g_p3.adicionaAresta('a5', 'P', 'C')
        self.g_p3.adicionaAresta('a6', 'T', 'C')
        self.g_p3.adicionaAresta('a7', 'M', 'C')
        self.g_p3.adicionaAresta('a8', 'M', 'T')
        self.g_p3.adicionaAresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p4.adicionaAresta('a1', 'J', 'C', 1)
        self.g_p4.adicionaAresta('a2', 'J', 'E', 1)
        self.g_p4.adicionaAresta('a3', 'C', 'E', 3)
        self.g_p4.adicionaAresta('a4', 'P', 'C', 2)
        self.g_p4.adicionaAresta('a5', 'P', 'C', 5)
        self.g_p4.adicionaAresta('a6', 'T', 'C', 2)
        self.g_p4.adicionaAresta('a7', 'M', 'C', 1)
        self.g_p4.adicionaAresta('a8', 'M', 'T', 1)
        self.g_p4.adicionaAresta('a9', 'T', 'Z', 3)

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C', 1)
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E', 3)
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C', 2)
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C', 3)
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C', 2)
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T', 2)
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z', 1)

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1', 'J', 'C', 1)
        self.g_c.adicionaAresta('a2', 'J', 'E', 3)
        self.g_c.adicionaAresta('a3', 'J', 'P', 2)
        self.g_c.adicionaAresta('a4', 'E', 'C', 3)
        self.g_c.adicionaAresta('a5', 'P', 'C', 2)
        self.g_c.adicionaAresta('a6', 'P', 'E', 2)

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria', 1)

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A', 1)
        self.g_l1.adicionaAresta('a2', 'A', 'B', 3)
        self.g_l1.adicionaAresta('a3', 'A', 'A', 1)

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B', 3)
        self.g_l2.adicionaAresta('a2', 'B', 'B', 2)
        self.g_l2.adicionaAresta('a3', 'B', 'A', 3)

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A', 2)
        self.g_l3.adicionaAresta('a2', 'C', 'C', 2)
        self.g_l3.adicionaAresta('a3', 'D', 'D', 1)
        self.g_l3.adicionaAresta('a4', 'D', 'D', 1)

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D', 3)

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C', 1)
        self.g_l5.adicionaAresta('a2', 'C', 'C', 3)

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo(['A', 'B', 'C', 'D'])

        #Grafo teste1

        self.teste1 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.teste1.adicionaAresta('1', 'A', 'B', 1)
        self.teste1.adicionaAresta('2', 'A', 'G', 3)
        self.teste1.adicionaAresta('3', 'A', 'J', 2)
        self.teste1.adicionaAresta('4', 'G', 'K', 3)
        self.teste1.adicionaAresta('5', 'K', 'J', 2)
        self.teste1.adicionaAresta('6', 'J', 'G', 2)
        self.teste1.adicionaAresta('7', 'J', 'I', 1)
        self.teste1.adicionaAresta('8', 'I', 'G', 1)
        self.teste1.adicionaAresta('9', 'G', 'H', 3)
        self.teste1.adicionaAresta('10', 'H', 'F', 1)
        self.teste1.adicionaAresta('11', 'F', 'B', 3)
        self.teste1.adicionaAresta('12', 'B', 'G', 2)
        self.teste1.adicionaAresta('13', 'B', 'C', 3)
        self.teste1.adicionaAresta('14', 'C', 'D', 2)
        self.teste1.adicionaAresta('15', 'D', 'E', 2)
        self.teste1.adicionaAresta('16', 'D', 'B', 1)
        self.teste1.adicionaAresta('17', 'B', 'E', 1)

        #Grafo teste2
        self.teste2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        self.teste2.adicionaAresta('a1', 'A', 'B', 3)
        self.teste2.adicionaAresta('a2', 'B', 'C', 1)
        self.teste2.adicionaAresta('a3', 'C', 'D', 3)
        self.teste2.adicionaAresta('a4', 'D', 'E', 2)
        self.teste2.adicionaAresta('a5', 'E', 'A', 3)
        self.teste2.adicionaAresta('a6', 'A', 'F', 2)

        self.g_g2 = MeuGrafo(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.g_g2.adicionaAresta('a1', '1', '2', 2)
        self.g_g2.adicionaAresta('a2', '2', '4', 1)
        self.g_g2.adicionaAresta('a3', '3', '2', 1)
        self.g_g2.adicionaAresta('a4', '2', '3', 3)
        self.g_g2.adicionaAresta('a5', '2', '4', 1)
        self.g_g2.adicionaAresta('a6', '2', '6', 3)
        self.g_g2.adicionaAresta('a7', '2', '5', 2)
        self.g_g2.adicionaAresta('a8', '5', '6', 3)
        self.g_g2.adicionaAresta('a9', '8', '6', 2)
        self.g_g2.adicionaAresta('a10', '7', '6', 2)
        self.g_g2.adicionaAresta('a11', '8', '7', 1)
        self.g_g2.adicionaAresta('a12', '8', '9', 1)

        self.g_g3 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        self.g_g3.adicionaAresta("a1", "A", "B", 1)
        self.g_g3.adicionaAresta("a2", "A", "D", 2)
        self.g_g3.adicionaAresta("a3", "B", "C", 1)
        self.g_g3.adicionaAresta("a4", "B", "E", 3)
        self.g_g3.adicionaAresta("a5", "C", "D", 3)
        self.g_g3.adicionaAresta("a6", "C", "E", 1)
        self.g_g3.adicionaAresta("a7", "D", "F", 5)
        self.g_g3.adicionaAresta("a8", "F", "E", 1)

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z', 'E-J', 'P-J', 'M-J', 'T-J', 'Z-J', 'Z-C', 'P-E', 'M-E', 'T-E', 'Z-E', 'M-P', 'T-P',
                          'Z-P',
                          'Z-M'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D', 'C-A', 'D-A', 'C-B', 'D-B', 'D-C'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D', 'B-A', 'C-A', 'D-A', 'C-B', 'D-B', 'D-C'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())
    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def test_dfs(self):
        self.assertEqual(set(self.g_p.dfs('J').A.keys()), set(['a1', 'a2', 'a4', 'a6', 'a8', 'a9']))
        self.assertEqual(set(self.g_p.dfs('C').A.keys()), set(['a1', 'a2', 'a4', 'a6', 'a8', 'a9']))
        self.assertEqual(set(self.g_p.dfs('E').A.keys()), set(['a2', 'a1', 'a4', 'a6', 'a8', 'a9']))
        self.assertEqual(set(self.g_p.dfs('P').A.keys()), set(['a4', 'a1', 'a2', 'a6', 'a8', 'a9']))
        self.assertEqual(set(self.g_p.dfs('M').A.keys()), set(['a7', 'a1', 'a2', 'a4', 'a6', 'a9']))
        self.assertEqual(set(self.g_p.dfs('T').A.keys()), set(['a6', 'a1', 'a2', 'a4', 'a7', 'a9']))
        self.assertEqual(set(self.g_p.dfs('Z').A.keys()), set(['a9', 'a6', 'a1', 'a2', 'a4', 'a7']))

        self.assertEqual(set(self.g_p_sem_paralelas.dfs('J').A.keys()), set(['a1', 'a2', 'a3', 'a4', 'a6', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('C').A.keys()), set(['a1', 'a2', 'a3', 'a4', 'a6', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('E').A.keys()), set(['a2', 'a1', 'a3', 'a4', 'a6', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('P').A.keys()), set(['a3', 'a1', 'a2', 'a4', 'a6', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('M').A.keys()), set(['a5', 'a1', 'a2', 'a3', 'a4', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('T').A.keys()), set(['a4', 'a1', 'a2', 'a3', 'a5', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('Z').A.keys()), set(['a7', 'a4', 'a1', 'a2', 'a3', 'a5']))

        self.assertEqual(set(self.g_c.dfs('J').A.keys()), set(['a1', 'a4', 'a6']))
        self.assertEqual(set(self.g_c.dfs('C').A.keys()), set(['a1', 'a2', 'a6']))
        self.assertEqual(set(self.g_c.dfs('E').A.keys()), set(['a2', 'a1', 'a5']))
        self.assertEqual(set(self.g_c.dfs('P').A.keys()), set(['a3', 'a1', 'a4']))

        self.assertEqual(set(self.g_c2.dfs('Nina').A.keys()), set(['amiga']))
        self.assertEqual(set(self.g_c2.dfs('Maria').A.keys()), set(['amiga']))

        self.assertEqual(set(self.teste1.dfs('A').A.keys()), set(['1', '11', '10', '9', '4', '5', '7', '13', '14', '15']))
        self.assertEqual(set(self.teste1.dfs('D').A.keys()), set(['14', '13', '1', '2', '4', '5', '7', '9', '10', '17']))

    def test_bfs(self):
        self.assertEqual(set(self.g_p.bfs('J').A.keys()), set(['a1', 'a2', 'a4', 'a6', 'a7', 'a9']))
        self.assertEqual(set(self.g_p.bfs('C').A.keys()), set(['a1', 'a2', 'a4', 'a6', 'a7', 'a9']))
        self.assertEqual(set(self.g_p.bfs('E').A.keys()), set(['a2', 'a1', 'a4', 'a6', 'a7', 'a9']))
        self.assertEqual(set(self.g_p.bfs('P').A.keys()), set(['a4', 'a1', 'a2', 'a6', 'a7', 'a9']))
        self.assertEqual(set(self.g_p.bfs('M').A.keys()), set(['a7', 'a8', 'a1', 'a2', 'a4', 'a9']))
        self.assertEqual(set(self.g_p.bfs('T').A.keys()), set(['a6', 'a8', 'a9', 'a1', 'a2', 'a4']))
        self.assertEqual(set(self.g_p.bfs('Z').A.keys()), set(['a9', 'a6', 'a8', 'a1', 'a2', 'a4']))

        self.assertEqual(set(self.g_p_sem_paralelas.bfs('J').A.keys()), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('C').A.keys()), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('E').A.keys()), set(['a2', 'a1', 'a3', 'a4', 'a5', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('P').A.keys()), set(['a3', 'a1', 'a2', 'a4', 'a5', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('M').A.keys()), set(['a5', 'a6', 'a1', 'a2', 'a3', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('T').A.keys()), set(['a4', 'a6', 'a7', 'a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('Z').A.keys()), set(['a7', 'a4', 'a6', 'a1', 'a2', 'a3']))

        self.assertEqual(set(self.g_c.bfs('J').A.keys()), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_c.bfs('C').A.keys()), set(['a1', 'a4', 'a5']))
        self.assertEqual(set(self.g_c.bfs('E').A.keys()), set(['a2', 'a4', 'a6']))
        self.assertEqual(set(self.g_c.bfs('P').A.keys()), set(['a3', 'a5', 'a6']))

        self.assertEqual(set(self.g_c2.bfs('Nina').A.keys()), set(['amiga']))
        self.assertEqual(set(self.g_c2.bfs('Maria').A.keys()), set(['amiga']))

        self.assertEqual(set(self.teste1.bfs('A').A.keys()), set(['1', '2', '3', '11', '13', '16', '17', '4', '8', '9']))
        self.assertEqual(set(self.teste1.bfs('D').A.keys()), set(['14', '15', '16', '1', '11', '12', '3', '10', '4', '8']))
        self.assertEqual(set(self.g_d.bfs('A').A.keys()), set(['asd']))

    def test_ciclo(self):
        self.assertEqual(self.g_p.ha_ciclo(), ['C', 'a2', 'E', 'a3', 'C'])
        self.assertEqual(self.g_p_sem_paralelas.ha_ciclo(), ['C', 'a4', 'T', 'a6', 'M', 'a5', 'C'])
        self.assertEqual(self.g_c.ha_ciclo(), ['J', 'a1', 'C', 'a4', 'E', 'a2', 'J'])
        self.assertFalse(self.g_c2.ha_ciclo())
        self.assertFalse(self.g_c3.ha_ciclo())
        self.assertEqual(self.g_l1.ha_ciclo(), ['A', 'a1', 'A'])
        self.assertEqual(self.g_l2.ha_ciclo(), ['B', 'a2', 'B'])
        self.assertEqual(self.g_l3.ha_ciclo(), ['C', 'a2', 'C'])
        self.assertEqual(self.g_l4.ha_ciclo(), ['D', 'a1', 'D'])
        self.assertEqual(self.g_l5.ha_ciclo(), ['C', 'a2', 'C'])
        self.assertFalse(self.g_d.ha_ciclo())
        self.assertFalse(self.g_d2.ha_ciclo())
        self.assertEqual(self.teste1.ha_ciclo(), ['A', '1', 'B', '11', 'F', '10', 'H', '9', 'G', '2', 'A'])
        self.assertEqual(self.teste2.ha_ciclo(), ['A', 'a1', 'B', 'a2', 'C', 'a3', 'D', 'a4', 'E', 'a5', 'A'])

    def test_caminho(self):
        self.assertEqual(self.g_p.caminho(2), ['J', 'a1', 'C', 'a7', 'M'])
        self.assertEqual(self.g_p.caminho(4), ['J', 'a1', 'C', 'a7', 'M', 'a8', 'T', 'a9', 'Z'])
        self.assertEqual(self.g_p.caminho(8), False)
        self.assertEqual(self.g_g1.caminho(5), ['A', '3', 'J', '5', 'K', '4', 'G', '9', 'H', '10', 'F'])
        self.assertEqual(self.g_g1.caminho(9), ['A', '3', 'J', '5', 'K', '4', 'G', '9', 'H', '10', 'F', '11', 'B', '13', 'C', '14', 'D', '15', 'E'])
        self.assertEqual(self.g_g1.caminho(12), False)
        self.assertEqual(self.g_g2.caminho(4), ['1', 'a1', '2', 'a7', '5', 'a8', '6', 'a10', '7'])
        self.assertEqual(self.g_g2.caminho(6), ['1', 'a1', '2', 'a7', '5', 'a8', '6', 'a10', '7', 'a11', '8', 'a12', '9'])
        self.assertEqual(self.g_g2.caminho(7), False)

    def test_conexo(self):
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_p_sem_paralelas.conexo())
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_p3.conexo())
        self.assertTrue(self.g_p4.conexo())

        self.assertTrue(self.g_c.conexo())
        self.assertTrue(self.g_c2.conexo())
        self.assertTrue(self.g_c3.conexo())

        self.assertFalse(self.g_l1.conexo())
        self.assertFalse(self.g_l2.conexo())
        self.assertFalse(self.g_l3.conexo())
        self.assertTrue(self.g_l4.conexo())
        self.assertTrue(self.g_l5.conexo())

        self.assertFalse(self.g_d.conexo())
        self.assertFalse(self.g_d2.conexo())

        self.assertTrue(self.teste1.conexo())
        self.assertTrue(self.teste2.conexo())

    def test_dijstra(self):
        self.assertEqual(self.g_p.dijkstra_drone('J', 'Z'), ['J', 'a1', 'C', 'a6', 'T', 'a9', 'Z'])
        self.assertEqual(self.g_p.dijkstra_drone('P', 'M'), ['P', 'a4', 'C', 'a7', 'M'])

        self.assertEqual(self.g_p4.dijkstra_drone('Z', 'J'), ['Z', 'a9', 'T', 'a6', 'C', 'a1', 'J'])
        self.assertEqual(self.g_p4.dijkstra_drone('E', 'M'), ['E', 'a2', 'J', 'a1', 'C', 'a7', 'M'])

        self.assertEqual(self.g_p_sem_paralelas.dijkstra_drone('T', 'E'), ['T', 'a4', 'C', 'a2', 'E'])
        self.assertEqual(self.g_p_sem_paralelas.dijkstra_drone('P', 'E'), ['P', 'a3', 'C', 'a2', 'E'])

        self.assertEqual(self.g_c.dijkstra_drone('J', 'P'), ['J', 'a3', 'P'])
        self.assertEqual(self.g_c.dijkstra_drone('P', 'E'), ['P', 'a6', 'E'])

        self.assertEqual(self.g_c2.dijkstra_drone('Nina', 'Maria'), ['Nina', 'amiga', 'Maria'])
        self.assertEqual(self.g_c2.dijkstra_drone('Maria', 'Nina'), ['Maria', 'amiga', 'Nina'])

        self.assertEqual(self.g_l1.dijkstra_drone('A', 'B'), ['A', 'a2', 'B'])
        self.assertEqual(self.g_l1.dijkstra_drone('B', 'A'), ['B', 'a2', 'A'])

        self.assertEqual(self.g_l2.dijkstra_drone('B', 'A'), ['B', 'a1', 'A'])
        self.assertEqual(self.g_l2.dijkstra_drone('A', 'B'), ['A', 'a1', 'B'])

        self.assertEqual(self.g_l3.dijkstra_drone('C', 'A'), ['C', 'a1', 'A'])
        self.assertEqual(self.g_l3.dijkstra_drone('C', 'C'), ['C'])

        self.assertEqual(self.g_l5.dijkstra_drone('D', 'C'), ['D', 'a1', 'C'])
        self.assertEqual(self.g_l5.dijkstra_drone('C', 'C'), ['C'])

        self.assertEqual(self.teste1.dijkstra_drone('C', 'J'), ['C', '13', 'B', '1', 'A', '3', 'J'])
        self.assertEqual(self.teste1.dijkstra_drone('H', 'A'), ['H', '10', 'F', '11', 'B', '1', 'A'])

        self.assertEqual(self.teste2.dijkstra_drone('E', 'B'), ['E', 'a5', 'A', 'a1', 'B'])
        self.assertEqual(self.teste2.dijkstra_drone('C', 'F'), ['C', 'a2', 'B', 'a1', 'A', 'a6', 'F'])

        self.assertEqual(self.g_g2.dijkstra_drone('1', '9'), ['1', 'a1', '2', 'a6', '6', 'a9', '8', 'a12', '9'])
        self.assertEqual(self.g_g2.dijkstra_drone('3', '5'), ['3', 'a3', '2', 'a7', '5'])

        self.assertEqual(self.g_g3.dijkstra_drone('A', 'F'), ['A', 'a1', 'B', 'a3', 'C', 'a6', 'E', 'a8', 'F'])
		self.assertEqual(self.g_g3.dijkstra_drone('D', 'F'), ['D', 'a7', 'F'])