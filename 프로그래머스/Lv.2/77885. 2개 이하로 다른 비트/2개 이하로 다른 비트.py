def solution(numbers):
    answer = []
    for number in numbers:
        first = 1
        while True:
            if number & first == 0:
                temp = number | first
                second = first >> 1
                while second >= 1:
                    if temp & second > 0:
                        temp ^= second
                        break
                
                answer.append(temp)
                break
                
            first <<= 1
        
    return answer