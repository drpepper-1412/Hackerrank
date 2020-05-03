def bn(input):
    backup = input.copy()
    arr = [False] * len(input)
    arr[0] = True

    for i in range(2, len(input)):
        maxi = [0, input[0]]
        for x, y in enumerate(input[1:i-1], 1):
            if y > maxi[1]:
                maxi[0], maxi[1] = x, y
        input[i] += maxi[1]
        if not maxi[0] or arr[maxi[0]]:
            arr[i] = True

    if arr[-1]:
        return max(input[:-1] + [input[-1] - backup[-1], input[-1] - backup[0]])
    return max(input)