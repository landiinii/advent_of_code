with open('input.txt', 'r') as file:
    input = file.read()
    
input = input.split('\n')

def try_all(sol, params):
    if params[0] > sol:
        return False
    elif len(params) == 1:
        return params[0] == sol
    else:
        plus_params = [params[0] + params[1]] + params[2:]
        mult_params = [params[0] * params[1]] + params[2:]
        cat_params = [int(str(params[0]) + str(params[1]))] + params[2:]
        
        return try_all(sol, plus_params) or try_all(sol, mult_params) or try_all(sol, cat_params)
    

total = 0
for equ in input:
    equ = equ.split(': ')
    if try_all(int(equ[0]), [int(x) for x in equ[1].split(' ')]):
        total += int(equ[0])
        
print(total)
        
        
        