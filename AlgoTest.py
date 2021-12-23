import unittest

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_something(self):


        # creatring graph
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

        # creating algo
        myalgo =GraphAlgo(g)

        # testing load - not full
        g0 = DiGraph()
        algo0 = GraphAlgo(g0)
        algo0.load_from_json("C:/Users/nechd\Desktop\OOP_2021-main\Assignments\Ex3\data\A0.json")
        #print("nodes\n:", algo2.graph.nodeD)
        #print("edges\n:", algo2.graph.edgeD)
        g1 = DiGraph()
        algo1 = GraphAlgo(g1)
        algo1.load_from_json("C:/Users/nechd\Desktop\OOP_2021-main\Assignments\Ex3\data\A1.json")
        g2 = DiGraph()
        algo2 = GraphAlgo(g2)
        algo2.load_from_json("C:/Users/nechd\Desktop\OOP_2021-main\Assignments\Ex3\data\A2.json")
        g3 = DiGraph()
        algo3 = GraphAlgo(g3)
        algo3.load_from_json("C:/Users/nechd\Desktop\OOP_2021-main\Assignments\Ex3\data\A3.json")
        g4 = DiGraph()
        algo4 = GraphAlgo(g4)
        algo4.load_from_json("C:/Users/nechd\Desktop\OOP_2021-main\Assignments\Ex3\data\A4.json")
        g5 = DiGraph()
        algo5 = GraphAlgo(g5)
        algo5.load_from_json("C:/Users/nechd\Desktop\OOP_2021-main\Assignments\Ex3\data\A5.json")


        # test for tsp
        l=[]
        for n in g.nodeD:
            l.append(g.nodeD[n].getId())
        #print(l)
        
        x =myalgo.TSP(l)
        #print("tsp:", x )
        t1 = x[1] < 10
        self.assertTrue(t1)


        myalgo.save_to_json("myjson4node")


        # testing dijsktra
        # x =myalgo.dijasktra(0)
        # print(x[0])
        # print(x[1])

        #testing shortest path
        a1 = myalgo.shortest_path(0, 1)
        b1 = (1.35, [0, 1])
        self.assertEqual(a1, b1)
        a2 = myalgo.shortest_path(0, 2)
        b2 = (2.5854, [0, 1, 2])
        self.assertEqual(a2, b2)
        a3 = myalgo.shortest_path(0, 3)
        b3 = (1.89, [0, 1, 3])
        self.assertAlmostEqual(a3[0], b3[0])
        self.assertEqual(a3[1], b3[1])
        a4 = myalgo.shortest_path(1, 3)
        b4 = (0.54, [1, 3])
        self.assertEquals(a4[0], b4[0])
        self.assertEquals(a4[1], b4[1])


        # testing is conneted
        y=myalgo.isConnected()
        #print(y)
        self.assertTrue(y)
        g.remove_edge(3, 0)
        y = myalgo.isConnected()
        # print(y)
        self.assertFalse(y)


        # testing center
        g.add_edge(3, 0, 2.5)
        myx = myalgo.centerPoint()
        #print("center:" ,myx)
        self.assertEqual(0,myx[0])
        x0 = algo0.centerPoint()
        #print("center:", x0)
        self.assertEqual(7 , x0[0])
        x1 = algo1.centerPoint()
        #print("center:", x1)
        self.assertEqual(8, x1[0])
        x2 = algo2.centerPoint()
        #print("center:", x2)
        self.assertEqual(0, x2[0])
        x3 = algo3.centerPoint()
        #print("center:", x3)
        self.assertEqual(2, x3[0])
        x4 = algo4.centerPoint()
        #print("center:", x4)
        self.assertEqual(6, x4[0])
        x5 = algo5.centerPoint()
        #print("center:", x5)
        self.assertEqual(40, x5[0])

        myalgo.plot_graph()
        algo1.plot_graph()



if __name__ == '__main__':
    unittest.main()
