program = [
    "MACRO",
    "INCR &ARG1",
    "ADD AREG, =1",
    "MEND",
    "START 100",
    "INCR ONE",
    "END"
]

MNT = []
MDT = []

mdt_index = 0
mnt_index = 0
inside_macro = False
macro_name = ""

for line in program:
    parts = line.split()

    if line == "MACRO":
        inside_macro = True
        continue

    if line == "MEND":
        MDT.append("MEND")
        mdt_index += 1
        inside_macro = False
        macro_name = ""
        continue

    if inside_macro:
        if macro_name == "":
            macro_name = parts[0]
            MNT.append((mnt_index, macro_name, mdt_index))
            mnt_index += 1
        else:
            MDT.append(line)
            mdt_index += 1

print("MNT TABLE")
print("Index\tName\tMDT Index")
for idx, name, mdt_i in MNT:
    print(f"{idx}\t{name}\t{mdt_i}")

print("\nMDT TABLE")
print("Index\tDefinition")
for i, line in enumerate(MDT):
    print(f"{i}\t{line}")