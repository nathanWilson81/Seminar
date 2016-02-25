import random
import re
import math


class Program(object):
    """ Chromosomal representation for the Genetic Algorithm
    """

    def __init__(self,chromosome):
        self.chromosome = chromosome #Linked List to define the genome
        self.fitness = 0
        self.size = 0

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

class Triangle:
    def __init__(self, name,xLen,yLen,yAngle):
        self.name = name
        self.xLen = xLen
        self.yLen = yLen
        self.zLen = 0
        self.xAngle = 0
        self.yAngle = yAngle
        self.zAngle = 0
        self.perimeter = 0

    def findZLen(self):
        self.zLen = math.sqrt((self.xLen**2) + (self.yLen**2) - (2 *
                                                                 self.xLen * self.yLen * math.cos(self.yAngle)))  # Law of cosines
        return self.zLen

    def findPerimeter(self):
        self.findZLen()
        self.perimeter = self.xLen + self.yLen + self.zLen
        print("Perimeter is: "+str(self.perimeter)+" pixels")
        return self.perimeter

    def findZAngle(self):
        self.zAngle = math.asin(
            (math.sin(math.degrees(self.yAngle)) * self.xLen) / self.zLen)  # Law of Sines
        return math.degrees(self.zAngle)

    def findArea(self):
        # Heron's Formula
        area = math.sqrt(self.perimeter * (self.perimeter - self.xLen) * (self.perimeter - self.yLen) * (self.perimeter - self.zLen))
        print("Area is: "+str(area)+" pixels")
        return area





class Individual:
    def __init__(self, commands, arguments):
        self.progString = []
        self.commandList = commands
        self.argumentList = arguments
        print("The commands are " + str(self.commandList))
        print("The arguments are " + str(self.argumentList))

    def map_string(self):
        for x in range(0, len(self.argumentList)):
            self.progString.append(
                '%s(%s)' % (self.commandList[x], self.argumentList[x]))
        print(self.progString)


class Generator:
    """Used to generate Programs from a set of rules"""
    def __init__(self, minCommands, maxCommands):
        self.commands = []
        self.arguments = []
        ########## CONSTANTS FOR GENERATION ####################
        self.MAX_DIRECTION_COMMAND_VALUE = 150
        self.MIN_DIRECTION_COMMAND_VALUE = 50
        self.MAX_ANGLE_COMMAND_VALUE = 178
        self.MIN_ANGLE_COMMAND_VALUE = 1
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
        chromosome.insert("home()")
        i = random.randrange(self.MIN_DIRECTION_COMMAND_VALUE, self.MAX_DIRECTION_COMMAND_VALUE)
        chromosome.insert("forward(" + str(i)+")")
        i = random.randrange(self.MIN_ANGLE_COMMAND_VALUE, self.MAX_ANGLE_COMMAND_VALUE)
        chromosome.insert("right("+str(i)+")")
        i = random.randrange(self.MIN_DIRECTION_COMMAND_VALUE, self.MAX_DIRECTION_COMMAND_VALUE)
        chromosome.insert("forward(" + str(i)+")")
        return chromosome

class Parser:
    """Used to Parse the generated Programs"""
    def __init__(self, expr):
        self.expr=expr

    def parseTriangle(self):
        forward = int(''.join(x for x in self.expr[0] if x.isdigit()))
        right = int(''.join(x for x in self.expr[1] if x.isdigit()))
        forward2 = int(''.join(x for x in self.expr[2] if x.isdigit()))
        return forward,forward2,right



def main():
    for x in range(0,100):
        print("Program " +str(x+1)+"\n")
        gen = Generator(4,4)
        prog = Program(gen.genTriangle())
        print (prog.toString()+"\n")
        parse = Parser(prog.expressions())
        xLen,yLen,yAngle = parse.parseTriangle()
        t = Triangle('Test',xLen,yLen,yAngle)
        per = t.findPerimeter()
        area = t.findArea()
        print("Ratio of perimeter to area is: "+ str(per/area))
        print("\n******************************************\n")



if __name__ == "__main__":
    main()
