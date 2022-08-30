
def isValid(s):
    # Write your code here
    from collections import Counter
    dic = Counter(s)
    dic_val = Counter(dic.values())
    if len(dic_val) == 1:
        return "YES"
    if len(dic_val) > 2:
        return "NO"    
    if 1 in dic_val.keys() and  dic_val[1] == 1:
      return "YES"
    max_key = max( dic_val.keys())
    if  dic_val[ max_key ] == 1 and abs(list(dic_val.keys())[0] - list(dic_val.keys())[1]) == 1:
      return "YES"
    return "NO"
    
    
    
    
    
      
    
    
print(isValid("aaabbbcccc"))    