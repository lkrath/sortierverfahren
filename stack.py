import node

class Stack:
    
    head = node.Node(None)
    
    def __init__(self):
        self.stack = "Stack"

    def isEmpty(self):
        return head.getContent() == None

    def top(self):
        return head

    def pop(self):
        global head
        x = head
        head = n.getNext()
        n.setContent(n.getNext())
        return x

    def push(self, n):
        global head
        if head.getContent() != 0:
            head.setContent(n.getContent())
        head = n
        
