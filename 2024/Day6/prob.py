


with open('input.txt', 'r') as file:
    input = file.read()
    
    
input = input.split('\n')
input = [list(line) for line in input]

for i in range(len(input)):
    if '^' in input[i]:
        sy = i
        sx = input[i].index('^')

directions = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}

def check_bounds(y, x, board_height, board_width):
    if y < 0: # escaped up
        return True
    if y >= board_height: # escaped down
        return True
    if x < 0: # escaped left
        return True
    if x >= board_width: # escaped right
        return True
    return False


def run1(y, x, board):
    dir = 0
    visited = set()
    while True:
        visited.add((y, x))
        dy, dx = directions[dir]
        if check_bounds(y+dy, x+dx, len(board), len(board[0])):
            break
        while board[y+dy][x+dx] == '#':
            dir = (dir + 1) % 4
            dy, dx = directions[dir]
        y += dy
        x += dx
        if check_bounds(y, x, len(board), len(board[0])):
            break
    return len(visited)

print('part1:', run1(sy, sx, input))

def run2(y, x, board):
    dir = 0
    visited = set()
    while True:
        new = (y, x, dir)
        if new in visited:
            return True
        visited.add(new)
        dy, dx = directions[dir]
        if check_bounds(y+dy, x+dx, len(board), len(board[0])):
            break
        while board[y+dy][x+dx] == '#':
            dir = (dir + 1) % 4
            dy, dx = directions[dir]
        y += dy  
        x += dx
        if check_bounds(y, x, len(board), len(board[0])):
            break
    return False





totals = 0
for by in range(len(input)):
    for bx in range(len(input[by])):
        if input[by][bx] == '.':
            input[by][bx] = '#'
            if run2(sy, sx, input):
                totals += 1
            input[by][bx] = '.'
print('part2:', totals)
