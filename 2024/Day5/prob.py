from math import floor


with open('input.txt', 'r') as file:
    input = file.read()
    
    
input = input.split('\n\n')
rules, pages = input[0], input[1]
rules = rules.split('\n')
pages = pages.split('\n')

before = {}
after = {}
for rul in rules:
    rul = rul.split('|')
    if rul[0] in before:
        before[rul[0]].append(rul[1])
    else:
        before[rul[0]] = [rul[1]]
        
    if rul[1] in after:
        after[rul[1]].append(rul[0])
    else:
        after[rul[1]] = [rul[0]]
        
        
        
        
def check_valid(page, i):
    checker = page[i]
    if checker in before:
        for b in before[checker]:
            if b in page[:i]:
                return False
    if checker in after:
        for a in after[checker]:
            if a in page[i+1:] and i+1 < len(page):
                return False
    return True

def swap_invalid(page, i):
    checker = page[i]
    if checker in before:
        for b in before[checker]:
            if b in page[:i]:
                b_pos = page.index(b)
                page[i], page[b_pos] = page[b_pos], page[i]
                return
    if checker in after:
        for a in after[checker]:
            if a in page[i+1:] and i+1 < len(page):
                a_pos = page.index(a)
                page[i], page[a_pos] = page[a_pos], page[i]
                return
    
        
invalids = []
        
for page in pages:
    page = page.split(',')
    valid = True
    for i in range(len(page)):
        if not check_valid(page, i):
            valid = False
            break
    if not valid:
        invalids.append(page)
        
        

def fix_ordering(v):
    valid = False
    while not valid:
        valid = True
        for i in range(len(v)):
            if not check_valid(v, i):
                valid = False
                swap_invalid(v, i)
                break    
    return v
        
total = 0
for v in invalids:
    v = fix_ordering(v)
    total += int(v[floor(len(v)/2)])
print(total)  
                    