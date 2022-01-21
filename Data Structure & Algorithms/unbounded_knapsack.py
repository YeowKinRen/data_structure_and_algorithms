"""


"""


def unbounded_knapsack(weight, value, N):
    memo = [0] * (N + 1)  # N is the total weight
    memo[0] = 0
    for bag_weight in range(1, N + 1):
        for j in range(len(weight)):  # go through items
            if weight[j] <= bag_weight:
                balance = bag_weight - weight[j]
                profit = value[j] + memo[balance]
                if profit > memo[bag_weight]:  # if there's new optimal
                    memo[bag_weight] = profit
    # memo[i] = memo[i-1]
    print(memo)
    return memo[N]


if __name__ == '__main__':
    weight = [5, 8, 9]
    value = [5, 11, 12]
    N = 12
    print(unbounded_knapsack(weight, value, N))
