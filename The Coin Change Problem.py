
# def getWays(n, c):
#
#     from itertools import product
#
#     c = sorted(c)
#     ways = {c[0]: [[c[0]]]}
#
#     for i in range(c[0]+1, n+1):
#         solution = []
#         for j in filter(lambda x: x <= i, c):
#             if j * 2 == i:
#                 solution.append([j]*2)
#             if i == j:
#                 solution.append([i])
#             else:
#                 if i-j in ways.keys() and j in ways.keys():
#                     for k in ways[i - j]:
#                         tem_k = k.copy()
#                         tem_k.append(j)
#                         if sorted(tem_k) not in solution:
#                             solution.append(sorted(tem_k))
#                     for l in product(ways[j], ways[i - j]):
#                         if sorted(l[0] + l[1]) not in solution:
#                             solution.append(sorted(l[0] + l[1]))
#         ways[i] = solution
#
#     return len(ways[n])
#
# def count(S, m, n):
#     # We need n+1 rows as the table is constructed
#     # in bottom up manner using the base case 0 value
#     # case (n = 0)
#     table = [[0 for x in range(m)] for x in range(n + 1)]
#
#     # Fill the entries for 0 value case (n = 0)
#     for i in range(m):
#         table[0][i] = 1
#
#     # Fill rest of the table entries in bottom up manner
#     for i in range(1, n + 1):
#         for j in range(m):
#             # Count of solutions including S[j]
#             x = table[i - S[j]][j] if i - S[j] >= 0 else 0
#
#             # Count of solutions excluding S[j]
#             y = table[i][j - 1] if j >= 1 else 0
#
#             # total count
#             table[i][j] = x + y
#
#     return table[n][m - 1]

def getWays(n, c):
    # Create an array of potential outcome up until n+1
    arr = [0] * (n+1)

    # Essentially we want to reduce n to 0 to make it a valid solution. So we can set arr[0]=1
    arr[0] = 1

    # We are going to iterate through the c list
    for i in range(len(c)):
        # j is the outcome that can be potentially achieved by c[i]
        for j in range(c[i], n+1):
            # We just need then to update arr[j]
            arr[j] += arr[j - c[i]]

    return arr[n]

