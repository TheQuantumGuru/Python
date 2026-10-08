u, a, t = map(
    float,
    input("Enter u, a, t separated by spaces: ").split()
)

v = u + a * t
s = u*t + (1/2)*a*t*t

print("u =", u, "m/s")
print("a =", a, "m/s^2")
print("t =", t, "s")
print("Final velocity =", v, "m/s")
print("displacement =", s, "m")