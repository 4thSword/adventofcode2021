with open('day-01/input_1.txt') as f:
    lines = f.readlines()

measures = []
sum_measures = []

for line in lines:
    measures.append(int(line))


larger = 0
smaller = 0
equals = 0

for i in range(len(measures)-2):
    sum_measures.append(measures[i] + measures[i+1] + measures[i+2])


for i in range(1, len(sum_measures)):
    if sum_measures[i] > sum_measures[i-1]:
        larger += 1
    elif sum_measures[i] < sum_measures[i-1]:
        smaller += 1
    else:
        equals +=1

print(f'''
Larger = {larger}
Smaller = {smaller}
Equals = {equals}
''')