function solution(files) {
    const getGroup = (str) => {
        let head = '';
        let number = '';
        let flag = 'HEAD';
        
        for (let ch of str) {
            if (ch.match(/[a-zA-Z\s\.\-]/)) {
                if (flag === 'HEAD') head += ch;
                if (flag === 'NUMBER') break;
            }
            
            if (ch.match(/\d/)) {
                if (flag === 'HEAD') flag = 'NUMBER';
                if (flag === 'NUMBER') {
                    if (number.length === 5) break;
                    number += ch;
                }
            }
        }
        
        return [head.toLowerCase(), Number(number)];
    }
    
    const answer = files.sort((a, b) => {
        let [headA, numberA] = getGroup(a);
        let [headB, numberB] = getGroup(b);
        
        if (headA !== headB) return headA < headB ? -1 : 1;
        if (numberA !== numberB) return numberA < numberB ? -1 : 1;
        
        return 0;
    });
    
    return answer;
}