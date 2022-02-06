"""
#################################################################
Author: Yeow Kin Ren
Copyright 2013, Yeow Kin Ren, All rights reserved.
#################################################################
Binary Search Tree
"""


class Node(object):
    def __init__(self, parent=None, left=None, right=None, value=None):
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

    def get_value(self):
        return self.value



class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def search(self, value, node=None):
        if node is None:
            node = self.root
        while True:
            if node.value == value:
                break
            elif node.value < value:
                node = node.right
            else:
                node = node.left
        return node

    def insert(self, value):
        new_node = Node(value=value)
        if self.root is None:
            self.root = new_node
        else:
            node = self.root
            while True:
                if node.value < value:
                    if node.right is not None:
                        node = node.right
                    else:
                        node.right = new_node
                        break
                else:
                    if node.left is not None:
                        node = node.left
                    else:
                        node.left = new_node
                        break
            new_node.parent = node

    def delete(self, value):
        """

        :param value:
        :return:
        """
        node = self.search(value)
        parent = node.parent
        # Case 1: No child - simply remove the node
        if node.left is None and node.right is None:
            if parent.value < value:
                parent.right = None
            else:
                parent.left = None
        # Case 3: 2 children - get the in order successor to replace the node to be deleted
        elif node.left is not None and node.right is not None:

            succ = self.in_order_successor(node)

            if node == self.root:
                self.root = succ
            succ.parent.left = None
            succ.parent = parent
            succ.left = node.left
            node.left.parent = succ
            succ.right = node.right
            node.right.parent = succ
        # Case 2: 1 child - replace the node with its child
        else:
            if node.right is not None:
                node.right.parent = parent
                node = node.right
            else:
                node.left.parent = parent
                node = node.left

            if parent.value < node.value:
                parent.right = node
            else:
                parent.left = node

    def in_order_successor(self, node):
        # Get the minimum key value in the right subtree
        if node.right is not None:
            return self.get_min(node.right)
        parent = node.parent
        while parent is not None:
            if node != parent.right:
                break
            node = parent
            parent = parent.parent
        return parent

    def get_min(self, node=None):
        if node is None:
            node = self.root
        current = node
        # loop down to find the leftmost leaf
        while current is not None:
            if current.left is None:
                break
            current = current.left
        return current


    def display(self):
        """Reference: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
        """
        print("################################")
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)
        print("################################")

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % (str(node.value))
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % str(node.value)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % (str(node.value))
            u = len(s)
            first_line = s + (x * '_') + ((n - x) * ' ')
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # 2 children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % (str(node.value))
        u = len(s)
        first_line = ((x + 1) * ' ') + ((n - x - 1) * '_') + s + (y * '_') + ((m - y) * ' ')
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)

        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    bst.display()
    bst.delete(40)
    bst.display()
    bst.delete(30)
    bst.display()
    bst.delete(20)
    bst.display()
    bst.delete(80)
    bst.display()
