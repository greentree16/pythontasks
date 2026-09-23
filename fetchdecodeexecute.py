# This is a sample Python script

memory = ["LOAD 4", "ADD 5", "STORE 6", "HALT", 10,7,8]

pc = 0 #program counter
mar = 0 #memeory address register
mdr = "" #memory data register
cir = "" #current instruction register
accumulator = 0 #temporary storage during calculations


while True:
    #FETCH
    mar = pc
    mdr = memory[mar]
    pc = pc + 1


    #DECODE
    parts = mdr.split(" ")
    operator = parts[0]
    operand = int(parts[1]) if len(parts) > 1 else ""

    print("the current operand and operator are:", operator, operand)


    #EXECUTE
    if operator == "LOAD":
        accumulator = memory[operand]

    if operator == "ADD":
        accumulator = accumulator + memory[operand]

    if operator == "STORE":
        memory[operand] = accumulator

    if operator == "HALT":
        break

print(memory)




