function solution(skill, skill_trees) {
    const indexMap = new Map();
    let answer = 0;
    Array.from(skill).forEach((ch, idx) => indexMap[ch] = idx);
    
    for (skill_tree of skill_trees) {
        let curIdx = -1;
        let flag = true;
        
        for (ch of skill_tree) {
            if (indexMap[ch] >= 0) {
                if (indexMap[ch] === curIdx + 1) {
                    curIdx = indexMap[ch];
                } else {
                    flag = false;
                    break;
                }
            }
        }
        
        if (flag) {
            answer += 1;   
        }   
    }
    
    return answer;
}