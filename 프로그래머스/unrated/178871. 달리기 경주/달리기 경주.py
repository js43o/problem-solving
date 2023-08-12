def solution(players, callings):
    answer = []
    indexOfPlayer = dict()
    playerOfIndex = dict()
    
    for idx in range(len(players)):
        indexOfPlayer[players[idx]] = idx
        playerOfIndex[idx] = players[idx]
    
    for calling in callings:
        idx = indexOfPlayer[calling]
        antecedent = playerOfIndex[idx - 1]
        
        indexOfPlayer[calling], indexOfPlayer[antecedent] = indexOfPlayer[antecedent], indexOfPlayer[calling]
        playerOfIndex[idx], playerOfIndex[idx - 1] = playerOfIndex[idx - 1], playerOfIndex[idx]
        
    for idx in range(len(players)):
        answer.append(playerOfIndex[idx])
        
    return answer