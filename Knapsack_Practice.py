def knapsack(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if weights[n - 1] > capacity:
        return knapsack(weights, values, capacity, n - 1)
    else:
        include = values[n - 1] + knapsack(weights, values, capacity - weights[n - 1], n - 1)
        exclude = knapsack(weights, values, capacity, n - 1)
        return max(include, exclude)

def main():
    weights = [2, 3, 7, 1]
    values = [10, 40, 60, 30]
    capacity = 8
    n = len(values)

    max_value = knapsack(weights, values, capacity, n)
    print("The maximum value that can be obtained is:", max_value)

if __name__ == "__main__":
    main()
