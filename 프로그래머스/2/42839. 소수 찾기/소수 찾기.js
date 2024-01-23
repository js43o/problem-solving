function solution(numbers) {
    let answer = new Set();
    numbers = Array.from(numbers).map(n => Number(n));

    const isPrime = (number) => {
        if (number < 2) {
            return false;
        }
        
        for (let i = 2; i <= Math.sqrt(number); i++) {
            if (number % i === 0) {
                return false;
            }
        }

        return true;
    }

    const dfs = (visited) => {
        const number = Number(visited.map(idx => numbers[idx]).join(''));
        if (isPrime(number)) {
            answer.add(number);
        }
        
        if (visited.length === numbers.length) {
            return;
        }

        numbers.forEach((number, idx) => {
            if (!visited.includes(idx)) {
                dfs([...visited, idx]);
            }
        });
    }
    
    numbers.forEach((number, idx) => {
        dfs([idx], numbers);
    });
    
    return answer.size;
}