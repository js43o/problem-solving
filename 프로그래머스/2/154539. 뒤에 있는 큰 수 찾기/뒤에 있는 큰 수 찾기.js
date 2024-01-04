function solution(numbers) {
    let result = numbers.map(() => -1);
    let stack = [];
    
    const top = () => stack[stack.length - 1];
    
    for (let i = 0; i < numbers.length; i++) {
        while (stack.length > 0 && numbers[top()] < numbers[i]) {
            result[top()] = numbers[i];
            stack.pop();
        }
        
        stack.push(i);
    }
    
    return result;
}