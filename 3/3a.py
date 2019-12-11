f = open('input.txt').readlines()

a = [(i[0],int(i[1:])) for i in f[0].split(',')]
b = [(i[0],int(i[1:])) for i in f[1].split(',')]

def travel(wire, layout):
    x = 0
    y = 0

    for i in wire:
        if i[0] == 'U':
            for j in range(i[1]):
                y += 1
                layout.add((x,y))
        elif i[0] == 'D':
            for j in range(i[1]):
                y -= 1
                layout.add((x,y))
        elif i[0] == 'L':
            for j in range(i[1]):
                x -= 1
                layout.add((x,y))
        elif i[0] == 'R':
            for j in range(i[1]):
                x += 1
                layout.add((x,y))

layout_a = set()
layout_b = set()
travel(a, layout_a)
travel(b, layout_b)

interception = layout_a & layout_b

distance = min([abs(i[0]) + abs(i[1]) for i in interception])

print(distance)
 
