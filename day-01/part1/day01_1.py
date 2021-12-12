# measures
with open('day-01/input_1.txt') as f:
    lines = f.readlines()

measures = []

for line in lines:
    measures.append(int(line))

print(measures[:10])

larger = 0
smaller = 0
equals = 0

for i in range(1, len(measures)):
    if measures[i] > measures[i-1]:
        larger += 1
    elif measures[i] < measures[i-1]:
        smaller += 1
    else:
        equals +=1

print(f'''
Larger = {larger}
Smaller = {smaller}
Equals = {equals}
''')