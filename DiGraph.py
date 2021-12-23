import random
from random import uniform
from Edges import Edges
from Node import Node
from src.GraphInterface import GraphInterface


class DiGraph (GraphInterface):



    def __init__(self):
        self.nodeD = dict()
        self.edgeD = dict()
        self.mc = 0

    def __repr__(self):
        m1=str(self.mc)
        m = str("mc: " )
        n = str(self.nodeD)
        e = str(self.edgeD)
        return "mc: "+m1+"\nnodeD"+n+"\nedegD: "+e

    def v_size(self) -> int:
        return len(self.nodeD)


    def e_size(self) -> int:
        return len(self.edgeD)

    def get_all_v(self) -> dict:
        return self.nodeD



    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodeD.get(id1).in1



    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodeD.get(id1).out1



    def get_mc(self) -> int:
        return self.mc


    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        s = (id1, id2)
        #print(s)
        if s in self.edgeD:
            pass
        else:
            if id1 in self.nodeD and id2 in self.nodeD:
                e1 = Edges(id1, id2, weight)
                self.edgeD[s] = e1

                # add to the src and dest nodes the edge
                #self.nodeD.get(id1).outfrom[s] = e1
                self.nodeD.get(id1).out1[id2] = weight
                #self.nodeD.get(id2).into[s] = e1
                self.nodeD.get(id2).in1[id1]=weight

                if s in self.edgeD:
                    self.mc = self.mc + 1
                    return True
                else:
                    return False
            else:
                pass



    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodeD:
            pass
        else:
            if pos == None:
                x = random.random()
                y = random.random()
                z = random.random()
                n1 = Node(x, y, z, node_id)
                self.nodeD[node_id] = n1
            else:
                x = pos[0]
                y = pos[1]
                z = pos[2]
                n1 = Node(x, y, z, node_id)
                self.nodeD[node_id] = n1
            if node_id in self.nodeD:
                self.mc = self.mc+1
                return True
            else:
                return False


    def remove_node(self, node_id: int) -> bool:

        if node_id in self.nodeD:
            remove = []
            #for r in self.nodeD.get(node_id).outfrom:
            for r in self.nodeD.get(node_id).out1:
                x=(node_id, r)
                remove.append(x)
            #for r in self.nodeD.get(node_id).into:
            for r in self.nodeD.get(node_id).in1:
                x = (r, node_id)
                remove.append(x)
            for r in remove:
                del self.edgeD[r]
            del self.nodeD[node_id]
            if node_id in self.nodeD:
                return False
            else:
                self.mc = self.mc+1
                return True
        else:
            pass



    def remove_edge(self, node_id1: int, node_id2: int) -> bool:

        s = (node_id1, node_id2)
        if s in self.edgeD:
            del self.edgeD[s]
            #del self.nodeD.get(node_id1).outfrom[s]
            del self.nodeD.get(node_id1).out1[node_id2]
            #del self.nodeD.get(node_id2).into[s]
            del self.nodeD.get(node_id2).in1[node_id1]
            if s in self.edgeD:
                return False
            else:
                self.mc = self.mc + 1
                return True
        else:
            pass

