function solution(sequence, k) {
    let start = 0;
    let end = 0;
    let answer = null;
    let cur = sequence[0];
    
    while (end < sequence.length && start < sequence.length) {
        if (cur < k) {
            end += 1;
            cur += sequence[end];
            continue;
        }
        
        if (cur > k) {
            cur -= sequence[start];
            start += 1;
            continue;
        }
        
        if (!answer || end - start < answer[1] - answer[0]) {
            answer = [start, end];
        }
        
        end += 1;
        cur += sequence[end];
    }
    
    return answer;
}