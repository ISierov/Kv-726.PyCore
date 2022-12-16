def next_pal(val):
    i = 1
     
    while True:
        next_val = val + i
        str_val = str(next_val)
        count_digits = len(str_val)
        
        if count_digits % 2 == 0:
            separator = int(count_digits / 2)
            sliced1 = str_val[:separator]
            sliced2 = str_val[separator:]
        else:
            separator = int((count_digits - 1) / 2)
            sliced1 = str_val[:separator]
            sliced2 = str_val[separator+1:]
        
        if sliced1 == sliced2[::-1]:
            break  
        else: 
            i += 1 
    
    return next_val
