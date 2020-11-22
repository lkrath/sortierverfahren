import stack, node

s = stack.Stack()
n1 = node.Node(7)
n2 = node.Node(8)
n3 = node.Node(4)
n4 = node.Node(12)

s.push(n1)
s.push(n2)
s.push(n3)
s.push(n4)
for i in range(4):
    print(s.pop().getContent())