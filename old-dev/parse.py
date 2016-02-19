import re

class Parser:
    def __init__(self,tree):
        self.tree = tree

    def parse_1argtree(self):
        command, argument = str.split(self.tree,'(')
        print (command)
        print (argument.strip(')'))

    def parse_2argtree(self):
        tokens = re.split('\W',self.tree)
        #print(tokens)
        print ("The original tree string is: " + str(self.tree))
        commands = [s for s in tokens if "forward" in s] #finds forward commands will need to go to regex when more commands are added
        print("The commands are: " + str(commands))
        arguments = re.findall(r'\d+',self.tree) #regex for pulling out decimal values for arguments
        print("The arguments are: " + str(arguments))


def main():
    #exampleTree = 'forward(24)'
    example2Tree = 'forward(forward(105, 23), 1)'
    #evalTree = Parser(exampleTree)
    #evalTree.parse_1argtree()
    newEvalTree = Parser(example2Tree)
    newEvalTree.parse_2argtree()


if __name__ == "__main__":
    main()
