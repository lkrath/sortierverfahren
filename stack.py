import node

class Stack:
    
    def __init__(self):
        self.stack = "Stack"
        self.head = None
        #self.head = node.Node(None)

    def isEmpty(self):
        return self.head == None

    def top(self):
        if self.head != None:
            return self.head.getContent()
        else:
            return "Nichts drin"

    def pop(self):
        x = self.head
        if self.head != None:
            self.head = self.head.getNext()
        return x

    def push(self, n):
        if n != None:
            n.setNext(self.head)
            self.head = n


        #if self.head != None:
        #    self.head.setNext(self.head)
        #self.head = n