import node

class Stack:
    
    def __init__(self):
        self.stack = "Stack"
        self.head = None
        #self.head = node.Node(None)

    def isEmpty(self):
        if self.head.getContent() == None or self.head == None:
            return True
        else:
            return False

    def top(self):
        return self.head.getContent()

    def pop(self):
        x = self.head
        self.head = self.head.getNext()
        return x

    def push(self, n):
        if self.head == None:
            self.head = n
        else:
            #self.head.setNext(self.head.getContent(head))
            self.head.setContent(n.getContent())
        
