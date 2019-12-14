f = open('input.txt').readlines()
f = [line.strip().split(')') for line in f]

nodes = {}
for line in f:
    nodes[line[0]] = set()
    nodes[line[1]] = set()

for line in f:
    nodes[line[0]].add(line[1])
    
def predecessors(n):
    global nodes
    if n == 'COM':
        return set([n])
    for p in nodes:
        if n in nodes[p]:
            return set([n]) | predecessors(p)

p_YOU = predecessors('YOU')
p_SAN = predecessors('SAN')

result = (p_YOU | p_SAN) - (p_YOU & p_SAN)

print(len(result)-2)
