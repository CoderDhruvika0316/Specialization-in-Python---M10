file = open("Bucket List.txt", "w")

file.write("-> Code my own website\n")
file.write("-> Master learning the recorder\n")
file.write("-> Go to a K - pop concert\n")
file.write("-> Eat ramyeon\n")

file.close()
print("Your Bucket List has been saved!!")

file = open("Bucket List.txt", "r")

bucket_list = file.read()
print("-" * 15, "MY BUCKET LIST", "-" * 15)
print(bucket_list)
print("-" * 50, "\n")

file.close()

file = open("Bucket List.txt", "r")

lines = file.readlines()

file.close()
print(f"There are {len(lines)} items on your Bucket List.")

file = open("Bucket List.txt", "a")

file.write("-> Own a pet cat\n")
file.write("-> Travel to Korea and Japan\n")

file.close()
print("You have successfully added two items to your Bucket List!!\n")

file = open("Bucket List.txt", "r")

updated_bucket_list = file.read()
print("-" * 15, "UPDATED BUCKET LIST", "-" * 15)
print(updated_bucket_list)
print("-" * 50)