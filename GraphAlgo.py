import matplotlib
import json
import string
from typing import List , cast
import random
from queue import PriorityQueue

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from DiGraph import DiGraph
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface





class GraphAlgo (GraphAlgoInterface):

    def __init__(self, g):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            f = open(file_name)
            data = json.load(f)
            #self.Graph = self.Graph.init_()
            for i in data["Nodes"]:
                n = (i["pos"])
                n: cast(string, n)  # cast it to string
                m = n.split(',')  # spliting to nodes
                print(m)
                pos = (float(m[0]), float(m[1]), float(m[2]))
                print(pos)
                self.graph.add_node(i["id"], pos)
            for i in data["Edges"]:
                self.graph.add_edge(i["src"], i["dest"], i["w"])
            return True
        except Exception as e:
            print(e)
            return False
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        #raise NotImplementedError

    def save_to_json(self, file_name: str) -> bool:
        dict = {"Nodes": [], "Edges": []}
        n =self.graph.nodeD
        # for node in self.graph.nodeD.values():
        #     id = node.getId()
        #     pos = f'{node.getX()},{node.getY()},{node.getY()}'
        #     dict['Nodes'].append({'id': id, 'pos': pos})
        for no in n:
            id =n[no].getId()
            x = str(n[no].getX())
            c1 =str(",")
            y = str(n[no].getY())
            z = str(n[no].getZ())
            pos = x + c1 + y + c1 + z
            #pos = f'{ n[no].getX(),n[no].getY(),n[no].getZ()}'
            #pos = [n[no].getX(),n[no].getY(),n[no].getZ()]
            dict['Nodes'].append({'id': id, 'pos': pos})
            #     pos = f'{node.getX()},{node.getY()},{node.getY()}'
        # for edge in self.graph.edgeD:
        #     dict['Edges':].append({'src': edge.getsrc(), 'dest': edge.getdest(), 'w': edge.getweight()})
        e = self.graph.edgeD
        for ed in e:
            dict['Edges'].append({'src': e[ed].getsrc() ,'dest': e[ed].getdest(), 'w': e[ed].getweight()})

        try:
            with open(file_name, 'w') as f:
                json.dump(dict, indent=2, fp=f)
            return True
        except Exception as e:
            print(e)
            return False


        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        #raise NotImplementedError

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        x = self.dijasktra(id1)
        l=(id1, id2)
        ans=(x[0].get(l),x[1].get(l))
        return ans;
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        #raise NotImplementedError

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        n_list = node_lst
        dubD =dict()
        listD=dict()
        for n in node_lst:
            pair = self.dijasktra(n)
            d = pair[0]
            dubD[n] = d
            # for p0 in d:
            #     dubD[p0] = d.get[p0]
            l = pair[1]
            listD[n] = l
            # for p1 in l:
            #     listD[p1] = l.get[p1]

        #print(dubD)
        #print(listD)

        small = float("inf")
        for outer in dubD:
            m=dubD[outer]
            for inner in m:
                if inner[0] != inner[1]:
                    if m[inner] < small:
                        small = m[inner]
                        in1 = inner
                        out1= outer
        #print(small, out1, in1)

        flooat= small
        liist=[]
        liist.append(in1[0])
        liist.append(in1[1])
        n_list.remove(in1[0])
        n_list.remove(in1[1])
        while len(n_list) > 0:
            new = n_list[0]
            begin = liist[0]
            end = liist[len(liist)-1]
            dist1=dubD[end][(end, new)]
            dist2=dubD[new][(new,begin)]
            if dist1 < dist2:
                flooat=flooat+dist1
                l=listD[end][(end, new)]
                count = 0
                for x in l:
                    if x not in liist:
                        liist.insert(count, x)
                        count=count+1
                    if x in n_list:
                        n_list.remove(x)
            else:
                flooat=flooat+dist2
                l = listD[new][(new,begin)]
                for x in l:
                    if x not in liist:
                        liist.append(x)
                    if x in n_list:
                        n_list.remove(x)

        ans= (liist, flooat)
        return ans
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    def centerPoint(self) -> (int, float):
        x = self.isConnected()
        if x == False:
            ans = (None, float("inf"))
            return ans
        short_long = dict()

        for key in self.graph.nodeD:
            big = 0.0
            a = self.graph.nodeD[key].getId()
            pair = self.dijasktra(a)
            for x in pair[0]:
                d = pair[0].get(x)
                #print(d)
                if d > big:
                    big = d

            short_long[a] = big
        #print(short_long)
        small = (None, float("inf"))
        for key in short_long:
            if short_long[key] < small[1]:
                small= (key,short_long[key])

        return small



        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        n = self.graph.nodeD
        e = self.graph.edgeD

        listx =[]
        listy = []
        listid =[]
        for cor in n:
            listx.append(n[cor].getX())
            listy.append(n[cor].getY())
            listid.append(n[cor].getId())
       # print(listx ,listy , listid)
        listx1 = []
        listx2 = []
        listy1 = []
        listy2 = []
        for cor in e:
            src = e[cor].getsrc()
            dest = e[cor].getdest()
            listx1.append(n[src].getX())
            listy1.append(n[src].getY())
            listx2.append(n[dest].getX())
            listy2.append(n[dest].getY())

       # print(listx1,listy1,listx2, listy2)
        lennode=len(listx)
        lenedge=len(listx1)
        figure(figsize=(8,5))
        for i in range (0, lennode):
            plt.plot(listx[i], listy[i], markersize=10, marker="o", color="blue")
            plt.text(listx[i], listy[i], listid[i], color='red', fontsize=16, fontstyle="normal")

        for i in range(0, lenedge):
            plt.annotate("", xy=(listx1[i], listy1[i]), xytext=(listx2[i], listy2[i]), arrowprops=dict(arrowstyle="<-"))





        # plt.plot(x,y,markersize= 10, marker = "o" , color = "blue" )
        # for dest in self.graph.edgeD[key.id]:
        #     his_x,his_y = self.graph.edgeD[dest].pos
        #     plt.annotate("",xy = (x,y),xytext = (his_x,his_y),arrowprops=dict(arrowstyle="<-") )
        plt.show()















        #raise NotImplementedError


    def dijasktra(self, src: int) -> tuple:
        q = PriorityQueue(maxsize=10000000000)
        mapd = dict()
        mapl = dict()
        l = []
        n = self.graph.get_all_v()
        for key in n:
            n1 = n[key]
            l2 = []
            l2.append(src)
            l2.append(n1.getId())
            l1 = (src, n1.getId())
            mapd[l1] = float("inf")
            mapl[l1] = l2
            #l.append(n1)
            l.append(key)


        l1 = (src, src)
        mapd[l1] = 0.0

        q.put((0.0,src))
        empt = q.empty()
        while(empt == False):
            peek1 = q.queue[0]
            peek = peek1[1]
            #for k in self.graph.nodeD.get(peek).outfrom:
            for k in self.graph.nodeD.get(peek).out1:
                #e = self.graph.nodeD.get(peek).outfrom[k]
                e=self.graph.nodeD.get(peek).out1[k]
                #dest =n[e.getdest()]
                #if dest in l:
                if k in l:
                    #l2 = (src, e.getdest())
                    l2 = (src, k)
                    if mapd.get(l2) == float("inf"):

                        #l3 = (src, e.getsrc())
                        l3 = (src, peek)
                        #d = mapd[l3] + e.getweight()
                        d = mapd[l3] + e
                        mapd[l2] = d
                        #q.put((d, e.getdest()))
                        q.put((d, k))
                        l5 = []
                        l6 = mapl[l3]
                        for i in range(len(l6)):
                            if l6[i] not in l5:
                                l5.append(l6[i])
                        #l5.append(e.getdest())
                        l5.append(k)
                        mapl[l2] = l5
                    else:
                        #l3 = (src, e.getsrc())
                        l3 = (src, peek)
                        #if mapd[l2] >mapd[l3] + e.getweight():
                        if mapd[l2] > mapd[l3] + e:
                            #d = mapd[l3] + e.getweight()
                            d = mapd[l3] + e
                            mapd[l2] = d
                            #q.put((d, e.getdest()))
                            q.put((d,k))
                            l5 = []
                            l6 = mapl[l3]
                            for i in range(len(l6)):
                                if l6[i] not in l5:
                                    l5.append(l6[i])
                            #l5.append(e.getdest())
                            l5.append(k)
                            mapl[l2] = l5

            y = q.get(0)
            empt = q.empty()
            n1 = self.graph.nodeD.get(peek)
            # if n1 in l:
            #     l.remove(n1)
            if peek in l:
                l.remove(peek)


        return (mapd, mapl)


    def isConnected(self) -> bool:
        if self.graph.v_size()==0:
            return False
        if self.graph.e_size() < self.graph.v_size():
            return False
        for key in self.graph.nodeD:
            self.graph.nodeD[key].settag(0)

        l = []
        n1 = list(self.graph.nodeD.values())[0]  # get first value
        l.append(n1)
        while len(l) > 0:
            n2 = l[0]
            l.remove(n2)
            n2.settag(1)
            # for k in self.graph.nodeD.get(n2.getId()).outfrom:
            for k in self.graph.nodeD.get(n2.getId()).out1:
                # e = self.graph.nodeD.get(n2.getId()).outfrom[k]  # edge
                e = self.graph.nodeD.get(n2.getId()).out1[k]  #other side of edge int
                # n3 = self.graph.nodeD.get(e.getdest())
                # if n3.gettag() != 1:
                #     if n3 not in l:
                #         l.append(n3)
                n3 =self.graph.nodeD.get(k)
                if n3.gettag() != 1:
                    if n3 not in l:
                        l.append(n3)


        for key in self.graph.nodeD:
            # print("key=" , key, self.graph.nodeD[key].gettag())
            if self.graph.nodeD[key].gettag() == 0:
                return False

        g = self.get_graph()
        graphflip = self.flipGraph(g)

        for key in graphflip.nodeD:
            graphflip.nodeD[key].settag(0)
        l = []
        n1 = list(graphflip.nodeD.values())[0]  # get first value
        l.append(n1)
        while len(l) > 0:
            n2 = l[0]
            l.remove(n2)
            n2.settag(1)
            #for k in graphflip.nodeD.get(n2.getId()).outfrom:
            for k in graphflip.nodeD.get(n2.getId()).out1:
                #e = graphflip.nodeD.get(n2.getId()).outfrom[k]  # edge
                e = graphflip.nodeD.get(n2.getId()).out1[k]  #other side of edge int
                # n3 = graphflip.nodeD.get(e.getdest())
                # if n3.gettag() != 1:
                #     if n3 not in l:
                #         l.append(n3)
                n3 = graphflip.nodeD.get(k)
                if n3.gettag() != 1:
                    if n3 not in l:
                        l.append(n3)
        for key in graphflip.nodeD:
            # print("key=" , key, self.graph.nodeD[key].gettag())
            if graphflip.nodeD[key].gettag() == 0:
                return False

        return True


    def flipGraph(self,graph: DiGraph)-> DiGraph:
        gr = DiGraph()
        for k in graph.nodeD:
            id=graph.nodeD[k].getId()
            cor=(graph.nodeD[k].getX(), graph.nodeD[k].getY(), graph.nodeD[k].getZ())
            gr.add_node(id, cor)
        for k in graph.edgeD:
            e = graph.edgeD[k]
            s = e.getsrc()
            d = e.getdest()
            w = e.getweight()
            gr.add_edge(d, s, w)
       # print("flipped nodes:\n", gr.nodeD)
       # print("flipped edges:\n", gr.edgeD)
        return gr