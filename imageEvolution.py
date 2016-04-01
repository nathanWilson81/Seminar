import random
import math
import time
import operator
import itertools
from turtle import *
#import numpy as np
from PIL import Image, ImageDraw

class Program(object):
    """ Chromosomal representation for the Genetic Algorithm
    """

    def __init__(self,chromosome):
        self.chromosome = chromosome #Linked List to define the genome
        self.fitness = None
        self.size = 0
        self.parse = Parser(self.expressions())
        self.poly = Polygon(self.coords())
        self.turnFunc = self.poly.turnFunc


    def getFitness(self):
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

    def execute(self,i):
        setup()
        ht()
        ts = getscreen()
        exec(self.toString())
        can = ts.getcanvas()
        can.postscript(file="test.eps")
        img = Image.open("test.eps")
        img.save("test"+str(i)+".png","png")
        reset()

    def savePIL(self,i):
        chain = list(itertools.chain(*self.poly.vertexList))
        print(chain)
        img = Image.new('RGB', (300,300),(255,255,255,0))
        draw = ImageDraw.Draw(img)
        draw.polygon(chain,outline=(255,0,0))
        img.show()


    def coords(self):
        coordList = []
        p = Parser(self.expressions())
        track = Tracker()
        comList, argList = p.parseList()
        coordList.append(track.pos())
        for x in range(0,len(argList)):
            if comList[x] == 'forward':
                track.forward(argList[x])
                coordList.append(track.pos())
            elif comList[x] == 'right':
                track.right(argList[x])
        return coordList

    def counterClockwiseCoords(self):
        coords = self.coords()
        v1 = coords[0]
        v2 = coords[1]
        v3 = coords[2]
        newCoords = [v1,v3,v2]
        return newCoords

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
    def __init__(self,vertexList):
        self.vertexList = vertexList
        self.size = len(self.vertexList)
        self.angles = []
        self.turnFunc = []
        self.perimeter = 0
        self.area = 0
        self.convex = None
        self.areaUnderFunc = 0
        self.turningFunction()
        self.funcArea()


    def dotAngles(self,x1,y1,x2,y2):
        #print('Values',x1,y1,x2,y2)
        top = (x1 * x2 + y1 * y2)
        bot = math.sqrt((x1**2 + y1**2) * (x2**2 + y2 ** 2))
        try:
            return (math.acos(top/bot))
        except ValueError:
            print("Tried to top/bot")
            return math.pi
        except ZeroDivisionError:
            return math.pi
            #self.dotAngles(x1,y1,x2,y2)
        #self.angles.append(math.acos(top/bot))

    def crossProductSign(self,x1,y1,x2,y2,z1,z2):
        c = [y1*z2 - z1*y2,
             z1*x2 - x1*z2,
             x1*y2 - y1*x2]
        return c[2]
        #return x1*y2 < x2*y1

    def degrees(self,angList):
        ret = []
        for i in range(len(angList)):
            ret.append(math.degrees(angList[i]))
        return ret

    def calcAngles(self):
        #print(self.vertexList)
        angList = []
        for i in range(self.size):
            p1 = self.vertexList[i]
            ref = self.vertexList[i-1]
            p2 = self.vertexList[i-2]
            x1, y1 = p1[0] - ref[0], p1[1] - ref[1]
            x2, y2 = p2[0] - ref[0], p2[1] - ref[1]
            zComp = self.crossProductSign(x1,y1,x2,y2,0,0)
            if zComp < 1:
                #print("Positive")
                ang = self.dotAngles(x1,y1,x2,y2)
                angList.append(ang)
            else:
                #print ("Negative")
                ang = self.dotAngles(x1,y1,x2,y2)
                angList.append(-ang)
        #print("Interior angles",angList)
        #print(self.degrees(self.externalAngles(self.reorderAngles(angList))))
        return self.externalAngles(self.reorderAngles(angList))
        #self.reorderAngles(angList)

    def coordDistance(self):
        #print("\nDistance time\n")
        distList = []
        for i in range(self.size):
            if i == self.size-1:
                p1 = self.vertexList[-1]
                p2 = self.vertexList[0]
                distList.append(math.hypot(p2[0]-p1[0],p2[1]-p1[1]))
            else:
                p1 = self.vertexList[i]
                p2= self.vertexList[i+1]
                distList.append(math.hypot(p2[0]-p1[0],p2[1]-p1[1]))
        return distList

    def reorderAngles(self,lis):
        #lis = [61.28761450547862, 149.71238549452138, 96.0, 105.00000000000001, 128.0]
        last = lis.pop(0)
        lis.append(last)
        #print(lis)
        return lis

    def normDist(self,distList):
        perimeter = 0
        retList = []
        for i in range(len(distList)):
            perimeter = perimeter + distList[i]
        for i in range(len(distList)):
            retList.append(distList[i]/perimeter)
        return retList

    def sumRadians(self,angList):
        if abs(sum(angList) - 2*math.pi) < .01 or self.size == 3:
            self.convex = True
            #print(self.convex)
            #print("The polygon is convex")

    def xVec(self,distVec):
        sum = 0
        ret = []
        for i in range(len(distVec)):
            sum = sum + distVec[i]
            ret.append(sum)
        return ret

    def yVec(self,angList):
        sum = 0
        ret = []
        for i in range(len(angList)):
            sum = sum + angList[i]
            ret.append(sum)
            if i == len(angList)-1 :
                pass
        return ret

    def externalAngles(self,angList):
        ext = []
        for i in range(len(angList)):
            if angList[i] > 0:
                ext.append(math.pi - angList[i])
            else:
                #print("concave angle found",angList[i])
                ans = math.pi+angList[i]
                #print("concave angle",-ans)
                #print("Answer was",ans)
                ext.append(-ans)
        #print("External angles are: ",ext)
        return ext

    def turningFunction(self):
        #self.sumRadians(self.calcAngles())
        angList = self.calcAngles()
        self.sumRadians(angList)
        yVec = self.yVec(angList)
        distList = self.xVec(self.normDist(self.coordDistance()))
        func = []
        for i in range(len(angList)):
            func.append([distList[i],yVec[i]])
        self.turnFunc = func
        #print(self.turnFunc)
        return func

    def funcArea(self):
        area = 0
        first = self.turnFunc[0][0] * self.turnFunc[0][1]
        area = area + first
        for i in range(1,len(self.turnFunc)):
            a = (self.turnFunc[i][0]-self.turnFunc[i-1][0]) * self.turnFunc[i][1]
            area = area+a
        #print(area)
            self.areaUnderFunc = area

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

        #print(func)
        return func

class Generator:
    """Used to generate Programs from a set of rules"""
    def __init__(self, minCommands, maxCommands):
        self.commands = []
        self.arguments = []
        ########## CONSTANTS FOR GENERATION ####################
        self.MAX_DIRECTION_COMMAND_VALUE = 150
        self.MIN_DIRECTION_COMMAND_VALUE = 50
        self.MAX_ANGLE_COMMAND_VALUE = 110
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

    def genGoalTriangle(self):
        chromosome = LinkedList()
        chromosome.insert("home ()")
        chromosome.insert("forward (" + str(50)+")")
        chromosome.insert("right ("+str(90)+")")
        chromosome.insert("forward (" + str(50)+")")
        return chromosome

    def genTest(self):
        chromosome = LinkedList()
        chromosome.insert("home ()")
        chromosome.insert("forward (" + str(84)+")")
        chromosome.insert("right ("+str(111)+")")
        chromosome.insert("forward (" + str(136)+")")
        return chromosome

    def genForwardRight(self):
        forwardArg = random.randrange(self.MIN_DIRECTION_COMMAND_VALUE, self.MAX_DIRECTION_COMMAND_VALUE)
        rightArg = random.randrange(self.MIN_ANGLE_COMMAND_VALUE, self.MAX_ANGLE_COMMAND_VALUE)
        forward = "forward (" + str(forwardArg)+")"
        right = "right (" + str(rightArg)+")"
        return forward,right

    def genPolygon(self,sides):
        chromosome = LinkedList()
        chromosome.insert("home ()")
        chromosome.insert("forward ("+str(random.randrange(self.MIN_DIRECTION_COMMAND_VALUE, self.MAX_DIRECTION_COMMAND_VALUE))+")")
        for i in range(0,sides-2):
            forward,right = self.genForwardRight()
            chromosome.insert(right)
            chromosome.insert(forward)
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
        t.findPerimeter()
        t.findArea()
        t.xVector()
        t.yVec()
        turn = t.turningFunction()
        return turn

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
        self._position = Vertex(0.0,0.0)
        self._orient = Vertex(1.0,0.0)

    def _setDegreesPerAU(self, fullcircle):
        """Helper function for degrees() and radians()"""
        self._fullcircle = fullcircle
        self._degreesPerAU = 360/fullcircle
        self._angleOffset = 0
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

class Generation:
    def __init__(self,progList):
        self.progList = progList
        self.sortProgs()

    def sortProgs(self):
        self.progList.sort(key=operator.attrgetter('fitness'))

def normalize(arg):
    return [float(i)/max(arg) for i in arg]

def fitness(per1,area1,rat1,per2,area2,rat2):
    return abs(per1-per2)+abs(area1-area2)+abs(rat1-rat2)

def ratFit(rat1,rat2):
    return abs(rat1-rat2)

def turningDistance(a1,a2):
    return abs(a1-a2)

def mutateArgs(program):
    mutProg = program.expressions()
    length = len(mutProg) - 1
    choice = random.randint(1,length)
    expr = mutProg.pop(choice-1)
    arg = int(''.join(x for x in expr if x.isdigit()))
    com = expr.split(' ')
    command = com[0]
    newArg = int(random.gauss(arg,25))
    newExpr = str(command) +str(" (")+str(newArg)+str(")")
    mutProg.insert(choice-1,newExpr)
    mutProg.reverse()
    LList = LinkedList()
    for x in range(0,len(mutProg)):
        LList.insert(mutProg[x])
    p = Program(LList)
    #print(p.expressions())
    return p
    #print("Program after mutation,",p.expressions())

def removeVertex(program):
    mutProg = program.expressions()
    num = (len(mutProg)-2)/2
    choice = random.randint(1,num)
    mutProg.pop(choice)
    mutProg.pop(choice)
    mutProg.reverse()
    LList = LinkedList()
    for x in range(0,len(mutProg)):
        LList.insert(mutProg[x])
    p = Program(LList)
    return p
    #print("Removed Vertex program",p.expressions())

def addVertex(program):
    mutProg = program.expressions()
    gen = Generator(4,4)
    forward,right = gen.genForwardRight()
    num = len(mutProg)-2
    choice = random.randint(2,num)
    if choice%2==0:
        choice -= 1
    mutProg.insert(choice+1,forward)
    mutProg.insert(choice+2,right)
    mutProg.reverse()
    LList = LinkedList()
    for x in range(0,len(mutProg)):
        LList.insert(mutProg[x])
    p = Program(LList)
    return p
    #print("Vertex added",p.expressions())
    #return mutProg

def mutate(progList):
    newProgs = []
    for x in range(0,len(progList)):
        choice = random.randint(1,3)
        if choice == 1:
            p = mutateArgs(progList[x])
            newProgs.append(p)
        elif choice == 2:
            p = removeVertex(progList[x])
            newProgs.append(p)
        else:
            p = addVertex(progList[x])
            newProgs.append(p)

    return newProgs

def geneticAlgorithm(goal, current):
    #print(type(current))
    #print(current.progList[0].fitness)
    fitList = []
    for x in range(0,len(current.progList)):
        fitList.append(current.progList[x])
    top = fitList[:10] #Grab top 10 for unchanged values
    del fitList[-25:] #Delete bottom 25 from the list
    middle = fitList[10:] #Get what's left to mutate
    newMiddle = mutate(middle)
    for x in range(0,len(newMiddle)):
        fit = turningDistance(goal.poly.areaUnderFunc,newMiddle[x].poly.areaUnderFunc)
        newMiddle[x].fitness = fit
    newBottom=[]
    for x in range(0,25):
        gen = Generator(4,4)
        prog = Program(gen.genPolygon(random.randint(3,8)))
        fit = turningDistance(goal.poly.areaUnderFunc, prog.poly.areaUnderFunc)
        prog.fitness = fit
        newBottom.append(prog)
    newGen = top + newMiddle + newBottom
    ret = Generation(newGen)
    return ret
    #bottom = current[-25:] #Grab last 25 to throw away

def initPop(goal):
    progList = []
    for x in range(0,100):
        gen = Generator(4,4)
        prog = Program(gen.genPolygon(random.randint(3,8)))
        fit = turningDistance(goal.poly.areaUnderFunc,prog.poly.areaUnderFunc)
        prog.fitness = fit
        progList.append(prog)
    g = Generation(progList)
    return g


def fitTest(goal,current):
    return turningDistance(goal.poly.areaUnderFunc,current.poly.areaUnderFunc)

def main():

    testSize=5
    num = 0
    generations=[]
    done = False
    count = 0
    gen = Generator(4,4)
    goal = Program(gen.genPolygon(4))
    print("Goal is")
    print(goal.toString())
    goal.execute(500)
    init = initPop(goal)
    #print(type(init))
    generations.append(init)
    while not done:
        init = geneticAlgorithm(goal,init)
        if init.progList[0].fitness < 0.000001:
            done = True
        generations.append(init)


    best = 2
    for x in range(0,len(generations)):
        if generations[x].progList[0].fitness < best:
            print("Generation",x)
            print(generations[x].progList[0].fitness)
            best = generations[x].progList[0].fitness
            generations[x].progList[0].execute(500+x)



  #for x in range(0,500):
    #    progList = []
    #    for y in range(0,100):
    #        gen = Generator(4,4)
    #        prog = Program(gen.genPolygon(random.randint(3,8)))
    ##        fit = turningDistance(goal.poly.areaUnderFunc,prog.poly.areaUnderFunc)
     #       prog.fitness = fit
     #       progList.append(prog)
     #   generations.append(Generation(progList))
    #geneticAlgorithm(generations[0])


    #t0 = time.clock()
    #while not done:
    #   gen = Generator(4,4)
    #    prog = Program(gen.genPolygon(random.randint(3,8)))
    #    fit = turningDistance(goal.poly.areaUnderFunc,prog.poly.areaUnderFunc)
    #    prog.fitness = fit
    #    if  fit < .0000001:
    #        print("\nFound it",count)
    #        print(prog.toString())
    #        prog.execute(1000)
    #        done = True
    #    elif fit < .001:
    #        progList.append(prog)
    #    count +=1
    #    if count % 1000000 == 0:
    #        print("Still churning along")
    #print((time.clock()-t0)/count)


    #print("Fitness hype")
    #ct = 1000
    #for x in range(0,len(progList)):
    #    progList[x].execute(ct)
    #    ct+=1

    #for x in range(1,179):
    #    gen = Generator(4,4)
    #    prog = Program(gen.genTest(x))
    #    t = prog.parse.parseTriangle()
    #    turnList.append(t)

    #for x in range(0,178):
    #    turningDistance(goal,turnList[x])

    #for x in range(0,testSize):
    #    print("Program " +str(x+1)+"\n")
    #    gen = Generator(4,4)
    #    prog = Program(gen.genPolygon(6))
    #    print(prog.turnFunc)
        #print(prog.poly.reorderAngles())
        #triTest = Polygon(prog.coords())
        #triTest.calcAngles()
        #triTest.coordDistance()
        #triTest.turningFunction()
    #    prog.execute(x)
    #    print (prog.toString()+"\n")
        #parse = Parser(prog.expressions())
        #prog.coords()
        #prog.execute()
        #t = parse.parseTriangle()
        #turnList.append(t)
    #    print("\n******************************************\n")

    #for x in range(0,testSize):
    #    for y in range(0,testSize):
    #        print("Turning distance from func " + str(x+1) + " to func "+ (str(y+1)))
    #        turningDistance(turnList[x],turnList[y])

if __name__ == "__main__":
    main()
