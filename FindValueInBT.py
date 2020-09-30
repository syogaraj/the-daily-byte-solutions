"""
This question is asked by Google. Given the reference to the root of a binary search tree and a search value, return the reference to the node that contains the value if it exists and null otherwise.
Note: all values in the binary search tree will be unique.

Ex: Given the tree...

        3
       / \
      1   4
and the search value 1 return a reference to the node containing 1.
Ex: Given the tree

        7
       / \
      5   9
         / \ 
        8   10
and the search value 9 return a reference to the node containing 9.
Ex: Given the tree

        8
       / \
      6   9
and the search value 7 return null.
"""

class MockBTNode():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def find_value(ref, value):
    if not ref:
        return None
    if ref.value == value:
        return ref
    if value > ref.value and (ref.left and value > ref.left.value):
        return find_value(ref.right, value)
    elif value < ref.value and (ref.right and value < ref.right.value):
        return find_value(ref.left, value)
    else:
        return None

if __name__ == "__main__":
    ### test1
    m = MockBTNode(8)
    m.right = MockBTNode(9)
    m.left = MockBTNode(6)
    assert find_value(m, 7) == None

    ### test2
    m = MockBTNode(8)
    m.right = MockBTNode(9)
    m.left = MockBTNode(6)
    assert find_value(m, 10) == None

    ### test3
    m = MockBTNode(3)
    m.right = MockBTNode(4)
    m.left = MockBTNode(1)
    value_node = find_value(m, 1)
    assert isinstance(value_node, MockBTNode)
    assert value_node.value == 1
    assert value_node.left == None
    assert value_node.right == None

    ### test4
    m = MockBTNode(7)
    m.right = MockBTNode(9)
    m.left = MockBTNode(5)
    m.right.right = MockBTNode(10)
    m.right.left = MockBTNode(8)
    value_node = find_value(m, 9)
    assert isinstance(value_node, MockBTNode)
    assert value_node.value == 9
    assert value_node.left.value == 8
    assert value_node.right.value == 10
