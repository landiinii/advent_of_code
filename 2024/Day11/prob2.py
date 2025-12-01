from functools import lru_cache 


with open('input.txt', 'r') as file:
    input = file.read()

input = input.split(' ')

input_map = {}
for i in range(len(input)):
    input_map[int(input[i])] = 1


def blink(stones):
    new_stones = {}
    for ston in stones:
        count = stones[ston]
        
        if ston == 0:
            if 1 in new_stones:
                new_stones[1] += count
            else:
                new_stones[1] = count
            
        elif (len(str(ston))) % 2 == 0:
            mid = len(str(ston))//2
            left = int(str(ston)[:mid])
            right = int(str(ston)[mid:])
            if left in new_stones:
                new_stones[left] += count
            else:
                new_stones[left] = count
            if right in new_stones:
                new_stones[right] += count
            else:
                new_stones[right] = count
        else:
            big = ston * 2024
            if big in new_stones:
                new_stones[big] += count
            else:
                new_stones[big] = count
            
    return new_stones
    
    
    
        
            
for revs in range(75):
    input_map = blink(input_map)
    print(revs, sum(input_map.values()))
