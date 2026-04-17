grammar = {
    'S': ['AB'],
    'A': ['a', 'ε'],
    'B': ['b']
}

FIRST = {}

def find_first(symbol):
    if symbol not in grammar:
        return {symbol}

    if symbol in FIRST:
        return FIRST[symbol]

    first = set()

    for production in grammar[symbol]:
        if production == 'ε':
            first.add('ε')
            continue

        for char in production:
            char_first = find_first(char)
            first.update(char_first - {'ε'})

            if 'ε' not in char_first:
                break
        else:
            first.add('ε')

    FIRST[symbol] = first
    return first

# 🔹 Print Grammar
print("Grammar:")
for non_terminal in grammar:
    for prod in grammar[non_terminal]:
        print(f"{non_terminal} -> {prod}")

# 🔹 Compute FIRST
for non_terminal in grammar:
    find_first(non_terminal)

# 🔹 Print FIRST Sets
print("\nFIRST Sets:")
for non_terminal in grammar:
    print(f"FIRST({non_terminal}) = {{", ", ".join(FIRST[non_terminal]), "}}")