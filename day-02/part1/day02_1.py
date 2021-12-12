with open('../input.txt') as f:
    lines = f.readlines()

instructions = []
horizontal = 0
vertical = 0

for line in lines:
    instruction = line.split(" ")
    instruction[1] = int(instruction[1])
    instructions.append(instruction)

print(instructions[:10])

for instruction in instructions:
    if instruction[0] == 'forward':
        horizontal += instruction[1]
    elif instruction[0] == 'up':
        vertical -= instruction[1]
    elif instruction[0] == 'down':
        vertical += instruction[1]

print(f'''
Vertical: {vertical}
Horizontal: {horizontal}
Answer: {vertical * horizontal}
''')