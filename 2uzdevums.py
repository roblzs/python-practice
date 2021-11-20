import math

def calculate_s(a, b, c):
    p = (a + b + c) / 2

    s = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return s

print(calculate_s(int(input("Ievadiet malu a: ")), int(input("Ievadiet malu b: ")), int(input("Ievadiet malu c: "))))