class Node:

    def __init__(self, content):
        self.node = "Node"
        self.__content = content
        __next_node = None

#    def __init__(self):
#        self.node = "Node"
#        __next_node = None

    def getContent(self):
        return __content
    
    def setContent(self, x):
        __next_node = __content
        __content = x

    def getNext(self):
        return __next_node
        