function solution(topping) {
    let answer = 0;
    let count1 = [...Array(10001)].map(() => 0);
    let count2 = [...Array(10001)].map(() => 0);
    let total1 = 0;
    let total2 = new Set(topping).size;
    topping.forEach(t => count2[t] += 1);
    
    for (let t of topping) {
        if (count1[t] === 0) {
            total1 += 1;
        }
        
        count1[t] += 1;
        
        if (count2[t] === 1) {
            total2 -= 1;
        }
        
        count2[t] -= 1;
        
        if (total1 === total2) {
            answer += 1;
        }
    }
    
    return answer;
}