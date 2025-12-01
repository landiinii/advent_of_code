with open('input.txt', 'r') as file:
    input = file.read()
    
new_input = []
for pos in range(len(input)):
    if pos % 2 == 0: # Character
        char_arr = [str(int(pos / 2))] * int(input[pos])
        new_input += char_arr
    else: # White space
        char_arr = ['.'] * int(input[pos])
        new_input += char_arr

#print(''.join(new_input))

def get_next_ws(input, ws, needed_leng):
    leng = 0
    while ws < len(input):
        if input[ws] == '.':
            leng += 1
            if leng == needed_leng:
                return ws + 1 - needed_leng
        else:
            leng = 0
        ws += 1
    return ws

running_ws = 0
pos = len(new_input) - 1
while pos >= 0:
    if new_input[pos] != '.':
        needed_char = new_input[pos]
        needed_leng = 1
        pos = pos - 1
        while new_input[pos] == needed_char:
            needed_leng += 1
            pos -= 1
        pos += 1
        next_ws = get_next_ws(new_input, running_ws, needed_leng)
        if next_ws < pos:
            new_input[next_ws:next_ws+needed_leng] = new_input[pos:pos+needed_leng]
            new_input[pos:pos+needed_leng] = ['.'] * needed_leng
            #print(''.join(new_input))
    pos -= 1
            
            
total = 0
for pos in range(len(new_input)):
    if new_input[pos] != '.':
        total += int(new_input[pos]) * pos
print(total)
