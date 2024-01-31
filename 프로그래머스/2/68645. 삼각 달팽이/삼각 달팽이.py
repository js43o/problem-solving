def solution(n):
    answer = []
    mat = [[0] * n for _ in range(n)]
    x = 0
    y = 0
    cur = 1
    
    while cur <= (n ** 2 + n) / 2:
        while y < n and mat[y][x] == 0:
            mat[y][x] = cur
            cur += 1
            y += 1
        
        y -= 1
        x += 1
        while x < n and mat[y][x] == 0:
            mat[y][x] = cur
            cur += 1
            x += 1
            
        x -= 2
        y -= 1
        while x >= 0 and y >= 0 and mat[y][x] == 0:
            mat[y][x] = cur
            cur += 1
            x -= 1
            y -= 1
        
        x += 1
        y += 2

    for idx, arr in enumerate(mat):
        answer.extend(arr[:idx + 1])
        
    return answer