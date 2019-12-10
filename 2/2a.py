f = open('input.txt').read()

tape = [int(i) for i in f.split(',')]
tape[1] = 12
tape[2] = 2

for i in range(0,len(tape),4):
    if tape[i] == 1:
        tape[tape[i+3]] = tape[tape[i+1]]+tape[tape[i+2]]
    elif tape[i] == 2:
        tape[tape[i+3]] = tape[tape[i+1]]*tape[tape[i+2]]
    elif tape[i] == 99:
        print(tape)
        exit()
