function solution(order) {
    const temp = [];
    let orderIdx = 0;
    let curBox = 1;
    
    while (orderIdx < order.length) {
        if (order[orderIdx] === curBox) {
            curBox += 1;
            orderIdx += 1;
            continue;
        }
        
        if (temp.length > 0 && temp[temp.length - 1] === order[orderIdx]) {
            temp.pop();
            orderIdx += 1;
            continue;
        }
        
        if (curBox > order.length && temp.length > 0 && temp[temp.length - 1] !== order[orderIdx]) {
            break;
        }
        
        temp.push(curBox);
        curBox += 1;
    };
    
    return orderIdx;
}
