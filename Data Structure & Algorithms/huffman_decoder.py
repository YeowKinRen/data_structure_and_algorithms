"""
#################################################################
Author: Yeow Kin Ren
Copyright (c) 2022 YeowKinRen, All rights reserved.
#################################################################

Huffman Decoder implementation using LZSS
Lempel–Ziv–Storer–Szymanski (LZSS) is a lossless data compression algorithm

"""
# TODO
import sys


class HuffmanTree:
    def __init__(self):
        self.tree = [None]

    def add(self, bitstring, data):
        """
        Traverse the tree based of the value of the bit string and set the character into the node.

        Precondition: None
        Time complexity:    Best case: O(n) where n is the length of the bit string.
                            Worst case: O(n) where n is the length of the bit string.
        Space complexity: O(2^n) where is the length of the bit string
        Aux space complexity: O(1)
        :param bitstring: String representing the bit string of the Huffman codeword
        :param data: String representing the character of the Huffman codeword
        :return: None
        """
        minTree = 2 ** (len(bitstring) + 1) - 1
        if len(self.tree) <= minTree:
            extra = minTree - len(self.tree)
            self.tree += ([None] * extra)
        parent = 0
        for i in range(len(bitstring)):
            if bitstring[i] == "0":
                parent = parent * 2 + 1
            elif bitstring[i] == "1":
                parent = parent * 2 + 2
        self.tree[parent] = data

    def find(self, bitstring, parent):
        """
        Traverse to the subsequent node based on the value of the bit string
        Precondition: None
        Time complexity:    Best case: O(1).
                            Worst case: O(1).
        Space complexity: O(1)
        Aux space complexity: O(1)
        :param bitstring: String representing the bit string of the Huffman codeword
        :param parent: integer value of the parent index
        :return: If the traversal reaches the leaf node, return True, string of the Huffman codeword else False, child
                index
        """
        if bitstring == "0":      # traverse to the left subtree
            child = parent * 2 + 1
        else:                   # traverse to the right subtree elif element == "1":
            child = parent * 2 + 2
        if self.tree[child] is None:
            return False, child
        else:
            return True, self.tree[child]


def eliasDecoder(bitstring, i, code=False):
    """
    decode an Elias omega-coded bit string starting from position i

    Precondition: None
    Time complexity:    Best case: O(n) where n is the length of the encoded Elias (omega) code.
                        Worst case: O(n) where n is the length of the encoded Elias (omega) code.
    Space complexity: O(1)
    Aux space complexity: O(1)
    :param bitstring: String value consists of 0 and 1 representing Elias omega-coded bit-string
    :param i: integer value of the initial position to begin decoding
    :param code: boolean value True to retrieve the Huffman codeword and False for the decoded decimal integer
    :return: integer value, i, of the subsequent position of bitstring and the decoded Elias omega-coded integer or the
            Huffman codeword
    """
    s = bitstring
    j = i
    while s[i] == "0":  # the minimal binary code of the length component
        decimal = 0
        while i <= j:
            if decimal == 0:
                decimal = decimal * 2 + 1
            else:
                if s[i] == "1":
                    decimal = decimal * 2 + 1
                elif s[i] == "0":
                    decimal = decimal * 2
            i += 1
        decimal += 1
        j += decimal
    decimal = 0
    while i <= j:       # the minimal binary code of the encoded Elias omega-coded integer
        if s[i] == "1":
            decimal = decimal * 2 + 1
        elif s[i] == "0":
            decimal = decimal * 2
        i += 1
    if code:            # Retrieve the Huffman codeword from the decoded length
        return i + decimal, s[i:i + decimal]
    return i, decimal


def LZSSDecoder(bitstring):
    """
    Decode the encoded LZSS characters and recover the original strings

    Precondition: None
    Time complexity:    Best case: O(n) where n is the length of the string.
                        Worst case: O(n) where n is the length of the string.
    Space complexity: O(n) where n is the input to the encoded LZSS characters
    Aux space complexity: O(n) where n is the input to the encoded LZSS characters
    :param bitstring: String value consists of 0 and 1 representing Elias omega-coded bit-string
    :return: String of the input to the encoded LZSS characters
    """
    s = bitstring
    output = []
    # header decoding
    i, headerLen = eliasDecoder(s, 0)
    huffmanTree = HuffmanTree()
    while headerLen:
        n = i
        decimal = 0             # ASCII value
        while i <= n + 6:
            if s[i] == "1":
                decimal = decimal * 2 + 1
            elif s[i] == "0":
                decimal = decimal * 2
            i += 1
        i, code = eliasDecoder(s, i, code=True)     # Huffman codeword
        huffmanTree.add(code, chr(decimal))         # Constructing the Huffman binary tree
        headerLen -= 1
    # data decoding
    i, dataLen = eliasDecoder(s, i)         # The total number of Format-0/1 fields
    while dataLen:
        if s[i] == "1":         # Format 1
            i += 1
            flag = False
            p = 0
            while not flag:     # Traverse through the Huffman binary Tree
                flag, p = huffmanTree.find(s[i], p)
                i += 1
            output.append(p)
        elif s[i] == "0":       # Format 0
            i += 1
            i, offset = eliasDecoder(s, i)    # Decoding the offset
            i, length = eliasDecoder(s, i)    # Decoding the length
            format1Output = []
            temp = offset
            while length:
                if offset == 0:
                    offset = temp
                format1Output.append(output[-offset])
                offset -= 1
                length -= 1
            output += format1Output
        dataLen -= 1
    output = "".join(output)
    return output


def read_file(filename):
    f = open(filename, "r")
    inputString = f.read()
    return inputString


def write_file(output):
    with open("output_decoder_lzss.txt", "w") as text_file:
        text_file.write(f"{output}")


if __name__ == '__main__':
    argument_00 = sys.argv[0]  # huffman_decoder.py
    argument_01 = sys.argv[1]  # <encoder output file.txt>
    encoderOutput = read_file(argument_01)
    # encoderOutput = read_file("encoder_output5_L40_B40.txt")
    decoderOutput = LZSSDecoder(encoderOutput)
    write_file(decoderOutput)
