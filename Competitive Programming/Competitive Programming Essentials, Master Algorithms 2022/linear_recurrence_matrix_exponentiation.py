
def power(a, b): # O(logb)
    res = 1
    while b:
        if b & 1:  # last bit is set
            res *= a
        a *= a
        b //= 2
    return res


mod = 1e9+7

def power2(a, b): # O(logb)
    # modular exponentiation
    res = 1
    while b:
        if b & 1:  # last bit is set
            res *= a
            res %= mod
        a *= a
        a %= mod
        b //= 2
    return int(res)

if __name__ == '__main__':
    print(power(2, 20))
    print(power2(2, 200))
