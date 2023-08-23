import ctypes

library = ctypes.cdll.LoadLibrary("./library.so")
go_collatz = library.collatz
go_loop_collatz = library.loopCollatz


def collatz(n: int):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


def fast_collatz(n: int):
    go_collatz.argtypes = [ctypes.c_int]
    go_collatz.restype = ctypes.c_int
    return go_collatz(n)


def loop_collatz(n: int, k: int):
    go_loop_collatz.argtypes = [ctypes.c_int, ctypes.c_int]
    go_loop_collatz.restype = ctypes.c_int
    return go_loop_collatz(n, k)


n = 5
n = loop_collatz(n, 1_000_000_000)
print(n)
