f = open('input.txt').read()

for n in range(100):
    for v in range(100):
        tape = [int(i) for i in f.split(',')]
        tape[1] = n
        tape[2] = v
        for i in range(0,len(tape),4):
            if tape[i] == 1:
                tape[tape[i+3]] = tape[tape[i+1]]+tape[tape[i+2]]
            elif tape[i] == 2:
                tape[tape[i+3]] = tape[tape[i+1]]*tape[tape[i+2]]
            elif tape[i] == 99:
                if tape[0] == 19690720:
                    print(n,v,100*n+v)
                    exit()
