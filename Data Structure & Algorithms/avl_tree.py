"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

AVL tree
(Adelson-Velsky & Landis) A self-balancing binary search tree

  z                                y
 /  \                            /   \
T1   y     Left Rotate(z)       z      x
    /  \   - - - - - - - ->    / \    / \
   T2   x                     T1  T2 T3  T4
       / \
     T3  T4

     z                                      y
    / \                                   /   \
   y   T4      Right Rotate (z)          x      z
  / \          - - - - - - - - ->      /  \    /  \
 x   T3                               T1  T2  T3  T4
/ \
T1   T2

"""


class Node(object):
    def __init__(self, parent=None, left=None, right=None, value=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value
        self.height = 1

    def get_sibling(self):
        if self.parent is None or self.parent.left is None:
            sibling = None
        elif self == self.parent.left:
            sibling = self.parent.right
        else:
            sibling = self.parent.left
        return sibling

    # def left_height(self):
    #     return self.left.height if self.left is not None else 0
    #
    # def right_height(self):
    #     return self.right.height if self.right is not None else 0

    def get_value(self):
        return self.value


class AVLTree:

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
        """Iteratively insertion"""""
        # Perform normal BST insertion
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

            node = new_node
            # Retrace back to the root
            while node.parent is not None:
                node = node.parent
                # Update the height of the ancestor node
                node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
                # Get the balance factor
                balance = self.get_balance(node)

                # Case 1 - Left Left
                if balance > 1 and value < node.left.value:
                    return self.right_rotate(node)

                # Case 2 - Right Right
                if balance < -1 and value > node.right.value:
                    return self.left_rotate(node)

                # Case 3 - Left Right (Double rotation)
                if balance > 1 and value > node.left.value:
                    node.left = self.left_rotate(node.left)
                    return self.right_rotate(node)

                # Case 4 - Right Left (Double rotation)
                if balance < -1 and value < node.right.value:
                    node.right = self.right_rotate(node.right)
                    return self.left_rotate(node)

    def left_rotate(self, z):
        y = z.right
        t2 = y.left         # T2 may be None
        if self.root == z:  # Relocate pointer if root
            self.root = y

        # Perform rotation
        y.left = z
        if z.parent is None:
            y.parent = None
        else:
            y.parent = z.parent
            if z.parent.value < y.value:

                z.parent.right = y
            else:
                z.parent.left = y

        z.parent = y

        z.right = t2
        if t2 is not None:
            t2.parent = z

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y    # Return the new subtree's root

    def delete(self, value):
        # TODO
        # Perform standard BST delete
        node = self.search(value)
        parent = node.parent
        # Case 1: No child - simply remove the node
        if node.left is None and node.right is None:
            if parent.value < value:
                parent.right = None
            else:
                parent.left = None
            node = parent
        # Case 3: 2 children - get the in order successor to replace the node to be deleted
        elif node.left is not None and node.right is not None:

            succ = self.in_order_successor(node)

            if node == self.root:
                self.root = succ
            succ.parent.left = None
            temp = succ.parent
            succ.parent = parent
            succ.left = node.left
            node.left.parent = succ
            succ.right = node.right
            node.right.parent = succ
            node = temp
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

        # Retrace back to the root
        while node.parent is not None:
            node = node.parent
            # Step 2 - Update the height of the ancestor node
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

            # Step 3 - Get the balance factor
            balance = self.get_balance(node)

            # Step 4 - If the node is unbalanced,
            # then try out the 4 cases
            # Case 1 - Left Left
            if balance > 1 and self.get_balance(node.left) >= 0:
                return self.right_rotate(node)

            # Case 2 - Right Right
            if balance < -1 and self.get_balance(node.right) <= 0:
                return self.left_rotate(node)

            # Case 3 - Left Right
            if balance > 1 and self.get_balance(node.left) < 0:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

            # Case 4 - Right Left
            if balance < -1 and self.get_balance(node.right) > 0:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def right_rotate(self, z):
        y = z.left
        t3 = y.right            # T3 may be None
        if self.root == z:      # Relocate pointer if root
            self.root = y

        # Perform rotation
        y.right = z

        if z.parent is None:
            y.parent = None
        else:
            y.parent = z.parent
            if z.parent.value < y.value:
                z.parent.right = y
            else:
                z.parent.left = y
        z.parent = y

        z.left = t3
        if t3 is not None:
            t3.parent = z

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y        # Return the new root

    def get_height(self, node):
        return node.height if node is not None else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node is not None else 0


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
            line = '%s' % (str(node.value) + ('(' + str(node.height) + ')'))
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % (str(node.value) + ('(' + str(node.height) + ')'))
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % (str(node.value) + ('(' + str(node.height) + ')'))
            u = len(s)
            first_line = s + (x * '_') + ((n - x) * ' ')
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # 2 children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % (str(node.value) + ('(' + str(node.height) + ')'))
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
    avl = AVLTree()
    # avl.insert(10)
    # avl.display()
    # avl.insert(20)
    # avl.display()
    # avl.insert(30)
    # avl.display()
    # avl.insert(40)
    # avl.display()
    # avl.insert(50)
    # avl.display()
    # avl.insert(25)
    # avl.display()

    nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

    for num in nums:
        avl.insert(num)

    avl.display()

    avl.delete(10)
    avl.display()
    
