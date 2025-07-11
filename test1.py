def sum(s1, m1, s2, m2):
    result_s = s1 * m2 + s2 * m1
    result_m = m1 * m2
    return result_s, result_m

def mul(s1, m1, s2, m2):
    result_s = s1 * s2
    result_m = m1 * m2
    return simplify(result_s, result_m)


def fraction_to_number(s1, m1):
    if m1 != 0:
        result = s1 / m1
        return result
    else:
        return "cannot divide by zero"

def simplify(s, m):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    div = gcd(abs(s), abs(m))
    s //= div
    m //= div
    if m < 0:
        s = -s
        m = -m
    return s, m


a = 2
b = 0    
c = 7
d = 1


x, y = mul(a, b, c, d)
print(f"{x}/{y}")

x, y = sum(a, b, c, d)
print(f"{x}/{y}")

z = fraction_to_number(a, b)
print(z)