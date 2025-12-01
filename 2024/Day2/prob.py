with open('input.txt', 'r') as file:
    input = file.read()
    
input = input.split('\n')
safe_count = 0

def check_report(report, skipped):
    direction = None
    prev_level = None
    safe = True
    for level in report:
        level = int(level)
        if prev_level is None:
            prev_level = level
            continue
        diff = level - prev_level
        if abs(diff) < 1 or abs(diff) > 3:
            if not skipped:
                skipped = True
                continue
            else:
                safe = False
                break
        if diff > 0:
            if direction is None:
                direction = 'up'
                prev_level = level
                continue
            elif direction == 'up':
                prev_level = level
                continue
            else:
                if not skipped:
                    skipped = True
                    continue
                else:
                    safe = False
                    break
        elif diff < 0:
            if direction is None:
                direction = 'down'
                prev_level = level
                continue
            elif direction == 'down':
                prev_level = level
                continue
            else:
                if not skipped:
                    skipped = True
                    continue
                else:
                    safe = False
                    break
    return safe
    
    

for report in input:
    report = report.split(' ')
    for i in range(len(report)):
        temp = report[:i]
        if i + 1 < len(report):
            temp = temp + report[i + 1:]
        safe = check_report(temp, True)
        if safe:
            break
        
    if safe and not (check_report(report, False) or check_report(report[1:], True)):
        print(report)
    if safe:
        safe_count += 1

print(safe_count)
    
    