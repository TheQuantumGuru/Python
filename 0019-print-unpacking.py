numbers = [1, 2, 3, 4, 5]
subjects = ["Physics", 'Maths', "Python"]

print(numbers)
print(*numbers)

print(subjects)
print(*subjects)

print(*subjects, sep=" , ")
print(*numbers, sep=" < ")