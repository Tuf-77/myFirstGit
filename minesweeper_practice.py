
rows = 5
columns = 5

for i in range(rows):
    i += 1
    print(f"{i:-}", end=" ")

print()

for column in range(columns):
    column += 1
    print(column, end="")
    for row in range(rows+1):
        print("| ", end="")
    print()
