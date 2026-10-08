file = open("output.txt", "w")

print("Physics", file=file)
print("Mathematics", file=file)
print("Python", file=file)

file.close()

print("Text has been written to output.txt")