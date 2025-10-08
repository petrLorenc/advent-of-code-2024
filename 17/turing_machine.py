with open("input_2.txt") as f:
    input_data = f.readlines()

for line in input_data:
    if "Register A: " in line:
        A = int(line.replace("Register A: ", ""). strip())
    if "Register B: " in line:
        B = int(line.replace("Register B: ", ""). strip())
    if "Register C: " in line:
        C = int(line.replace("Register C: ", ""). strip())
    if "Program: " in line:
        program = [int(x) for x in line.replace("Program: ", "").strip().split(",")]
print(A, B, C, program)

idx_combo = 0
idx_literal = 1

out = ""

def get_combo(operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    else:
        raise Exception("Invalid combo")

def get_literal(operand):
    return operand

while idx_combo < len(program):
    opcode = program[idx_combo]
    operand = program[idx_literal]
    print(A, B, C, out)

    if opcode == 0:
        A = A // 2 ** get_combo(operand)
    if opcode == 1:
        # xor
        B = B ^ get_literal(operand)
    if opcode == 2:
        # modulo
        B = get_combo(operand) % 8
    if opcode == 3:
        if A == 0:
            pass
        else:
            idx_combo = get_literal(operand) - 2
            idx_literal = get_literal(operand) - 1
    if opcode == 4:
        # xor on B
        B = B ^ C
    if opcode == 5:
        out += str(get_combo(operand) % 8) + ","
    if opcode == 6:
        B = A // 2 ** get_combo(operand)
    if opcode == 7:
        C = A // 2 ** get_combo(operand)

    idx_combo += 2
    idx_literal += 2

print(out)