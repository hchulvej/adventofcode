with open("2025_01.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Optional: remove trailing newline characters
lines = [line.strip() for line in lines]


print(lines[2])