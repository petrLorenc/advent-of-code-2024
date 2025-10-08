
with open("input_2.txt") as f:
    input_data = f.readlines()

for line in input_data:
    if "Register A: " in line:
        A = int(line.replace("Register A: ", ""). strip())
    if "Register B: " in line:
        B_init = int(line.replace("Register B: ", ""). strip())
    if "Register C: " in line:
        C_init = int(line.replace("Register C: ", ""). strip())
    if "Program: " in line:
        program = [int(x) for x in line.replace("Program: ", "").strip().split(",")]
to_find = ",".join([str(x) for x in program])



def get_literal(operand):
    return operand
import tqdm

number = len(program)
suffix = 1
revealed_number = 0
out = []

A_init = sum(7 * 8**i for i in range(len(program) - 1)) + 1
while ",".join(out) != ",".join([str(x) for x in program]):
    out = []
    A = A_init
    B = 0
    C = 0
    idx_combo = 0
    idx_literal = 1

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

    # while idx_combo < len(program) and to_find.startswith(out.strip(",")):
    while idx_combo < len(program):
        opcode = program[idx_combo]
        operand = program[idx_literal]
        # print(opcode, operand)

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
            out.append(str(get_combo(operand) % 8))
        if opcode == 6:
            B = A // 2 ** get_combo(operand)
        if opcode == 7:
            C = A // 2 ** get_combo(operand)

        idx_combo += 2
        idx_literal += 2
    # print(A_init, bin(A_init), ",".join(out))
    add = 0
    # out = list(str(int("".join([str(x) for x in out]))))
    for i in range(len(out) - 1, -1, -1):
        if out[i] != program[i]:
            add = 8**i
            A_init += add
            break

print(revealed_number)
