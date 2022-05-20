import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *


class TestGrafodfs(unittest.TestCase):

    def setUp(self):
        #Grafo teste
        self.g_p = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.g_p.adicionaAresta('1', 'A', 'B')
        self.g_p.adicionaAresta('2', 'A', 'G')
        self.g_p.adicionaAresta('3', 'A', 'J')
        self.g_p.adicionaAresta('4', 'G', 'K')
        self.g_p.adicionaAresta('5', 'K', 'J')
        self.g_p.adicionaAresta('6', 'J', 'G')
        self.g_p.adicionaAresta('7', 'J', 'I')
        self.g_p.adicionaAresta('8', 'I', 'G')
        self.g_p.adicionaAresta('9', 'G', 'H')
        self.g_p.adicionaAresta('10', 'H', 'F')
        self.g_p.adicionaAresta('11', 'F', 'B')
        self.g_p.adicionaAresta('12', 'B', 'G')
        self.g_p.adicionaAresta('13', 'B', 'C')
        self.g_p.adicionaAresta('14', 'C', 'D')
        self.g_p.adicionaAresta('15', 'D', 'E')
        self.g_p.adicionaAresta('16', 'D', 'B')
        self.g_p.adicionaAresta('17', 'E', 'B')


        #como deve ficar
        self.dfs = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.dfs.adicionaAresta('1', 'A', 'B')
        self.dfs.adicionaAresta('13', 'B', 'C')
        self.dfs.adicionaAresta('14', 'C', 'D')
        self.dfs.adicionaAresta('15', 'D', 'E')
        self.dfs.adicionaAresta('11', 'B', 'F')
        self.dfs.adicionaAresta('10', 'F', 'H')
        self.dfs.adicionaAresta('9', 'H', 'G')
        self.dfs.adicionaAresta('8', 'G', 'I')
        self.dfs.adicionaAresta('7', 'I', 'J')
        self.dfs.adicionaAresta('6', 'J', 'K')

    def test_dfs(self):
        self.assertTrue(self.dfs.test_dfs())