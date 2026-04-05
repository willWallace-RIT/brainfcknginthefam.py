import sys

# Mapping surnames to brainfuck ops
ops = {
    "Smith": ">",
    "Nguyen": "<",
    "Garcia": "+",
    "Kim": "-",
    "Patel": ".",
    "Khan": ",",
    "Ivanov": "[",
    "Silva": "]"
}

def parse(code):
    return [ops[word] for word in code.split() if word in ops]

def run(code):
    code = parse(code)
    tape = [0] * 30000
    ptr = 0
    pc = 0
    loop_stack = []

    while pc < len(code):
        cmd = code[pc]

        if cmd == ">":
            ptr += 1
        elif cmd == "<":
            ptr -= 1
        elif cmd == "+":
            tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == "-":
            tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == ".":
            sys.stdout.write(chr(tape[ptr]))
        elif cmd == ",":
            tape[ptr] = ord(sys.stdin.read(1))
        elif cmd == "[":
            if tape[ptr] == 0:
                depth = 1
                while depth:
                    pc += 1
                    if code[pc] == "[":
                        depth += 1
                    elif code[pc] == "]":
                        depth -= 1
            else:
                loop_stack.append(pc)
        elif cmd == "]":
            if tape[ptr] != 0:
                pc = loop_stack[-1]
            else:
                loop_stack.pop()

        pc += 1

run("""
Garcia Garcia Garcia Garcia Garcia Garcia Garcia Garcia Garcia Garcia
Ivanov
Smith Garcia Garcia Garcia Garcia Garcia Garcia Garcia
Nguyen Kim
Silva
Smith Garcia Garcia Garcia Garcia Garcia Patel
""")
