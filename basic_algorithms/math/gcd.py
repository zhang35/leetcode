# Greatest Common Divisor
# Euclidean algorithm
def euclid(m: int, n: int) -> int:
    while n:
        r = m % n
        m, n = n, r
    return m

print(euclid(12, 8))