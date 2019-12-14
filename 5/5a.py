f = open('input.txt').read()

input = 1
tape = [int(i) for i in f.split(',')]

def execute(opcode, parameters, parameter_modes):
    global input, tape
    if opcode == 1:
        a = 0
        b = 0
        r = 0
        if parameter_modes[0] == '0':
            a = tape[parameters[0]]
        else:
            a = parameters[0]
        if parameter_modes[1] == '0':
            b = tape[parameters[1]]
        else:
            b = parameters[1]
        r = a + b
        tape[parameters[2]] = r
    elif opcode == 2:
        a = 0
        b = 0
        r = 0
        if parameter_modes[0] == '0':
            a = tape[parameters[0]]
        else:
            a = parameters[0]
        if parameter_modes[1] == '0':
            b = tape[parameters[1]]
        else:
            b = parameters[1]
        r = a * b
        tape[parameters[2]] = r
    elif opcode == 3:
        tape[parameters[0]] = input
    elif opcode == 4:
        if parameter_modes[0] == '0':
            print(tape[parameters[0]])
        else:
            print(parameters[0])
    elif opcode == 99:
        exit()

pc = 0
parameter_number = {1:3,2:3,3:1,4:1,99:0}


while True:
    current = str(tape[pc]).zfill(5)    
    opcode = int(current[-2:])
    parameter_modes = current[:-2][::-1]
    print('Debug decode', tape[pc:pc+4])
    parameters = tape[pc+1:pc+1+parameter_number[opcode]]
    print('Debug opcode', opcode, parameters, parameter_modes)
    execute(opcode, parameters, parameter_modes)
    pc += parameter_number[opcode] + 1
