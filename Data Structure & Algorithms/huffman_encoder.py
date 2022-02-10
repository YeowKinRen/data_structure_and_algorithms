"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Huffman coding Algorithm
Introduced by David A. Huffman


"""
# TODO
import sys


class Heap:
    """
    Simple heap data structure for Huffman encoding
    """

    def __init__(self, heap=None):
        self.heap = [] if heap is None else heap

    def heapify(self, parent_index=0):
        """
        Perform heapify starting from the root
        """
        heap = self.heap
        length = len(heap)
        if length == 1:
            return
        parent = parent_index
        while 2 * parent < length:
            child = 2 * parent
            if child + 1 < length and heap[child + 1][1] < heap[child][1]:
                child += 1
            elif child + 1 < length and heap[child + 1][1] == heap[child][1]:
                if len(heap[child + 1][0]) < len(heap[child][0]):
                    child += 1
            # if freq equal check for the str length sink the lesser str length
            if heap[parent][1] < heap[child][1]:
                return
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child

    def del_min(self):
        heap = self.heap
        last_element = heap.pop()
        if not heap:
            return last_element
        item = heap[0]
        heap[0] = last_element
        self.heapify()
        return item

    def add(self, element):
        self.heap.append(element)
        self.heapify()


def decimalToBinary(number, elias=False):
    """
    Converts an integer value from decimal numeral system to binary numeral system

    Precondition: None
    Time complexity:    Best case: O(n) where n is the length of the string.
                            Worst case: O(n) where n is the length of the string.
    Space complexity: O(1)
    Aux space complexity: O(1)
    :param number: an integer representing the decimal numeral system
    :param elias: a boolean value, True to set the most significant bit to "0"
    :return: Binary bit string of the argument
    """
    if number < 0:
        return 'Not positive'
    i = 0
    result = []
    while number >> i:
        result.append('1' if number >> i & 1 else '0')
        i += 1
    result.reverse()
    if elias:
        result[0] = "0"
    result = "".join(result)
    return result


def elias(integer):
    """
    Performs Elias (omega) encoding on the argument

    Precondition: None
    Time complexity:    Best case: O(n^2) where n is the length of the bit string of the argument.
                        Worst case: O(n^2) where n is the length of the bit string of the argument.
    Space complexity: O(n^2) where n is the length of the bit string of the argument.
    Aux space complexity: O(n^2) where n is the length of the bit string of the argument.
    :param integer: The integer value to be encode
    :return: The Elias omega code of the argument
    """
    output = [decimalToBinary(integer)]
    while len(output[-1]) > 1:
        length = decimalToBinary(len(output[-1]) - 1, elias=True)
        output.append(length)
    output.reverse()
    output = "".join(output)
    return output


def headerEncode(string):
    """
    Construct the header of the characters encoded by using Huffman code.

    Precondition: None
    Time complexity:    Best case: O(n) where n is the length of the string.
                        Worst case: O(n) where n is the length of the string.
    Space complexity: O(n) where n is the length of the string.
    Aux space complexity: O(n) where n is the length of the string.
    :param string: string consists of ASCII characters in the range [32,127] and/or 10.
    :return:
    """
    output = []
    sortStr = sorted(string)
    strUniqFreq = []
    stringList = [None] * 128
    previous = ""
    for s in sortStr:
        if s == previous:
            strUniqFreq[-1][1] += 1
        else:
            previous = s
            stringList[ord(s)] = []
            strUniqFreq.append([s, 1])
    s = [i for i in strUniqFreq]
    h = Heap(s)
    h.heapify()
    while len(h.heap) > 1:
        x = h.del_min()
        y = h.del_min()
        for charX in x[0]:
            stringList[ord(charX)].append("0")
        for chary in y[0]:
            stringList[ord(chary)].append("1")
        xy = [x[0] + y[0], x[1] + y[1]]
        h.add(xy)
    for s in strUniqFreq:
        i = ord(s[0])
        stringList[i].reverse()
        stringList[i] = "".join(stringList[i])
    length = len(strUniqFreq)
    e = elias(length)
    output.append(e)
    for s in strUniqFreq:
        i = ord(s[0])
        b = decimalToBinary(i)
        output.append(b)
        huffman = stringList[i]
        length = len(huffman)
        e = elias(length)
        output.append(e)
        output.append(huffman)
    o = "".join(output)
    return o


def read_file(filename):
    f = open(filename, "r")
    inputString = f.read()
    return inputString


def write_file(output):
    with open("output_header.txt", "w") as text_file:
        text_file.write(f"{output}")


if __name__ == '__main__':
    argument_00 = sys.argv[0]  # huffman_encoder.py
    argument_01 = sys.argv[1]  # <input text file>
    inputString = read_file(argument_01)
    # inputString = read_file("headerInput.txt")
    outputString = headerEncode(inputString)
    write_file(outputString)
