import os

print("=" * 10, "Science Notes", "=" * 10)

with open("Science Notes.txt", "r") as file:
    for i in file:
        print(i.strip())

print("=" * 34)

print("=" * 10, "Word Count", "=" * 10)

with open("Maths Notes.txt", "r") as new_file:
    for i in new_file:
        words = i.split()
        print(f"{len(words)} words: {i.strip()}")

print("=" * 30)

print("=" * 10, "Merge All Notes", "=" * 10)

if os.path.exists("Science Notes.txt"):
    print("Your Science Notes File exists.")

else:
    print("Your Science Notes File does not exist.\nIt is being created now.")

merge = ""

with open("Science Notes.txt", "r") as file:
    merge += f"=========Science Notes==========\n{file.read()}\n"

with open("Maths Notes.txt", "r") as f:
    merge += f"==========Maths Notes===========\n{f.read()}"

with open("All Notes.txt", "w") as all:
    all.write(merge)

if os.path.exists("All Notes.txt"):
    os.remove("All Notes.txt")
    print("All Notes has been deleted.")

else:
    print("All Notes does not exist.\nHence, it cannot be deleted.")