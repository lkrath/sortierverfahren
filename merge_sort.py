# Merge Sort 

zahlen = [7, 9, 12, 75, 8, 78, 3, 14]

def merge_sort(list):
    if len(list) > 2:
        half = (len(list)-1) // 2
        left = merge_sort(list[:half])
        right = merge_sort(list[half:])

        return merge(left, right)

    else:
        return list

#    if len(list) <= 1:
#        return list;

#    left, right = merge_sort(list[:len(list) // 2]), merge_sort(list[len(list) // 2:])

#    return merge(left, right)    



def merge(lista, listb):
    listc = []
    a, b = 0, 0
    while a < len(lista) and b < len(listb):
        if lista[a] < listb[b]:
            listc.append(lista[a])
            a += 1
        else:
            listc.append(listb[b])

        if a == len(lista): 
            listc.extend(listb[b:])
        if b == len(listb):
            listc.extend(lista[a:])
    return listc


print(merge_sort(zahlen))