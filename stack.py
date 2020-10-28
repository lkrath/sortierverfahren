import node

class Stack:
    
    head = node.Node(None)
    
    def __init__(self):
        self.stack = "Stack"

    def isEmpty(self):
        return self.head.getContent() == None

    def top(self):
        return self.head

    def pop(self):
        x = self.head
        self.head = self.head.getNext()
        self.head.setContent(self.head.getNext())
        return x

    def push(self, n):
        if self.head.getContent() != None:
            self.head.setContent(n.getContent())
        self.head = n
        
