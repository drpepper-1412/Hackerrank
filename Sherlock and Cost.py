def cost(B):
    arr = []
    for k in range(len(B)):
        arr.append([0, 0])

    B = [(1, i) for i in B]

    for i in range(1, len(B)):
        arr[i][0] = max(B[i][0] - B[i-1][0] + arr[i-1][0], abs(B[i][0] - B[i-1][1]) + arr[i-1][1])
        arr[i][1] = max(B[i][1] - B[i-1][0] + arr[i-1][0], abs(B[i][1] - B[i-1][1]) + arr[i-1][1])

    return max(arr[-1])


