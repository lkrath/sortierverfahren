class Node:

    
    def __init__(self, content):
        self.node = "Node"
        self.__content = content
        self.__next_node = None

    def getContent(self):
        return self.__content
    
    def setContent(self, x):
        self.__content = x

    def getNext(self):
        return self.__next_node

    def setNext(self, x):
        self.__next_node = x   