
def power(a, b):
    res = 1
    while b:
        if b & 1:  # last bit is set
            res *= a
        a *= a
        b //= 2
    return res



if __name__ == '__main__':
    print(power(2, 20))
