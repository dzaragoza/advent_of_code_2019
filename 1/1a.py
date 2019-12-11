f = open('input.txt').readlines()

total = sum([int(line)//3-2 for line in f])
print(total)
