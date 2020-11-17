import stack, node

s = stack.Stack()
n1 = node.Node(7)
n2 = node.Node(8)
n3 = node.Node(4)

s.push(n1)
s.push(n2)
#s.push(n3)
print(s.isEmpty())
print((s.pop()).getContent())
print(s.top())
#print((s.pop()).getContent())