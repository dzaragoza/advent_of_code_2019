f = open('input.txt').readlines()

a = [(i[0],int(i[1:])) for i in f[0].split(',')]
b = [(i[0],int(i[1:])) for i in f[1].split(',')]

x = 0
y = 0

layout = {}
distance_a = {}
distance_b = {}

counter_a = 0
counter_b = 0
for i in a:    
    if i[0] == 'U':
        for j in range(i[1]):
            y += 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([0]))
            counter_a += 1
            distance_a[(x,y)] = counter_a
    elif i[0] == 'D':
        for j in range(i[1]):
            y -= 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([0]))
            counter_a += 1
            distance_a[(x,y)] = counter_a
    elif i[0] == 'L':
        for j in range(i[1]):
            x -= 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([0]))
            counter_a += 1
            distance_a[(x,y)] = counter_a
    elif i[0] == 'R':
        for j in range(i[1]):
            x += 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([0]))
            counter_a += 1
            distance_a[(x,y)] = counter_a
    
x = 0
y = 0
    
for i in b:
    if i[0] == 'U':
        for j in range(i[1]):
            y += 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([1]))
            counter_b += 1
            distance_b[(x,y)] = counter_b
    elif i[0] == 'D':
        for j in range(i[1]):
            y -= 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([1]))
            counter_b += 1
            distance_b[(x,y)] = counter_b
    elif i[0] == 'L':
        for j in range(i[1]):
            x -= 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([1]))
            counter_b += 1
            distance_b[(x,y)] = counter_b
    elif i[0] == 'R':
        for j in range(i[1]):
            x += 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([1]))
            counter_b += 1
            distance_b[(x,y)] = counter_b
   
# retrace a and b
minimum = 100000000000000
for i in [x for x in layout if layout[x] == set([0,1])]:
    m = distance_a[i] + distance_b[i]
    if m < minimum:
        minimum = m

print(minimum)
