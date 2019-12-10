f = open('input.txt').readlines()

accumulator = 0
for line in f:
    current = int(line)
    while current//3-2 > 0:
        accumulator += current//3-2
        current = current//3-2
    

print(accumulator)
