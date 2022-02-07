"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
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

    def is_left(self, node):
        if self.left is not None and self.left.value == node.value:
            return True
        return False

    def is_right(self, node):
        if self.right is not None and self.right.value == node.value:
            return True
        return False

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

    def search(self, value, node=None):
        if node is None:
            node = self.root
        if node.value == value:  # match
            return node
        elif value < node.value:  # search left subtree
            if node.left is not None:
                return self.search(value, node=node.left)
        else:  # search right subtree
            if node.right is not None:
                return self.search(value, node=node.right)
        return node  # unsuccessful search

    # def delete(self, value):
    #     # 473
    #     node = self.search(value)
    #     if node.left is not None and node.right is not None:    # has 2 children
    #         replacement = node.left
    #         node.parent.left = replacement
    #         replacement.
    #     parent = node.parent
    #
    #
    #
    #     parent = node.parent
    #     if len(self) == 1:
    #         self.root.set_black()  # special case: ensure that root is black
    #     elif node is not None:
    #         n = node.num_children()    #TODO
    #         if n == 1:  # deficit exists unless child is a red leaf
    #             c = next(self.children(node))
    #             if not c.is_red_leaf():
    #                 self.fix_deficit(node, c)
    #             elif n == 2:  # removed black node with red child
    #                 if node.left.is_red_leaf():
    #                     node.left.set_black()
    #                 else:
    #                     node.right.set_black()
    #
    # def fix_deficit(self, z, y):
    #     if not y.get_colour():  # y is black; will apply Case 1 or 2
    #         x = y.get_red_child()
    #         if x is not None:   # Case 1: Node y Is Black and Has a Red Child x
    #             old_color = z.get_colour()  # Case 1: y is black and has red child x; do ”transfer”
    #             middle = self.restructure(x)
    #             middle.red = old_color  # middle gets old color of z
    #             middle.left.set_black()  # children become black
    #             middle.right.set_black()
    #         else:   # Case 2: y is black, but no red children; recolor as ”fusion”
    #             y.set_red()
    #             if z.is_red():
    #                 z.set_black()
    #             elif not z != self.root:
    #                 self.fix_deficit(z.parent, z.sibling())  # recur upward

    # else:  # Case 3: y is red; rotate misaligned 3-node and repeat
    #     self.rotate(y)
    #     y.set_black()
    #     z.set_red()
    #     if z == y.right:
    #         self.fix_deficit(z, z.left)
    #     else:
    #         self.fix_deficit(z, z.right)

    # Case 2: Node y Is Black and Both Children of y Are Black (or None).
    # Case 3: Node y Is Red.

    def insert(self, value):
        new_node = Node(value=value)
        if self.root is None:
            self.root = new_node
        else:
            self.set_temp_parent(new_node)
        self.resolve_red(new_node)

    def resolve_red(self, node):
        if self.root is None or node == self.root:
            self.root = node
            node.set_black()
        else:
            parent = node.parent
            if parent.get_colour():  # Double red problem
                uncle = parent.get_sibling()
                if uncle is None or not uncle.get_colour():  # Case 1: Uncle is Black or None
                    mid = self.restructure(node)  # Perform trinode restructuring
                    mid.set_black()
                    if mid.left is not None:
                        mid.left.set_red()
                    mid.right.set_red()
                else:  # # Case 2: Uncle is Red
                    print("check")
                    grand = parent.parent
                    grand.set_red()  # Perform recolouring
                    grand.left.set_black()
                    grand.right.set_black()
                    self.resolve_red(grand)
            else:
                print("exit")

    def set_temp_parent(self, new_node):
        current_node = self.root
        while True:
            if new_node.get_value() < current_node.get_value():
                if current_node.left is None:
                    new_node.parent = current_node
                    current_node.left = new_node
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

    def display(self):
        """Reference: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
        Node colour: *:red :black
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
            line = '%s' % (str(node.value) + ('*' if node.get_colour() else ''))
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % (str(node.value) + ('*' if node.get_colour() else ''))
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % (str(node.value) + ('*' if node.get_colour() else ''))
            u = len(s)
            first_line = s + (x * '_') + ((n - x) * ' ')
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % (str(node.value) + ('*' if node.get_colour() else ''))
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
    rbt = RedBlackTree()
    rbt.insert(4)
    rbt.insert(7)
    rbt.insert(12)
    rbt.display()

    rbt.insert(15)
    rbt.insert(3)
    rbt.insert(5)
    rbt.insert(14)
    rbt.display()

    rbt.insert(18)
    rbt.display()
