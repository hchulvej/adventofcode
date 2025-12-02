from pathlib import Path

# Make the input path relative to this script's directory so the script
# can be run from any working directory.
input_path = Path(__file__).parent / "2025_01.txt"

with input_path.open("r", encoding="utf-8") as f:
    lines = [line.strip() for line in f]

print(lines[2])