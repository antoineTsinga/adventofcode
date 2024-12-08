
from typing import List

def level_is_not_safe(level: List[int]) -> int:
    index_where_unsafe = 0
    diff = level[-1] - level[0] # > 0 supposé croissant; <0 supposé décroissant
    
    for k in range(1,len(level)) :
        
        if diff == 0 or abs(level[k]-level[k-1])>3 or abs(level[k]-level[k-1])<1:
            index_where_unsafe = k
            break
        if level[k]<=level[k-1] and diff > 0 :
            index_where_unsafe = k
            break
        if level[k]>=level[k-1] and diff < 0 :
            index_where_unsafe = k
            break
    
    return index_where_unsafe

def reports_safe(reports: List[List[int]]) -> int:
    count = 0

    for level in reports:
        if not level_is_not_safe(level):
            count += 1

    return count

def reports_safe_dampener(reports: List[List[int]]) -> int:
    count = 0
    
    for level in reports:
        index_where_unsafe = level_is_not_safe(level) 
        if index_where_unsafe == 0:
            count += 1
        else :
            l1 = [element for i, element in enumerate(level) if i != index_where_unsafe]
            l2 = [element for i, element in enumerate(level) if i != index_where_unsafe - 1]
            if not level_is_not_safe(l1) or not level_is_not_safe(l2):
                count += 1

    return count

lines = []
with open("./inputs/day2", 'r') as file:
    for line in file:
        lines.append([int(i) for i in line.split()])


print(reports_safe(lines))
print(reports_safe_dampener(lines))
