f = open('input.txt').readlines()

a = [(i[0],int(i[1:])) for i in f[0].split(',')]
b = [(i[0],int(i[1:])) for i in f[1].split(',')]

x = 0
y = 0

layout = {}

for i in a:
    if i[0] == 'U':
        for j in range(i[1]):
            y += 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([0]))
    elif i[0] == 'D':
        for j in range(i[1]):
            y -= 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([0]))
    elif i[0] == 'L':
        for j in range(i[1]):
            x -= 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([0]))
    elif i[0] == 'R':
        for j in range(i[1]):
            x += 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([0]))
    
x = 0
y = 0
    
for i in b:
    if i[0] == 'U':
        for j in range(i[1]):
            y += 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([1]))
    elif i[0] == 'D':
        for j in range(i[1]):
            y -= 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([1]))
    elif i[0] == 'L':
        for j in range(i[1]):
            x -= 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([1]))
    elif i[0] == 'R':
        for j in range(i[1]):
            x += 1
            layout[(x,y)] = layout.setdefault((x,y),set()).union(set([1]))
   
x = 100000000000000000000
y = 100000000000000000000

distance = x + y

for i in layout:
    #print(i, layout[i])
    #continue
    if layout[i] == set([0,1]):
        print(i, layout[i],abs(i[0]) + abs(i[1]))
        d = abs(i[0]) + abs(i[1])
        if d < distance:
            distance = d
print(distance)
