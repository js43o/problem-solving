function solution(order) {
    let answer = 0;
    const temp = [];
    let orderIdx = 0;
    let curBox = 1;
    
    while (orderIdx < order.length && curBox <= order.length) {
        if (order[orderIdx] === curBox) {
            answer += 1;
            curBox += 1;
            orderIdx += 1;
            continue;
        }
        
        if (temp.length > 0 && temp[temp.length - 1] === order[orderIdx]) {
            temp.pop();
            answer += 1;
            orderIdx += 1;
            continue;
        }
        
        temp.push(curBox);
        curBox += 1;
    };
    
    while (orderIdx < order.length && temp.length && temp[temp.length - 1] === order[orderIdx]) {
        temp.pop();
        answer += 1;
        orderIdx += 1;
    }
    
    return answer;
}