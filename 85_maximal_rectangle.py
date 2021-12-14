def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    height = [0] * (n + 1)
    ans = 0
    for row in matrix:
        for i in range(n):
            height[i] = height[i] + 1 if row[i] == '1' else 0
            print('i: {} | height[i]: {}'.format(i, height[i]))
        stack = [-1]
        for i in range(n + 1):
            print('i: {}'.format(i))
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - 1 - stack[-1]
                ans = max(ans, h * w)
                print('ans: {} || h: {} || w: {}'.format(ans, h, w))
            stack.append(i)
            print('stack: {}'.format(stack))
    return ans


maximalRectangle([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
                 "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])
