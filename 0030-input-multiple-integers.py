x, y, z = map(int, input("Enter three integers separated by spaces: ").split())

print("x =", x)
print("y =", y)
print("z =", z)

print("Sum =", x + y + z)
print("Product =", x * y * z)

print("Type of x =", type(x))
print("Type of y =", type(y))
print("Type of z =", type(z))

U = (x**2)*(y**3)*(z**5)
V = x**3 * y**2 * z**6

print("U=", U)
print("V=", V)