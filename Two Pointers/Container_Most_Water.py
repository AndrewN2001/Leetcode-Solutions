def maxArea(heights):
    n = len(heights)
    res = 0
    for l in range(n):
        for r in range(l + 1, n):
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)
    return res

def maxArea_linear(heights):
    l, r = 0, len(heights) - 1
    res = 0
    while l < r:
        area = (r - l) * min(heights[l], heights[r])
        res = max(res, area)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return res

def main():
    test_array = [1, 7, 2, 5, 4, 7, 3, 6]
    print(maxArea_linear(test_array))

if __name__ == "__main__":
    main()