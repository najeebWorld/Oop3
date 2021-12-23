import unittest

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_something(self):
        #self.assertEqual(True, False)  # add assertion here
        print("\n \n testting")
        g = DiGraph()
        g.add_node(0, (0, 0, 0))
        g.add_node(1, (1.5, -2.6, 0))
        g.add_node(2, (3.251, 5.987, 0))
        g.add_node(3, (-3.25, 5.25, 0))
        g.add_edge(0, 1, 1.35)
        g.add_edge(0, 2, 5.624)
        g.add_edge(0, 3, 2.45)
        g.add_edge(1, 2, 1.2354)
        g.add_edge(1, 3, 0.54)
        g.add_edge(2, 3, 3.657)
        g.add_edge(3, 0, 2.5)
        g.add_edge(2, 1, 2.5)

        algo =GraphAlgo(g)
        l=[]
        for n in g.nodeD:
            l.append(g.nodeD[n].getId())
        #print(l)
        
        x =algo.TSP(l)
        print("tsp:", x )



        # algo.save_to_json("myjson4node")
        # algo.plot_graph()
        # x =algo.dijasktra(0)
        # print(x[0])
        # print(x[1])


        # a1 = algo.shortest_path(0, 1)
        # b1 = (1.35, [0, 1])
        # self.assertEqual(a1, b1)
        # a2 = algo.shortest_path(0, 2)
        # b2 = (2.5854, [0, 1, 2])
        # self.assertEqual(a2, b2)
        # a3 = algo.shortest_path(0, 3)
        # b3 = (1.89, [0, 1, 3])
        # self.assertAlmostEqual(a3[0], b3[0])
        # self.assertEqual(a3[1], b3[1])
        # a4 = algo.shortest_path(1, 3)
        # b4 = (0.54, [1, 3])
        # self.assertEquals(a4[0], b4[0])
        # self.assertEquals(a4[1], b4[1])
        #
        #
        #
        # y=algo.isConnected()
        # print(y)
        # self.assertTrue(y)
        # g1 = algo.get_graph()
        # g1.remove_edge(3, 0)
        # algo1 =GraphAlgo(g1)
        # y = algo1.isConnected()
        # print(y)
        # self.assertFalse(y)
        #
        # g.add_edge(3, 0, 2.5)
        # x = algo.centerPoint()
        # print("center:" ,x)
        # self.assertEqual(0,x[0])
        #
        #



        # g2=DiGraph()
        # algo2 = GraphAlgo(g2)
        # algo2.load_from_json("C:/Users/nechd\Desktop\OOP_2021-main\Assignments\Ex3\src\data\A5_edited")
        # print("nodes\n:", algo2.graph.nodeD)
        # print("edges\n:", algo2.graph.edgeD)

if __name__ == '__main__':
    unittest.main()
