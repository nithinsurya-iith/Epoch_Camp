import numpy as np

class Node:
    def __init__(self, value, children = (), op = None, op_args = ()):
        self.value = value
        self.children = children
        self.op = op
        self.op_args = op_args

    def __add__(self, other):
        if not isinstance(other, Node):
            other = Node(other)
        return Node(self.value + other.value, children=(self,other), op='add')

    def __sub__(self, other):
        if not isinstance(other, Node):
            other = Node(other)
        return Node(self.value - other.value, children=(self,other), op='sub')

    def __mul__(self, other):
        if not isinstance(other, Node):
            other = Node(other)
        return Node(self.value * other.value, children=(self,other), op='mul')

    def __truediv__(self, other):
        if not isinstance(other, Node):
            other = Node(other)
        return Node(self.value / other.value, children=(self,other), op='div')

    def __pow__(self, other):
        if not isinstance(other, Node):
            other = Node(other)
        return Node(self.value ** other.value, children=(self,other), op='pow')
