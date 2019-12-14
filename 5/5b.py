f = open('input.txt').read()

input = 5
tape = [int(i) for i in f.split(',')]


def execute(opcode, parameters, parameter_modes, pc):
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
        pc += parameter_number[opcode] + 1
    
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
        pc += parameter_number[opcode] + 1
    
    elif opcode == 3:
        tape[parameters[0]] = input
        pc += parameter_number[opcode] + 1
    
    elif opcode == 4:
        if parameter_modes[0] == '0':
            print(tape[parameters[0]])
        else:
            print(parameters[0])
        pc += parameter_number[opcode] + 1
    
    elif opcode == 5:
        c = 0
        if parameter_modes[0] == '0':
            c = tape[parameters[0]]
        else:
            c = parameters[0]
        if int(c) != 0:
            if parameter_modes[1] == '0':
                pc = tape[parameters[1]]
            else:
                pc = parameters[1]
        else:
            pc += parameter_number[opcode] + 1
    
    elif opcode == 6:
        c = 0
        if parameter_modes[0] == '0':
            c = tape[parameters[0]]
        else:
            c = parameters[0]
        if int(c) == 0:
            if parameter_modes[1] == '0':
                pc = tape[parameters[1]]
            else:
                pc = parameters[1]
        else:
            pc += parameter_number[opcode] + 1
    
    elif opcode == 7:
        a = 0
        if parameter_modes[0] == '0':
            a = tape[parameters[0]]
        else:
            a = parameters[0]
        if parameter_modes[1] == '0':
            b = tape[parameters[1]]
        else:
            b = parameters[1]            
        if a < b:
            r = 1
        else:
            r = 0
        if parameter_modes[2] == '0':
            tape[parameters[2]] = r
        else:
            parameters[2] = r
        pc += parameter_number[opcode] + 1
    
    elif opcode == 8:
        a = 0
        if parameter_modes[0] == '0':
            a = tape[parameters[0]]
        else:
            a = parameters[0]
        if parameter_modes[1] == '0':
            b = tape[parameters[1]]
        else:
            b = parameters[1]            
        if a == b:
            r = 1
        else:
            r = 0
        if parameter_modes[2] == '0':
            tape[parameters[2]] = r
        else:
            parameters[2] = r
        pc += parameter_number[opcode] + 1
    
    elif opcode == 99:
        exit()
    
    return pc

pc = 0
parameter_number = {1:3,2:3,3:1,4:1,5:2,6:2,7:3,8:3,99:0}


while True:
    current = str(tape[pc]).zfill(5)    
    opcode = int(current[-2:])
    parameter_modes = current[:-2][::-1]
    #print('Debug decode', tape[pc:pc+4])
    parameters = tape[pc+1:pc+1+parameter_number[opcode]]
    #print('Debug opcode', opcode, parameters, parameter_modes)
    pc = execute(opcode, parameters, parameter_modes,pc)
    
