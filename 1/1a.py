f = open('input.txt').readlines()

accumulator = 0
for line in f:
    accumulator += int(line)//3-2

print(accumulator)
