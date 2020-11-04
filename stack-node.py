import stack, node

s = stack.Stack()
n1 = node.Node(7)
n2 = node.Node(8)

s.push(n1)
s.push(n2)
print(s.isEmpty())
print((s.pop()).getContent())
