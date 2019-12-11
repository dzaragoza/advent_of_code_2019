f = open('input.txt').readlines()

a = [(i[0],int(i[1:])) for i in f[0].split(',')]
b = [(i[0],int(i[1:])) for i in f[1].split(',')]

def travel(wire, layout, distance):
    x = 0
    y = 0
    counter = 0
    
    for i in wire:    
        if i[0] == 'U':
            for j in range(i[1]):
                y += 1
                layout |= set([(x,y)])
                counter += 1
                distance[(x,y)] = counter
        elif i[0] == 'D':
            for j in range(i[1]):
                y -= 1
                layout |= set([(x,y)])
                counter += 1
                distance[(x,y)] = counter
        elif i[0] == 'L':
            for j in range(i[1]):
                x -= 1
                layout |= set([(x,y)])
                counter += 1
                distance[(x,y)] = counter
        elif i[0] == 'R':
            for j in range(i[1]):
                x += 1
                layout |= set([(x,y)])
                counter += 1
                distance[(x,y)] = counter

layout_a = set()
layout_b = set()
distance_a = {}
distance_b = {}

travel(a, layout_a, distance_a)
travel(b, layout_b, distance_b)
    
interception = layout_a & layout_b

distance = min([distance_a[i] + distance_b[i] for i in interception])
print(distance)
