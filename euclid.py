def EU(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x1, y1 = EU(b, a % b)  # Recursive call
        x = y1
        y = x1 - (a // b) * y1
        return (gcd, x, y)