f = open('input.txt').readlines()

a = [(i[0],int(i[1:])) for i in f[0].split(',')]
b = [(i[0],int(i[1:])) for i in f[1].split(',')]

def travel(wire, layout, value):
    x = 0
    y = 0

    for i in wire:
        if i[0] == 'U':
            for j in range(i[1]):
                y += 1
                layout[(x,y)] = layout.setdefault((x,y),set()).union(set([value]))
        elif i[0] == 'D':
            for j in range(i[1]):
                y -= 1
                layout[(x,y)] = layout.setdefault((x,y),set()).union(set([value]))
        elif i[0] == 'L':
            for j in range(i[1]):
                x -= 1
                layout[(x,y)] = layout.setdefault((x,y),set()).union(set([value]))
        elif i[0] == 'R':
            for j in range(i[1]):
                x += 1
                layout[(x,y)] = layout.setdefault((x,y),set()).union(set([value]))

layout = {}
travel(a, layout, 0)
travel(b, layout, 1)
  
x = 2**30
y = 2**30

distance = x + y

for i in layout:
    if layout[i] == set([0,1]):
        d = abs(i[0]) + abs(i[1])
        if d < distance:
            distance = d

print(distance)
