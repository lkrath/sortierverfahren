# Quick Sort aber alleine

def quick_sort(list):
    lenght = len(list)
    
    if lenght < 2:
        return list
    else:
        pivot_point = list.pop()

    greater = []
    less = []

    for item in list:
        if item > pivot_point:
            greater.append(item)
        else:
            less.append(item)
    
    return quick_sort(less) + [pivot_point] + quick_sort(greater)

print(quick_sort([4,7,3,8,4,7,4,5,1,4,9,8,5]))