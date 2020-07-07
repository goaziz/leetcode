

def maxArea(height):
    res, l, r = 0, 0, len(height) - 1
    while l < r:
        h = min(height[l], height[r])
        res, l, r = max(res, h * (r - l)), l + (height[l] == h), r - (height[r] == h)
    return res


d = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(d))
