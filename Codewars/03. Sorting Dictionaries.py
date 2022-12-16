def sort_dict(d):
    sortedValues = []

    for k, v in d.items():
        sortedValues.append(v)
        
    sortedValues.sort(reverse = True)

    res = []
    i = 0
    
    while i < len(sortedValues):
        for key, value in d.items():
            if value == sortedValues[i]:
                temp = (key, value)
                del d[key]
                break
        i += 1
        res.append(temp)

    return res
