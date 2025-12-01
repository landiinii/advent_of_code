with open('input.txt', 'r') as file:
    input = file.read()
    
    
input = input.split('\n')
input = [list(x) for x in input]

width = len(input[0])
height = len(input)
    
# Part 1
# total = 0
# for r in range(len(input)):
#     for l in range(len(input[r])):
#         let = input[r][l]
#         if let == 'X':
#             for rmod in range(-1, 2):
#                 for lmod in range(-1, 2):
#                     if rmod == 0 and lmod == 0:
#                         continue
#                     if r + rmod >= 0 and r + rmod < height and l + lmod >= 0 and l + lmod < width and input[r+rmod][l+lmod] == 'M':
#                         if r + (rmod * 2) >= 0 and r + (rmod * 2) < height and l + (lmod * 2) >= 0 and l + (lmod * 2) < width and input[r+(rmod * 2)][l+(lmod * 2)] == 'A':
#                             if r + (rmod * 3) >= 0 and r + (rmod * 3) < height and l + (lmod * 3) >= 0 and l + (lmod * 3) < width and input[r+(rmod * 3)][l+(lmod * 3)] == 'S':
#                                 total += 1
# print(total)


total = 0
for r in range(len(input)):
    for l in range(len(input[r])):
        let = input[r][l]
        if let == 'A':
            if r + 1 < height and r-1 >= 0 and l + 1 < width and l-1 >= 0:
                if (input[r-1][l-1] == 'M' and input[r+1][l+1] == 'S') or (input[r-1][l-1] == 'S' and input[r+1][l+1] == 'M'):
                    if (input[r-1][l+1] == 'M' and input[r+1][l-1] == 'S') or (input[r-1][l+1] == 'S' and input[r+1][l-1] == 'M'):
                        total += 1
print(total)
        