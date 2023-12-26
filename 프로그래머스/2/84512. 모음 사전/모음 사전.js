const letters = ['A', 'E', 'I', 'O', 'U'];
let answer = -1;
let count = 0;

function dfs(cur, target) {
    if (cur === target) {
        answer = count;
        return;
    }
    
    count += 1;
    
    if (cur.length >= 5) {
        return;
    }

    for (let i = 0; i < 5; i++) {
        dfs(cur + letters[i], target);
    }
}

function solution(word) {
    dfs('', word);
    return answer;
}