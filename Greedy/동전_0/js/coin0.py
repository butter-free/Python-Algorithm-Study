N, K = map(int, input().split())

value_of_coins = []
for _ in range(N):
    value_of_coins.append(int(input()))

min_count = 0
for i in range(N-1, -1, -1):
    if K < value_of_coins[i]:
        continue

    min_count += K // value_of_coins[i]
    K %= value_of_coins[i]

    if K == 0:
        break

print (min_count)
