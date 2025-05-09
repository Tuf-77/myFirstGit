import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘└ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ● ● ●  │",
        "│         │",
        "│  ● ● ●  │",
        "└─────────┘"),
 }

dice = []
total = 0
num_of_rolls = int(input("How many dice do you want to roll?: "))

for i in range(num_of_rolls):
    dice.append(random.randint(1, 6))

# for i in range(num_of_rolls):
#     for line in dice_art.get(dice[i]):
#         print(line)

for i in range(5):
    for j in dice:
        print(dice_art.get(j)[i], end="")
    print()
for i in dice:
    total += i

print(dice)
print(f"Total is {total}")
