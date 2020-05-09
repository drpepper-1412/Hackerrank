def fg(height, bloom, wilt):

    dic = {height[i]: j for i, j in enumerate(zip(bloom, wilt))}

    for k in range(1, len(height)):
        move_cuz_of_date = k
        move_cuz_of_height = k

        for m in range(k-1, -1, -1):
            if ((dic[height[k]][0] > dic[height[m]][1] or dic[height[k]][1] < dic[height[m]][0])
                    and height[k] > height[m]):
                move_cuz_of_height = m
            elif dic[height[k]][0] <= dic[height[m]][1] and dic[height[k]][1] >= dic[height[m]][0]:
                if height[k] < height[m]:
                    move_cuz_of_date = m
                else:
                    break
        if move_cuz_of_date != k:
            height.insert(move_cuz_of_date, height.pop(k))
        elif move_cuz_of_height != k:
            height.insert(move_cuz_of_height, height.pop(k))

    return height
