f = open('input.txt').readlines()

a = [(i[0],int(i[1:])) for i in f[0].split(',')]
b = [(i[0],int(i[1:])) for i in f[1].split(',')]

def travel(wire, layout, value, distance):
    x = 0
    y = 0
    counter = 0
    for i in wire:    
        if i[0] == 'U':
            for j in range(i[1]):
                y += 1
                layout[(x,y)] = layout.setdefault((x,y),set()).union(set([value]))
                counter += 1
                distance[(x,y)] = counter
        elif i[0] == 'D':
            for j in range(i[1]):
                y -= 1
                layout[(x,y)] = layout.setdefault((x,y),set()).union(set([value]))
                counter += 1
                distance[(x,y)] = counter
        elif i[0] == 'L':
            for j in range(i[1]):
                x -= 1
                layout[(x,y)] = layout.setdefault((x,y),set()).union(set([value]))
                counter += 1
                distance[(x,y)] = counter
        elif i[0] == 'R':
            for j in range(i[1]):
                x += 1
                layout[(x,y)] = layout.setdefault((x,y),set()).union(set([value]))
                counter += 1
                distance[(x,y)] = counter

layout = {}
distance_a = {}
distance_b = {}
counter_b = 0

travel(a, layout, 0, distance_a)
travel(b, layout, 1, distance_b)
    
  
# retrace a and b
minimum = 2**30
for i in [x for x in layout if layout[x] == set([0,1])]:
    m = distance_a[i] + distance_b[i]
    if m < minimum:
        minimum = m

print(minimum)