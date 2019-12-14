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
        return [n]
    for p in nodes:
        if n in nodes[p]:
            return [n] + predecessors(p)

san_you = set(predecessors('YOU')).difference(predecessors('SAN'))
you_san = set(predecessors('SAN')).difference(predecessors('YOU'))

print(len(san_you | you_san)-2)

#361
