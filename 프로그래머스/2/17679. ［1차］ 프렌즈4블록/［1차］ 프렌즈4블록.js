const isSame = (i, j, mat) => {
    const target = mat[i][j];
    return mat[i + 1][j] === target && mat[i][j + 1] === target && mat[i + 1][j + 1] === target;
}

function solution(m, n, board) {
    let answer = 0;
    const mat = board.map(row => Array.from(row));
    
    const eraseBlock = (i, j) => {
        for (let [dy, dx] of [[i, j], [i + 1, j], [i, j + 1], [i + 1, j + 1]]) {
            if (mat[dy][dx] !== '') {
                answer += 1;
                mat[dy][dx] = '';
            }
        }
    }
    
    const rearrangeBlocks = () => {
        for (let j = n - 1; j >= 0; j--) {
            let validBlocks = [];
            
            for (let i = m - 1; i >= 0; i--) {
                if (mat[i][j] !== '') {
                    validBlocks.push(mat[i][j]);
                }
            }
            
            validBlocks.push(...[...Array(m - validBlocks.length)].map(() => ''));
            validBlocks = validBlocks.reverse();
            
            for (let i = m - 1; i >= 0; i--) {
                mat[i][j] = validBlocks[i];
            }
        }
    }
    
    const checkSameBlocks = () => {
        const toErase = [];
        
        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                if (i + 1 >= m || j + 1 >= n || mat[i][j] === '') {
                    continue;
                }
                
                if (isSame(i, j, mat)) {
                    toErase.push([i, j]);
                }
            }
        }
        
        if (toErase.length === 0) {
            return;
        }
        
        while (toErase.length > 0) {
            const [i, j] = toErase.pop();
            eraseBlock(i, j);
        }
        
        rearrangeBlocks();
        checkSameBlocks();
    }
    
    checkSameBlocks();
    
    return answer;
}