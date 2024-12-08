import re
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

def calculate(match):
        a, b = int(match.group(1)), int(match.group(2))
        return a * b

def count_match(line) :
    matches = re.finditer(pattern, line)
    res = 0
    for match in matches:
        res += calculate(match)
    return res

results = 0
with open("./inputs/day3", 'r') as file:
    line = ""
    for l in file :
         line += l
         
    listdont = line.split("don't()")
    results += count_match(listdont[0])
    for k in range(1, len(listdont)):
        listdo = listdont[k].split('do()',1)[1:]
        for doline in listdo :
            results += count_match(doline)


print(results)