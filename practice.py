def find_outlier(integers):
    even_list = []
    odd_list = []
    for int in integers:
        if int%2 == 0:
            even_list.append(int)
        else:
            odd_list.append(int)
    if len(even_list) > len(odd_list):
        return odd_list[0]
    else:
        return even_list[0]
    
    
        
    


print(find_outlier([2, 4, 6, 8, 10, 3]))