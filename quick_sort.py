# Quick Sort

zahlen = [7, 9, 12, 75, 8, 78, 3, 14]

def quick(list):
    if len(list) > 1:
        pivot = list.pop()
    else:
        return list   
        
    more = []
    less = []

    for number in list:
        if number > pivot:
            more.append(number)

        else:
            less.append(number)

    return quick(less) + [pivot] + quick(more)

    

print(quick(zahlen))