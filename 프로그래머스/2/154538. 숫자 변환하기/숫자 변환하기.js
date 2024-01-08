class Queue {
    constructor(array) {
        this.data = [...array];
        this.front = 0;
    }
    
    push(item) {
        this.data.push(item);
    }
    
    popleft() {
        const result = this.data[this.front];
        this.front += 1;
        
        return result;
    }
    
    isEmpty() {
        return this.data.length === this.front;
    }
}

function solution(x, y, n) {
    const dist = [...Array(1000001)].map(() => -1);
    let q = new Queue([x]);
    dist[x] = 0;
    
    while (!q.isEmpty()) {
        const cur = q.popleft();
        if (cur === y) {
            break;    
        }
        
        for (let next of [cur * 2, cur * 3, cur + n]) {
            if (next <= 1000000 && dist[next] === -1) {
                dist[next] = dist[cur] + 1;
                q.push(next);
            }
        }
    }
    
    return dist[y];
}