import random
import math
from turtle import *

class Program(object):
    """ Chromosomal representation for the Genetic Algorithm
    """

    def __init__(self,chromosome):
        self.chromosome = chromosome #Linked List to define the genome
        self.fitness = None
        self.size = 0

    def getFitness(self,per1,area1,ratio1,per2,area2,ratio2):
        print("Not implemented yet")


    def getSize(self):
        print("Not yet implemented")

    def expressions(self):
        expr=[]
        current = self.chromosome.head
        while current:
            expr.append(current.get_data())
            current = current.get_next()
        #print(expr)
        return expr

    def toString(self):
        progList = []
        current = self.chromosome.head
        while current:
            progList.append(current.get_data())
            current = current.get_next()
        progString = "\n".join(progList)
        return progString

    def execute(self):
        setup()
        exec(self.toString())
        exitonclick()

    def coords(self):
        coordList = []
        p = Parser(self.expressions())
        track = Tracker()
        comList, argList = p.parseList()
        #print(comList)
        #print(argList)
        #print(track.pos())
        coordList.append(track.pos())
        for x in range(0,len(argList)):
            if comList[x] == 'forward':
                track.forward(argList[x])
                #print(track.pos())
                coordList.append(track.pos())
            elif comList[x] == 'right':
                track.right(argList[x])
                #print(track.pos())
        #track.home()
        #print(track.pos())
        print(coordList)

class Node(object):
    """Standard Node object of a Linked List"""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    """Linked List Data Structure"""
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        newNode = Node(data)
        newNode.set_next(self.head)
        self.head = newNode

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            return ValueError("That data is not in the list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("That data is not in the list can not delete it")
        else:
            previous.set_next(current.get_next())

    def printList(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()

    def toString(self):
        progList = []
        current = self.head
        while current:
            progList.append(current.get_data())
            current = current.get_next()
        progString = "\n".join(progList)
        return progString

class Vertex(tuple):
    def __new__(cls,x,y):
        return tuple.__new__(cls,(x,y))
    def __add__(self, other):
        return Vertex(self[0]+other[0], self[1]+other[1])
    def __mul__(self, other):
        if isinstance(other, Vertex):
            return self[0]*other[0]+self[1]*other[1]
        return Vertex(self[0]*other, self[1]*other)
    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vertex(self[0]*other, self[1]*other)
    def __sub__(self, other):
        return Vertex(self[0]-other[0], self[1]-other[1])
    def __neg__(self):
        return Vertex(-self[0], -self[1])
    def __abs__(self):
        return (self[0]**2 + self[1]**2)**0.5
    def rotate(self, angle):
        """rotate self counterclockwise by angle
        """
        perp = Vertex(-self[1], self[0])
        angle = angle * math.pi / 180.0
        c, s = math.cos(angle), math.sin(angle)
        return Vertex(self[0]*c+perp[0]*s, self[1]*c+perp[1]*s)
    def __getnewargs__(self):
        return (self[0], self[1])
    def __repr__(self):
        return "(%.2f,%.2f)" % self

class Polygon:
    def __init__(self,vertexList,sideList,yAngle):
        this.vertexList = vertexList
        this.sides = len(vertexList)
        this.sideList = sideList
        this.yAngle = yAngle

class Triangle:
    def __init__(self, name,xLen,yLen,yAngle):
        self.name = name
        self.xLen = xLen
        self.yLen = yLen
        self.zLen = 0
        self.xAngle = 0
        self.yAngle = math.radians(yAngle)
        self.zAngle = 0
        self.perimeter = 0

    def findZLen(self):
        self.zLen = math.sqrt((self.xLen**2) + (self.yLen**2) - (2 *
                                                                 self.xLen * self.yLen * math.cos(self.yAngle)))  # Law of cosines
        return self.zLen

    def findPerimeter(self):
        self.findZLen()
        self.perimeter = self.xLen + self.yLen + self.zLen
        #print("Perimeter is: "+str(self.perimeter)+" pixels")
        return self.perimeter

    def findZAngle(self):
        first = self.zLen**2 + self.yLen**2 - self.xLen**2
        second = 2*self.zLen*self.yLen
        self.zAngle = math.degrees(math.acos(first/second))
        #self.zAngle = math.acos((self.zLen**2 + self.yLen**2 - self.xLen**2) / 2*(self.zLen*self.yLen))
        return self.zAngle
        #self.zAngle = math.asin(
        #    (math.sin(math.degrees(self.yAngle)) * self.xLen) / self.zLen)  # Law of Sines
        #return math.degrees(self.zAngle)

    def findXAngle(self):
        self.xAngle = 180-math.degrees(self.yAngle)-self.zAngle

    def findArea(self):
        # Heron's Formula
        s = (self.xLen+self.yLen+self.zLen) / 2 #Semi perimeter
        area = (s*(s-self.xLen)*(s-self.yLen)*(s-self.zLen)) **.5
        return area

    def xVector(self):
        newXLen = self.xLen / self.perimeter
        newYLen = self.yLen / self.perimeter
        newZlen = self.zLen / self.perimeter
        xVec = [newXLen,newYLen,newZlen]
        return xVec

    def checkAngles(self):
        print("Sum of the angles " + str(self.zAngle+math.degrees(self.yAngle)+self.xAngle))

    def yVec(self):
        self.findZAngle()
        self.findXAngle()
        x = math.radians(self.xAngle)
        z = math.radians(self.zAngle)
        y = self.yAngle
        newX = x
        newY = x+y
        newZ = x+y+z
        total = newX+newY+newZ
        #print(total / (2*math.pi))
        yVec = [newX,newY,newZ]
        return yVec

    def turningFunction(self):
        xVec = self.xVector()
        yVec = self.yVec()
        func = []
        for x in range(0,len(xVec)):
            l = [xVec[x],yVec[x]]
            func.append(l)

        print(func)




class Generator:
    """Used to generate Programs from a set of rules"""
    def __init__(self, minCommands, maxCommands):
        self.commands = []
        self.arguments = []
        ########## CONSTANTS FOR GENERATION ####################
        self.MAX_DIRECTION_COMMAND_VALUE = 150
        self.MIN_DIRECTION_COMMAND_VALUE = 50
        self.MAX_ANGLE_COMMAND_VALUE = 178
        self.MIN_ANGLE_COMMAND_VALUE = 50
        ########## INITIALIZATION ARGUMENTS ####################
        self.maxComCount = maxCommands
        self.minComCount = minCommands

    def generate(self):
        # dictionary for arguments
        argDict = {'1': 'forward', '2': 'right', '3': 'home'}
        comAmount = random.randint(self.minComCount, self.maxComCount)
        for x in range(0, comAmount):
            #arg = random.randrange(1,3)
            com = random.choice(list(argDict.values()))
            self.commands.append(com)
            if com == 'forward':
                self.arguments.append(random.randrange(
                    self.MIN_DIRECTION_COMMAND_VALUE, self.MAX_DIRECTION_COMMAND_VALUE))
            elif com == 'right':
                self.arguments.append(
                    random.randrange(self.MIN_ANGLE_COMMAND_VALUE, self.MAX_ANGLE_COMMAND_VALUE))
            else:
                self.arguments.append('0')
        #print (self.commands)
        #print (self.arguments)
        return self.commands, self.arguments

    def genTriangle(self):
        #argDict = {'1': 'forward', '2': 'right', '3': 'home'}
        chromosome = LinkedList()
        chromosome.insert("home ()")
        i = random.randrange(self.MIN_DIRECTION_COMMAND_VALUE, self.MAX_DIRECTION_COMMAND_VALUE)
        chromosome.insert("forward (" + str(i)+")")
        i = random.randrange(self.MIN_ANGLE_COMMAND_VALUE, self.MAX_ANGLE_COMMAND_VALUE)
        chromosome.insert("right ("+str(i)+")")
        i = random.randrange(self.MIN_DIRECTION_COMMAND_VALUE, self.MAX_DIRECTION_COMMAND_VALUE)
        chromosome.insert("forward (" + str(i)+")")
        return chromosome

class Parser:
    """Used to Parse the generated Programs"""
    def __init__(self, expr):
        self.expr=expr

    def parseTriangle(self):
        forward = int(''.join(x for x in self.expr[0] if x.isdigit()))
        right = int(''.join(x for x in self.expr[1] if x.isdigit()))
        forward2 = int(''.join(x for x in self.expr[2] if x.isdigit()))
        #return forward,forward2,right
        t = Triangle('Test',forward,forward2,right)
        per = t.findPerimeter()
        area = t.findArea()
        rat = per/area
        t.xVector()
        t.yVec()
        t.turningFunction()
        return per,area,rat

    def parseList(self):
        progList=[]
        comList = []
        argList = []
        for x in range(0,len(self.expr)):
            progList.append(self.expr[x].split())
        for x in range(0,len(self.expr)):
            comList.append(progList[x][0])
        for x in range(0,len(self.expr)-1):
            arg = int(''.join(x for x in progList[x][1] if x.isdigit()))
            argList.append(arg)
        return comList, argList


class Tracker:
    def __init__(self):
        self._angleOffset = 0
        self._angleOrient = 1
        self._degrees()
        Tracker._reset(self)

    def _reset(self):
        self._position = Vertex(0,0)
        self._orient = Vertex(1,0)

    def _setDegreesPerAU(self, fullcircle):
        """Helper function for degrees() and radians()"""
        self._fullcircle = fullcircle
        self._degreesPerAU = 360/fullcircle
        #if self._mode == "standard":
        #    self._angleOffset = 0
        #else:
        #    self._angleOffset = fullcircle/4.

    def _degrees(self, fullcircle=360.0):
        self._setDegreesPerAU(fullcircle)

    def _go(self,distance):
        ende = self._position + self._orient * distance
        self._goto(ende)

    def _rotate(self,angle):
        angle *= self._degreesPerAU
        self._orient = self._orient.rotate(angle)

    def _goto(self,end):
        self._position = end

    def forward(self,distance):
        self._go(distance)

    def right(self,angle):
        self._rotate(-angle)

    def pos(self):
        return self._position

    def home(self):
        self._goto(0,0)

def normalize(arg):
    return [float(i)/max(arg) for i in arg]

def fitness(per1,area1,rat1,per2,area2,rat2):
    return abs(per1-per2)+abs(area1-area2)+abs(rat1-rat2)

def ratFit(rat1,rat2):
    return abs(rat1-rat2)


def main():
    perList=[]
    areaList=[]
    ratList=[]
    testSize=100
    for x in range(0,testSize):
        print("Program " +str(x+1)+"\n")
        gen = Generator(4,4)
        prog = Program(gen.genTriangle())
        #prog.execute()
        print (prog.toString()+"\n")
        parse = Parser(prog.expressions())
        prog.coords()
        #prog.execute()
        per,area,rat = parse.parseTriangle()
        perList.append(per)
        areaList.append(area)
        ratList.append(rat)
        #print("Perimeter is: " + str(per) + " pixels")
        #print("Area is: "+ str(area)+ " pixels")
        #print("Ratio of perimeter to area is: "+ str(rat))
        print("\n******************************************\n")

if __name__ == "__main__":
    main()
