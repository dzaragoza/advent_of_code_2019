f = open('input.txt').readlines()
f = [line.strip().split(')') for line in f]


def travel(n, nodes):
    r = 0
    for n1 in nodes[n]:
        #print(n1)
        r += 1 + travel(n1, nodes)
    return r

nodes = {}
for line in f:
    nodes[line[0]] = set()
    nodes[line[1]] = set()

for line in f:
    nodes[line[0]].add(line[1])

total = 0
for n in nodes:
    total += travel(n, nodes)
    
print(total)
    
