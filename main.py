import re

types = []  # Types available
count = []  # Counts of types
files = []  # List of Files

# Search files and append them to files array
with open('folders.txt', 'r') as f:
    content = f.readlines()
    for i in content:
        i = i.replace("\n", "")
        x = re.search("[a-z][.]", i)
        if x is not None:
            files.append(i)

# Identify the type and increase the count accordingly
for i in files:
    dot = i.find(".")
    type = i[dot+1:]
    if type not in types:
        types.append(type)
        count.append(1)
    else:
        count[types.index(type)] += 1

# Write to the folderscount file
with open('filescount.txt', 'a') as f:
    for i in range(len(types)):
        a = f"{types[i]} : {count[i]}\n"
        f.write(a)
