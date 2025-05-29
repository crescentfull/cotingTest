def solution(emergency):
    answer = []
    
    rank = {value: num+1 for num, value in enumerate(sorted(emergency, reverse=True))}
    
    answer = [rank[i] for i in emergency]
        
    return answer