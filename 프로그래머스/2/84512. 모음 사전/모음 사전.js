
function solution(word) {
    const gap = [781, 156, 31, 6, 1];
    const face = ['A', 'E', 'I', 'O', 'U'];
    let answer = word.length;
    
    Array.from(word).forEach((w, i) => {
        answer += gap[i] * face.indexOf(w);
    });
    
    return answer;
}