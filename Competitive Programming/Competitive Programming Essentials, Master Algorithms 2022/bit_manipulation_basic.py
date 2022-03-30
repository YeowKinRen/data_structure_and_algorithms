

def odd_even(n):
    if n&1:
        print("odd")
    else:
        print("even")

def get_ith_bit(n, i):
    mask = 1<<i
    if n&mask > 0:
        print(1)
    else:
        print(0)

def clear_ith_bit(n, i):
    mask = ~(1<<i)
    return n&mask

def set_ith_bit(n, i):
    mask = 1<<i
    return n|mask

def update_ith_bit(n, i, v):
    clear_ith_bit(n, i)
    mask = v<<i
    return n|mask

def clear_last_ith_bit(n, i):
    """ ~0 == 11111
    11111<<i == 11000"""
    mask = (~0)<<i
    return n&mask

def clear_range_bit(n, i, j):
    a = (~0)<<(j+1) # 1111000000
    b = (1<<i)-1    # 0000001111
    mask = a|b      # 1111001111
    return n&mask

def replace(n, i, j, m):
    n = clear_range_bit(n, i, j)
    mask = m<<i
    return n|mask

def is_power_of_2(n):
    if (n&(n-1))==0:
        print("power of 2")

def is_power_of_4(n):
    if ((n & (n - 1)) == 0)and(n & 0xAAAAAAAA == 0):
        return True
    else:
        return False

def decoded(encoded, first):
    arr = [first]
    xor = first
    for i in range(len(encoded)):
        xor ^= encoded[i]
        arr.append(xor)
    return arr

def count_bit(n):
    """o(n):log(n)"""
    cnt = 0
    while n>0:
        last_bit = n&1
        cnt += last_bit
        n = n>>1
    return cnt

def count_bit_hack(n):
    cnt = 0
    while n>0:
        n = n&(n-1) # remove the last set bit
        cnt += 1
    return cnt

def convert_to_binary(n):
    ans = 0
    p = 1
    while n>0:
        last_bit = n&1
        ans += p*last_bit
        p = p*10
        n = n>>1
    return ans

def sort_by_bits( arr):

        for i in range(len(arr)):
            # bit_count() only in py3.10
            arr[i]+=bin(arr[i]).count('1')*10001
            # arr[i]+=(arr[i].bit_count())*10001
        arr.sort()
        for i in range(len(arr)):
            arr[i]=arr[i]%10001
        print(arr)
        return arr


def longest_consecutive_1(n):
    count = 0
    while n:
        n = n & (n<< 1)
        count +=1
    return count

def hammingDistance(x, y):
    n = x^y
    cnt = 0
    while n>0:
        n = n&(n-1) # remove the last set bit
        cnt += 1
    return cnt


if __name__ == '__main__':
    odd_even(5)
    sort_by_bits([0,1,2,3,4,5,6,7,8])