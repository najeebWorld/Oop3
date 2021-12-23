import unittest
import random
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_something(self):

        myalgo = GraphAlgo()
        myalgo.load_from_json("my graph1.json")


        # load and save
        # myalgo.load_from_json("my graph1.json")
        # myalgo.save_to_json("myGraph1copy.json")
        # my_algo_new =GraphAlgo()
        # my_algo_new.load_from_json("myGraph1copy.json")
        # ans = True
        # for n in myalgo.graph.nodeD:
        #     if myalgo.graph.nodeD[n].getId() != my_algo_new.graph.nodeD[n].getId():
        #         ans = False
        #     if myalgo.graph.nodeD[n].getX() != my_algo_new.graph.nodeD[n].getX():
        #         ans = False
        #     if myalgo.graph.nodeD[n].getY() != my_algo_new.graph.nodeD[n].getY():
        #         ans = False
        #     if myalgo.graph.nodeD[n].getZ() != my_algo_new.graph.nodeD[n].getZ():
        #         ans = False
        # self.assertTrue(ans)
        # for e in myalgo.graph.edgeD:
        #     if myalgo.graph.edgeD[e].getsrc() != my_algo_new.graph.edgeD[e].getsrc():
        #         ans = False
        #     if myalgo.graph.edgeD[e].getdest() != my_algo_new.graph.edgeD[e].getdest():
        #         ans = False
        #     if myalgo.graph.edgeD[e].getweight() != my_algo_new.graph.edgeD[e].getweight():
        #         ans = False
        # self.assertTrue(ans)


        # shortest path
        # x= myalgo.shortest_path(0, 8)
        # self.assertAlmostEqual(x[0],5.0)
        # self.assertEqual(x[1], [0, 1, 2, 4, 5, 8])


        # center
        # ans=myalgo.centerPoint()
        # print(ans)
        # self.assertEqual(ans[0],4)
        # self.assertAlmostEqual(ans[1],2)


        # tsp
        # lenn =len(myalgo.graph.nodeD)
        # liist=random.sample(range(0, lenn), 5)
        # print(liist)
        # ans =myalgo.TSP(liist)
        # print("ans:" ,ans)
        # a1= len(ans[0]) >= len(liist)
        # self.assertTrue(a1)






        # plot
        myalgo.plot_graph()






if __name__ == '__main__':
    unittest.main()
