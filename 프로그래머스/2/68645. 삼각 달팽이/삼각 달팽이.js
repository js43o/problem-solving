function solution(n) {
    const mat = [...Array(n)].map(_ => [...Array(n)].map(_ => 0));
    let [y, x, cur] = [-1, 0, 1];
    
    for (let i = 0; i < n; i++) {   // 직선 경로의 개수는 총 n개
        for (let k = 0; k < n - i; k++) {   // i번째 직선 경로의 길이는 (n - i)
            if (i % 3 === 0) {
                y += 1;
            }
            
            if (i % 3 === 1) {
                x += 1;
            }
            
            if (i % 3 === 2) {
                y -= 1;
                x -= 1;
            }
            
            mat[y][x] = cur;
            cur += 1;
        }
    }
    
    return mat.map((arr, idx) => arr.slice(0, idx + 1)).reduce((acc, cur) => [...acc, ...cur]);
}