def zifzag(input):
    arr = []
    for i in input:
        arr.append([1, 1])

    for i in range(1, len(input)):
        for j in range(i):
            if input[i] > input[j] and arr[i][0] <= arr[j][1]:
                arr[i][0] = arr[j][1] + 1
            elif input[i] < input[j] and arr[i][1] <= arr[j][0]:
                arr[i][1] = arr[j][0] + 1

    return max(sum(arr, []))
