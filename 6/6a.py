f = open('input.txt').readlines()
f = [line.strip().split(')') for line in f]

def travel(n, nodes):
    r = 0
    for n1 in nodes[n]:
        r += 1 + travel(n1, nodes)
    return r

nodes = {}
for line in f:
    nodes[line[1]] = set()
nodes['COM'] = set()

for line in f:
    nodes[line[0]].add(line[1])

total = sum([travel(n, nodes) for n in nodes])
print(total)
