function solution(prices) {
    let result = [...Array(prices.length)].map(() => 0);
    let stack = [];
    
    for (let i = 0; i < prices.length; i++) {
        while (stack.length > 0 && prices[stack[stack.length - 1]] > prices[i]) {
            result[stack[stack.length - 1]] = i - stack[stack.length - 1];
            stack.pop();
        }
               
        stack.push(i);
    }
    
    while (stack.length > 0) {
        result[stack[stack.length - 1]] = prices.length - stack[stack.length - 1] - 1;
        stack.pop();
    }
    
    return result;
}