characters = int(input("Enter the number of chararcters you want to preview from your notes:"))

file = open("Notes.txt", "r")
print(f"The first {characters} characters in your notes are: {file.read(characters)}\n")
file.close()

file = open("Notes.txt", "r")
lines = file.readlines()
file.close()

print(f"The length of lines in your notes are: {len(lines)}")

for i in range(1, len(lines) + 1):
    print(f"{i} - {lines[i - 1].strip()}")

print()

word = input("Skip the lines in your notes starting with:")
file = open("Notes.txt", "r")

for i in file:
    if i.startswith(word):
        print(f"Skip - {i.strip()}")

    else:
        print(f"Keep - {i.strip()}")

file.close()
print()

file = open("Notes.txt", "r")

abc = file.readlines()
file.close()

new_file = open("New Notes.txt", "w")

for i in range(0, len(abc), 2):
    new_file.write(abc[i])

new_file.close()
print("You have successfully updated your new notes!")