class Node:

    def __init__(self, x, y, z, id):
        self.x = x
        self.y = y
        self.z = z
        self.id = id
        self.in1 = dict()
        self.out1 = dict()
        self.tag = 0




        # this function returns the id
    def getId(self):
        return self.id

        # this function returns the x
    def getX(self):
        return self.x

        # this function returns the y
    def getY(self):
        return self.y

        # this function returns the y
    def getZ(self):
        return self.z

        # this function set new value of x
    def setX(self,x):
       self.x = x

        # this function set new value of y
    def setY(self,y):
        self.y = y

        # this function set new value of x
    def setZ(self,z):
        self.z = z

         #this function return the dictionary of nodes in
    def getIn1(self) :
        return self.in1

        # this function return the dictionary of nodes out
    def getOut1(self) :
        return  self.out1


    def gettag(self):
        return self.tag


    def settag(self,t):
        self.tag=t;



