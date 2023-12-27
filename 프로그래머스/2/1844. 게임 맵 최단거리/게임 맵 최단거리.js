function solution(maps) {
    let dist = [...Array(maps.length)].map(_ => [...Array(maps[0].length)].map(__ => -1));
    let q = [[0, 0]];
    
    dist[0][0] = 1;
    
    while (q.length > 0) {
        const [y, x] = q[0];
        q = q.slice(1);
        
        if (y === maps.length - 1 && x === maps[0].length - 1) {
            break;
        }
        
        for (let [dy, dx] of [[-1, 0], [1, 0], [0, -1], [0, 1]]) {
            if (0 <= y + dy && y + dy < maps.length && 0 <= x + dx && x + dx < maps[0].length) {
                if (maps[y + dy][x + dx] === 1 && dist[y + dy][x + dx] === -1) {
                    dist[y + dy][x + dx] = dist[y][x] + 1;
                    q.push([y + dy, x + dx]);
                }
            }
        }
    }
    
    return dist[maps.length - 1][maps[0].length - 1];
}