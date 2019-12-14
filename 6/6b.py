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
        return set(n)
    for p in nodes:
        if n in nodes[p]:
            return set(n).add(predecessors(p))

san_you = predecessors('YOU')).difference(predecessors('SAN')
you_san = predecessors('SAN')).difference(predecessors('YOU')

print(len(san_you | you_san)-2)

#361
