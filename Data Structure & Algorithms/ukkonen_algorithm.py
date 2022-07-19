"""
Author: Yeow Kin Ren
Student ID: 30762243
"""
import csv
import sys


class Tree:
    __slots__ = {"root",
                 "active_length",
                 "active_link",
                 "active_node",
                 "end",
                 "string",
                 "showStopper",
                 "output",
                 "prev_mid_node",
                 "prev_left_node"}

    def __init__(self):
        self.root = Node(start=0, end=None, leaf=False)
        self.active_length = 0
        self.active_link = self.root
        self.active_node = self.root
        self.end = End()
        self.string = ""
        self.showStopper = False
        self.output = []
        self.prev_mid_node = None
        self.prev_left_node = None

    def ukkonen(self, string):
        """
        Constructing suffix trees by implementing the ukkonen's Algorithm

        Precondition: None
        Time complexity:    Best case: O(n) where n is the length of the string.
                            Worst case: O(n) where n is the length of the string.
        Space complexity: O(1)
        Aux space complexity: O(1)
        :param string: A string, for the suffix tree to build upon
        :return: None
        """
        self.string = string
        s = string
        n = len(s)
        i, j = 0, 0
        self.active_node = self.root
        while i < n:
            j = j
            self.end.end = i
            self.prev_mid_node = None
            self.prev_left_node = None
            while j <= i:
                print("+++++++++++", i, j)
                index = self.get_index(j)
                # If there exist a suffix link then traverse to the node else begin from root
                if self.active_node.suffix_link is not None:
                    print("iflink1", self.show_data(self.active_node), self.show_data(self.active_node.suffix_link))
                    link = self.active_node.suffix_link
                    suffixJ = self.active_node.suffixJ
                    # self.active_node = self.active_node.suffix_link.parent
                    self.active_node = self.root
                else:
                    print("elselink1", self.show_data(self.active_node))
                    self.active_node = self.root
                    link = self.root
                # self.active_node = self.root
                # link = self.root
                if link != self.root or self.root.edge[index] is not None:  # the
                    if link == self.root:
                        print("iflink2")
                        child = link.edge[index]
                        tempj = j
                    else:
                        print("elselink2", suffixJ + j, suffixJ, j)
                        child = link
                        tempj = suffixJ + j
                    # child = link.edge[index]
                    # tempj = j
                    if not self.showStopper:
                        self.active_length = 0
                    length_child = child.end.end - child.start + 1
                    # if the data is over the node or equal the node
                    while i - tempj > length_child or \
                            ((i - tempj == length_child) and
                             child.edge[self.get_index(tempj + length_child)] is not None):
                        # traverse to next node Skip Count
                        self.active_node = child
                        print("while traverse", self.show_data(child), " -> ",
                              self.show_data(child.edge[self.get_index(tempj + length_child)]))
                        new_index = self.get_index(tempj + length_child)
                        tempj += length_child
                        child = child.edge[new_index]
                        length_child = child.end.end - child.start + 1  # ??????
                        self.active_length = 0
                    print("End while", self.show_data(self.active_node), self.show_data(self.prev_mid_node))
                    while self.active_length + tempj <= i and s[tempj + self.active_length] == s[
                        child.start + self.active_length]:
                        # the string and node data must be equal to increment self.active_length)
                        self.active_length += 1
                    if child.leaf and self.active_length == length_child:  # Rule 1
                        # if matched until the second last of the active node, extend the node with i
                        j += 1
                        print("Rule1: extend")
                    elif i - tempj + 1 == self.active_length and s[child.start + self.active_length - 1] == s[
                        i]:  # Rule 3
                        # if the letter to be added already existed in the node, STOP all further processing in this
                        # phase and move on to the next phase
                        if self.prev_mid_node is not None and self.active_node is not self.root:  # Create suffix link
                            print("showstopper suffix link", self.show_data(self.prev_mid_node), self.show_data(self.active_node))
                            self.active_node.suffix_link = self.root
                            self.prev_mid_node.suffix_link = self.active_node
                        self.showStopper = True
                        self.active_node = self.root
                        print("Rule3: showstopper", self.show_data(self.active_node))
                        break
                    elif self.active_length <= length_child:  # Rule 2
                        if self.active_length < length_child:  # Rule 2 Case 1
                            # if matched until within the active node, branch out to new node
                            child_end = child.end.end
                            child.end = End(child.start + self.active_length - 1)  # Existing node shorten
                            if child.leaf:
                                left = Node(start=(child.end.end + 1), end=self.end)
                            else:
                                left = Node(start=(child.end.end + 1), end=End(child_end), leaf=False)
                            left.edge = child.edge
                            child.edge = [None] * 27
                            child.leaf = False  # Middle node connecting the new node and a shorten existing node
                            new_node = Node(start=i, end=self.end)  # Newly created node
                            i_new = self.get_index(i)
                            new_node.parent = child
                            child.edge[i_new] = new_node  # New node link to mid node
                            i_left = self.get_index(left.start)
                            left.parent = child
                            child.edge[i_left] = left  # Mid node link to exist node
                            self.showStopper = False
                            j += 1
                        elif not child.leaf and self.active_length == length_child:  # Rule 2 Case 2
                            # if matched until the end of the active node, add and connect new node
                            new_node = Node(start=i, end=self.end)
                            i_new = self.get_index(i)
                            new_node.parent = child
                            child.edge[i_new] = new_node
                            j += 1
                            self.showStopper = False

                        if self.prev_mid_node is not None:  # Create suffix link (Every internal node has a suffix link)
                            print("if1", tempj, j, self.show_data(self.prev_left_node))
                            self.prev_mid_node.suffix_link = child
                            self.prev_mid_node.suffixJ = tempj - j  # what is this?
                            # print(tempj, j)
                            if self.prev_left_node is not None:
                                self.prev_left_node.suffix_link = left
                                self.prev_left_node = left
                                if left.suffix_link is None:
                                    left.suffix_link = self.root

                            if child.suffix_link is None:  # if doesn't already exist a suffix link
                                child.suffix_link = self.root
                            self.prev_mid_node = child
                        else:
                            print("case 2 else")
                            self.active_node = child
                            if child.suffix_link is None:   # if doesn't already exist a suffix link
                                child.suffix_link = self.root
                            if not left.leaf:   # if left node is an internal node
                                print("enter")
                                self.prev_left_node = left
                                if left.suffix_link is None:
                                    left.suffix_link = self.root
                            self.prev_mid_node = child
                            self.prev_mid_node.suffixJ = tempj - j  # what is this?
                else:  # Add new node to the root
                    print("else new node")
                    new_node = Node(start=i, end=self.end)
                    self.root.edge[index] = new_node
                    new_node.parent = self.root
                    j += 1
                # j += 1
            i += 1

    def show_data(self, node):
        if node is None:
            return "No Suffix Link"
        if node.end is None:
            return "Root"
        return self.string[node.start:node.end.end + 1]

    def get_index(self, position):
        index = ord(self.string[position]) - 96
        if index < 0:
            index = 0
        return index

    def suffix(self, node=None, previous_length=0):
        """
        By traversing the suffix tree to obtain the suffix array
        :param node: The Node class
        :param previous_length: The current length of the suffix in the edge
        :return: A list containing the suffix array
        """
        if node is None:
            node = self.root
        for edge in node.edge:
            if edge is not None:
                nextNode = edge
                length = previous_length + (nextNode.end.end - nextNode.start + 1)
                if nextNode.leaf:
                    self.output.append(nextNode.start - previous_length)
                self.suffix(node=nextNode, previous_length=length)
        return self.output

    def visual(self, node=None, pad=""):
        if node is None:
            node = self.root
        pad += "-"
        for edge in node.edge:
            if edge is not None:
                nextNode = edge
                print(pad, self.show_data(nextNode), "(", nextNode.start, ",", nextNode.end.end, ")",
                      self.show_data(nextNode.suffix_link))
                self.visual(node=nextNode, pad=pad)
        return


class End:
    def __init__(self, end=0):
        self.end = end


class Node:
    __slots__ = {"leaf", "start", "suffixJ", "end", "edge", "suffix_link", "parent"}

    def __init__(self, end=None, start=0, leaf=True):
        self.leaf = leaf
        self.start = start
        self.suffixJ = 0
        self.end = end
        self.edge = [None] * 27
        self.suffix_link = None
        self.parent = None


if __name__ == '__main__':
    suffix = Tree()
    inputString = "aabbabaa"
    inputString = "abacabade" + "abc"
    suffix.ukkonen(inputString)
    suffix.visual()
    out = suffix.suffix()
    print(out)
