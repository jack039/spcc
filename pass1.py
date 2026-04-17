OPTAB = {
    "START": "AD",
    "END": "AD",
    "LTORG": "AD",
    "DS": "DL",
    "DC": "DL",
    "MOVER": "IS",
    "MOVEM": "IS",
    "ADD": "IS",
    "SUB": "IS",
    "MULT": "IS",
    "STOP": "IS"
}

REG = {
    "AREG": 1,
    "BREG": 2,
    "CREG": 3,
    "DREG": 4
}

program = [
    "START 100",
    "MOVER AREG, ONE",
    "ADD BREG, TWO",
    "ONE DC 5",
    "TWO DS 1",
    "END"
]

SYMTAB = {}
LC = 0
IC = []  

print("Processing Pass 1...\n")

for line in program:
    parts = line.replace(',', '').split()

    if parts[0] == "START":
        LC = int(parts[1])
        IC.append(f"(AD) (C,{LC})")   
        print(f"START found. LC = {LC}")
        continue

    if parts[0] == "END":
        IC.append("(AD)")
        print("END encountered.")
        break
    
    if parts[0] not in OPTAB:
        label = parts[0]
        opcode = parts[1]
        operand = parts[2]

        if label not in SYMTAB:
            SYMTAB[label] = LC
    else:
        label = None
        opcode = parts[0]
        operand = parts[1] if len(parts) > 1 else None

    if opcode in ["MOVER", "ADD", "SUB", "MULT", "MOVEM"]:
        reg = parts[-2]
        symbol = parts[-1]

        IC.append(f"(IS) ({REG[reg]}) ({symbol})")  
        LC += 1

    elif opcode == "DC":
        IC.append(f"(DL) (C,{operand})")   
        LC += 1

    elif opcode == "DS":
        IC.append(f"(DL) (C,{operand})")   
        LC += int(operand)
        
    elif opcode == "STOP":
        IC.append("(IS)")
        LC += 1

    print(f"LC = {LC}")

print("\nIntermediate Code (IC):")
for line in IC:
    print(line)

print("\nSymbol Table (SYMTAB):")
for symbol, address in SYMTAB.items():
    print(f"{symbol} : {address}")