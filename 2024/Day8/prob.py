with open('input.txt', 'r') as file:
    input = file.read()
    
input = input.split('\n')
input = [list(x) for x in input]


characters = {}
for py in range(len(input)):
    for px in range(len(input[py])):
        char = input[py][px]
        if char != '.':
            if char in characters:
                characters[char].append((py, px))
            else:
                characters[char] = [(py, px)]
                
 
                

                
antinodes = set()
for char in characters:
    for pos in range(len(characters[char])):
        for pos2 in range(pos+1, len(characters[char])):
            ant1 = characters[char][pos]
            ant2 = characters[char][pos2]
            antinodes.add(ant1)
            antinodes.add(ant2)
            disty = abs(ant1[0] - ant2[0])
            distx = abs(ant1[1] - ant2[1])
            # get anti nodes y
            if ant1[0] <= ant2[0]: # 1 is up from 2
                aniy1 = ant1[0] - disty
                aniy2 = ant2[0] + disty
                # get anti nodes x
                if ant1[1] <= ant2[1]:  # 1 is up from 2 and left of 2
                    anix1 = ant1[1] - distx
                    anix2 = ant2[1] + distx
                    while aniy1 >= 0 and anix1 >=0: # keep going up and left
                        antinodes.add((aniy1, anix1))
                        aniy1 -= disty
                        anix1 -= distx
                    while aniy2 < len(input) and anix2 < len(input[0]): # keep going down and right
                        antinodes.add((aniy2, anix2))
                        aniy2 += disty
                        anix2 += distx
                else:  # 1 is up from 2 and right of 2
                    anix1 = ant1[1] + distx
                    anix2 = ant2[1] - distx
                    while aniy1 >= 0 and anix1 < len(input[0]): # keep going up and right
                        antinodes.add((aniy1, anix1))
                        aniy1 -= disty
                        anix1 += distx
                    while aniy2 < len(input) and anix2 >= 0: # keep going down and left
                        antinodes.add((aniy2, anix2))
                        aniy2 += disty
                        anix2 -= distx
            else:  # 1 is down from 2
                aniy1 = ant1[0] + disty
                aniy2 = ant2[0] - disty
                # get anti nodes x
                if ant1[1] <= ant2[1]:  # 1 is down from 2 and left of 2
                    anix1 = ant1[1] - distx
                    anix2 = ant2[1] + distx
                    while aniy1 < len(input) and anix1 >= 0: # keep going down and left
                        antinodes.add((aniy1, anix1))
                        aniy1 += disty
                        anix1 -= distx
                    while aniy2 >= 0 and anix2 < len(input[0]): # keep going up and right
                        antinodes.add((aniy2, anix2))
                        aniy2 -= disty
                        anix2 += distx
                else:   # 1 is down from 2 and right of 2
                    anix1 = ant1[1] + distx
                    anix2 = ant2[1] - distx
                    while aniy1 < len(input) and anix1 < len(input[0]): # keep going down and right
                        antinodes.add((aniy1, anix1))
                        aniy1 += disty
                        anix1 += distx
                    while aniy2 >= 0 and anix2 >= 0: # keep going up and left
                        antinodes.add((aniy2, anix2))
                        aniy2 -= disty
                        anix2 -= distx
                
    
# print(antinodes)
print(len(antinodes))    
