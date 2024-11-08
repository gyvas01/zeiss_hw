import re

HEAVYLIFTER_VERSION = 'v1'

lines = open('instruction_set_01.txt', 'r').read().split('\n')

bottom_line = [line.strip() for line in lines].index('bottom')
num_stacks = int(lines[bottom_line - 1].strip()[-1])
stacks = [[] for _ in range(num_stacks)]

def process_line(line, len):
    for i in range(len):
        if line[4 * i + 1] != ' ':
            stacks[i].append(line[4 * i + 1])

for line in lines[:bottom_line - 1][::-1]:
    process_line(line, num_stacks)

for line in lines[bottom_line + 2:]:
    m = re.search(r"move (\d+) from (\d+) to (\d+)", line)
    move_cnt, fr, to = map(int, m.group(1, 2, 3))
    if HEAVYLIFTER_VERSION == 'v1':
        for i in range(move_cnt):
            stacks[to - 1].append(stacks[fr - 1].pop())
    elif HEAVYLIFTER_VERSION == 'v2':
        stacks[to - 1].extend(stacks[fr - 1][0 - move_cnt:])
        del stacks[fr - 1][0 - move_cnt:]

# print('Final state of the stacks:')
# print(*stacks, sep='\n')
# print()
# print(f'Top elements of each stack: {[s[-1] if len(s) > 0 else "<empty stack>" for s in stacks]}')
print(''.join([s[-1] for s in stacks]))