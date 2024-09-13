# It alternates the roles of the rods (source, destination, auxiliary) in each recursive call.
# You can only move one disk at a time and a larger disk may not be placed on top of a smaller disk.

def hanoi(a: str, b: str, c: str, n: int) -> None:
    # a: source, b: auxiliary, c: destination
    if n == 1:
        print(f"{a} -> {c}")
        return

    # temporarily move the smaller ones to b, to reveal the biggest one on A
    # ignore the biggest ones on c, as they make no difference
    hanoi(a, c, b, n-1)

    # move the biggest one at the bottom
    print(f"{a} -> {c}")

    # move the rest from b to c
    hanoi(b, a, c, n-1)

hanoi('a', 'b', 'c', 4)