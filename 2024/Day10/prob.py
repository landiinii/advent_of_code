with open('input.txt', 'r') as file:
    input = file.read()

input = input.split('\n')
input = [list(row) for row in input]
    
directions = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1)
}

def chase_trails(map, heady, headx):
    sub_path = 0
    for dir in directions:
        posy = heady + directions[dir][0]
        posx = headx + directions[dir][1]
        if posy < 0 or posy >= len(map) or posx < 0 or posx >= len(map[0]):
            continue
        elif map[posy][posx] == str(int(map[heady][headx]) + 1):
            if map[posy][posx] == '9':
                sub_path += 1
            else:
                sub_path += chase_trails(map, posy, posx)
    return sub_path
        
        
            
total = 0
for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] == '0':
            sub_total = set()
            nines = chase_trails(input, y, x)
            total += nines
print(total)
