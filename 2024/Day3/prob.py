import re


with open('input.txt', 'r') as file:
    input = file.read()

dos = input.split('do()')

matches = []
for do in dos:
    doit = do.split('don\'t()')
    matches += re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', doit[0])


total = 0
for match in matches:
    nums = match[4:-1].split(',')
    total += int(nums[0]) * int(nums[1])

print(total)