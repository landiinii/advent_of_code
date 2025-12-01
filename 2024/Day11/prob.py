from functools import lru_cache 

with open('input.txt', 'r') as file:
    input = file.read()

input = input.split(' ')



    
@lru_cache(maxsize=None)
def change(stone):
    if stone == '0':
        return '1', False
    elif len(stone) % 2 == 0:
        mid = int(len(stone)/2)
        return [str(int(stone[:mid])), str(int(stone[mid:]))], True
    else:
        return str(int(stone) * 2024), False
        
        
def blink(lineos):
    i = len(lineos) - 1
    while i >= 0:
        resp, two = change(lineos[i])
        if two:
            lineos[i:i+1] = resp
        else:
            lineos[i] = resp
        i -= 1
    return lineos
        
            
for revs in range(75):
    input = blink(input)
    print(revs, len(input))
print(len(input))
