import random



class Program(object):
    def __init__(self,genome):
        self.genome = genome #Linked List to define the genome
        self.fitness = 0
        self.size = 0 

    def getFitness(self):
        print("Not implemented yet")

    def getSize(self):
        print("Not yet implemented")

    def toString(self):
        print("Not yet implemented")



class Node(object):
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
        genome = LinkedList()
        genome.insert("home()")
        i = random.randrange(self.MIN_DIRECTION_COMMAND_VALUE, self.MAX_DIRECTION_COMMAND_VALUE)
        genome.insert("forward(" + str(i)+")")
        i = random.randrange(self.MIN_ANGLE_COMMAND_VALUE, self.MAX_ANGLE_COMMAND_VALUE)
        genome.insert("right("+str(i)+")")
        i = random.randrange(self.MIN_DIRECTION_COMMAND_VALUE, self.MAX_DIRECTION_COMMAND_VALUE)
        genome.insert("forward(" + str(i)+")")
        return genome

class Parser:
    def __init__(self, commands, arguments):
        self.commandList = commands
        self.argumentList = arguments
        self.progList = []

    def combine(self):
        for x in range(0, len(self.commandList)):
            self.progList.append(self.commandList[x])
            self.progList.append(str(self.argumentList[x]))
        # print(self.progList)
        self.remove0()
        self.format_list()

    def remove0(self):
        homeCount = self.progList.count('0')
        if homeCount > 0:
            for x in range(0, homeCount):
                self.progList.remove('0')
        #print("The amount of 0s is: "+str(homeCount))

    def format_list(self):
        mystring = " ".join(self.progList)
        print(mystring)


def main():
    for x in range(0,100):
        print("Program " +str(x+1))
        gen = Generator(4,4)
        print (gen.genTriangle().toString())
        print("\n******************************************\n")



if __name__ == "__main__":
    main()
