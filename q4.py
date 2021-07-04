
lst = [3,2,1,4,10,15,11,12,14,5]

def candyStore(lst, N, K):
    diff = N - K
    if diff == 1:
        minimum = min(lst)
        maximum = max(lst)
    else:
        minimum = 0
        maximum = 0
        sorted_list = sorted(lst)
        min_lst = sorted_list[:diff]
        max_lst = sorted_list[-diff:]
        
        for i in range(len(min_lst)):
            minimum = min_lst[i] + minimum
        for j in range(len(min_lst)):
            maximum = max_lst[j] + maximum    
            
            
    print(minimum, maximum)
candyStore(lst, 10, 3)