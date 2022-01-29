"""
#################################################################
Author: Yeow Kin Ren
Copyright 2013, Yeow Kin Ren, All rights reserved.
#################################################################
Red-Black Tree
"""


class Node(object):
    def __init__(self, parent=None, left=None, right=None, value=None, colour=True):
        self.red = colour  # red by default
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value

    def get_sibling(self):
        if self.parent is None or self.parent.left is None:
            sibling = None
        elif self == self.parent.left:
            sibling = self.parent.right
        else:
            sibling = self.parent.left
        return sibling

    def set_red(self):
        self.red = True

    def set_black(self):
        self.red = False

    def get_colour(self):
        return self.red

    def get_value(self):
        return self.value

    def insert_child(self, child):
        if child.get_value() < self.get_value():
            self.left = child
        else:
            self.right = child
        child.parent = self

    def print_colour(self):
        return "RED" if self.get_colour() else "BLACK"


class RedBlackTree(object):

    def __init__(self):
        self.root = None

    def relink(self, parent, child, make_left_child):
        if make_left_child:
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent

    def rotate(self, node):
        parent = node.parent
        grand = parent.parent
        if grand is None:
            self.root = node
            node.parent = None
        else:
            self.relink(grand, node, parent == grand.left)
        if node == parent.left:
            self.relink(parent, node.right, True)
            self.relink(node, parent, False)

        else:
            self.relink(parent, node.left, False)
            self.relink(node, parent, True)

    def restructure(self, node):
        """Trinode Restructuring"""
        parent = node.parent
        grand = parent.parent
        if (node == parent.right) == (parent == grand.right):
            self.rotate(parent)
            return parent
        else:
            self.rotate(node)
            self.rotate(node)
            return node

    def insert(self, value):
        new_node = Node(value=value)
        self.resolve_red(new_node)

    def resolve_red(self, node):
        if self.root is None or node == self.root:
            self.root = node
            node.set_black()
        else:
            parent = self.set_temp_parent(node)
            if parent.get_colour():  # Double red problem
                uncle = parent.get_sibling()
                if uncle is None or not uncle.get_colour():  # Case 1: Uncle is Black or None
                    mid = self.restructure(node)  # Perform trinode restructuring
                    mid.set_black()
                    if mid.left is not None:
                        mid.left.set_red()
                    mid.right.set_red()
                else:  # # Case 2: Uncle is Red
                    grand = parent.parent
                    grand.set_red()     # Perform recolouring
                    grand.left.set_black()
                    grand.right.set_black()
                    self.resolve_red(grand)

    def set_temp_parent(self, new_node):
        current_node = self.root
        while True:
            if new_node.get_value() < current_node.get_value():
                if current_node.left is None:
                    new_node.parent = current_node
                    current_node.right = new_node
                    return current_node
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    new_node.parent = current_node
                    current_node.right = new_node
                    return current_node
                else:
                    current_node = current_node.right

    def visualize(self, node=None, length=0):
        if node is None:
            print("#########################")
            node = self.root
        print("-"*length, "Node Value:", node.value, "Colour:", node.print_colour())
        if node.left is None:
            print("-NONE parent:", node.value)
        else:
            self.visualize(node=node.left, length=length+1)
        if node.right is None:
            print("-NONE parent:", node.value)
        else:
            self.visualize(node=node.right, length=length+1)





if __name__ == '__main__':
    rbt = RedBlackTree()
    rbt.insert(4)
    rbt.visualize()
    rbt.insert(7)
    rbt.visualize()
    rbt.insert(12)
    rbt.visualize()
    rbt.insert(15)
    rbt.visualize()
    rbt.insert(3)
    rbt.visualize()
