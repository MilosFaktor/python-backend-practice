# testing speed between list compreensions and classic loop
import time


def bench() -> tuple[float, float]:
    N = 10_000

    t0 = time.perf_counter()
    squares = [x * x for x in range(N)]
    t1 = time.perf_counter()

    b = []
    for x in range(N):
        b.append(x * x)
    t2 = time.perf_counter()

    return t1 - t0, t2 - t1


runs: int = 10
c_total = 0
f_total = 0

for _ in range(runs):
    c, f = bench()
    c_total += c
    f_total += f

print("comprehension avg:", c_total / runs)
print("for loop avg:     ", f_total / runs)
