"""
######################################################################################
# In Python, Big Integer does not require explicit handling
# https://www.codementor.io/@arpitbhayani/how-python-implements-super-long-integers-12icwon5vk
# How Python internally manages & optimises the storage of large integers
######################################################################################
"""


# Given 2 large numbers. The numbers may not fit into long long int, the task is to add these 2 numbers.
def large_numbers(num1: str, num2: str) -> str:
    if int(num1) > int(num2):
        num1, num2 = num2, num1
    num2_rev = "".join(reversed(num2))
    num1_rev = "".join(reversed(num1))
    carry = 0
    result = []
    for i in range(len(num1)):
        sum = int(num1_rev[i]) + int(num2_rev[i]) + carry
        carry = sum // 10
        output = sum % 10
        result += str(output)
    for i in range(len(num1), len(num2)):
        sum = int(num2_rev[i]) + carry
        carry = sum // 10
        output = sum % 10
        result += str(output)
    return "".join(reversed(result))


def python_large_numbers(a, b):
    return a + b


def multiply(a, no, size):
    carry = 0
    for i in range(size):
        product = a[i] * no + carry
        a[i] = product % 10
        carry = product // 10
    # to handle the carry
    while carry:
        a[size] = carry % 10
        carry = carry // 10
        size += 1
    return a, size


def big_factorial(n):
    # Given an integer, find its factorial which may be large and may not fit into integer
    a = [0] * 1000
    a[0] = 1
    size = 1
    for i in range(2, n):
        a, size = multiply(a, i, size)
    # Print the Result in the Reverse Order
    # size - 1 to 0
    for i in range(size - 1, -1, -1):
        print(a[i], end="")
    print()
    return


if __name__ == '__main__':
    num1 = "64"
    num2 = "12999"
    print(large_numbers(num1, num2))
    print(big_factorial(100))
