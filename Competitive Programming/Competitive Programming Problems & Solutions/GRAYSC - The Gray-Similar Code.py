# https://www.codechef.com/problems/GRAYSC
# https://discuss.codechef.com/t/graysc-editorial/388


# cook your dish here
n = int(input())
array = list(map(int, input().split()))
out = False
if n >= 130:  # at least 65 values of xi
    print("Yes")
else:
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                x = array[i] ^ array[j] ^ array[k]
                if x in array[k + 1:n]:
                    print("Yes")
                    out = True
                    break
        if out:
            break
    if not out:
        print("No")


# n = int(input())
# array = list(map(int, input().split()))
# dic = {}
# for i in range(n):
#     if array[i] not in dic.keys():
#         dic[array[i]] = 1
#     else:
#         dic[array[i]] += 1
# out = False
# if n >= 130:  # at least 65 values of xi
#     print("Yes")
# else:
#     print(dic)
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 x = array[i] ^ array[j] ^ array[k]
#                 if array[i] in dic.keys():
#                     cnt = dic[array[x]]
#                 else:
#                     dic[array[i]] = 0
#                     cnt = dic[array[x]]
#
#
#                 if (array[i] == x):
#                     cnt -= 1
#                 if (array[j] == x):
#                     cnt -= 1
#                 if (array[k] == x):
#                     cnt -= 1
#                 if cnt >= 1:
#                     print("Yes")
#                     out = True
#                     break
#         if out:
#             break
#     if not out:
#         print("No")