def lnds(input):
    arr = [1] * len(input)

    for i in range(1, len(input)):
        for j in range(i):
            if input[i] >= input[j] and arr[j] >= arr[i]:
                arr[i] = arr[j] + 1

    return max(arr)


print(lnds([5, 3, 4, 8, 6, 7]))

