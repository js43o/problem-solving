function solution(arr) {
    let answer = [0, 0];
    
    const divide = (startY, startX, endY, endX) => {
        if (startY === endY - 1 && startX === endX - 1) {
            const number = arr[startY][startX];
            answer[number] += 1;
            
            return number;
        }
    
        const midLen = (endY - startY) / 2;
        const leftTop = divide(startY, startX, startY + midLen, startX + midLen);
        const rightTop = divide(startY, startX + midLen, startY + midLen, endX);
        const leftBottom = divide(startY + midLen, startX, endY, startX + midLen);
        const rightBottom = divide(startY + midLen, startX + midLen, endY, endX);
        
        if (leftTop === rightTop && leftTop === leftBottom && leftTop === rightBottom) {
            answer[leftTop] -= 3;
            return leftTop;
        }
        
        return null;
    }
    
    divide(0, 0, arr.length, arr.length);
    
    return answer;
}