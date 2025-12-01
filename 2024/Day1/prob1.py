from collections import Counter
# import numpy as np

with open('input1.txt', 'r') as file:
    input = file.read()
    
input = input.split('\n')
left = [int(line.split('   ')[0]) for line in input] 
right = [int(line.split('   ')[1]) for line in input]
print(left[:5])
print(right[:5])

left.sort()
right.sort()

# left_array = np.array(left)
# right_array = np.array(right)

# Subtract right array from left array
# result = left_array - right_array
# result = np.abs(result)

# print(result.sum())

# map right list

counts = Counter(right)
print(counts[52600])

sim_score = 0

for row in left:
    if row in counts:
        sim_score += row * counts[row]
        
print(sim_score)