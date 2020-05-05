def fg(height, bloom, wilt):

    dic = {height[i]: j for i, j in enumerate(zip(bloom, wilt))}

    for k in range(1, len(height)):
        for m in range(k):
            if (dic[height[k]][0] > dic[height[m]][1] and height[k] > height[m]) or \
                    (dic[height[k]][0] <= dic[height[m]][1] and height[k] < height[m]):
                height.insert(m, height.pop(k))
                break

    return height
