from ast import List
from collections import defaultdict
from math import *
def total_distance_between(l1 : List, l2:List) :
    t = [abs(a-b) for a,b in zip(sorted(l1),sorted(l2))]
    return sum(t)

def similary_score(l1 : List, l2:List):
    dict = defaultdict(lambda:0)
    for l in l2 :
        dict[l] = dict[l] + 1
    
    score = 0
    for k in l1:
        score += dict[k]*k
    return score

col1 = []
col2 = []

with open("./inputs/day1", 'r') as file:
    for line in file:
        values = line.split()
        col1.append(int(values[0]))
        col2.append(int(values[1]))

print(total_distance_between(col1, col2))
print(similary_score(col1, col2))
        

