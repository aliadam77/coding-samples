def solution(s,d,dict1):
    for i in dict1:
        if dict1[i][0] == d:
            if i == s:
                return dict1[s][1]
    
    total = 1
    
    
    
        
    
            
            
            
    return
def main():
    dict1 = {'hey':['girl',5],'gay':['boy',10]}
    list1 = [['hey','girl',5],['gay','boy',10]]
    sol = solution ('hey','girl',dict1)
    print(sol)
    
main()
