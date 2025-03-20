def solution(clothes):
    category_dict = {}
    
    for name, category in clothes:
        if category in category_dict:
            category_dict[category] += 1
        else:
            category_dict[category] = 1
            
    result = 1
    
    print(category_dict)
    
    for category, count in category_dict.items():
        result *= (count + 1)
        
    result -= 1
    
    print(result)
    
    return result