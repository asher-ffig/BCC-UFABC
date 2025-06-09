H = [5, 2, 5, 1, 1, 0]

def heaps(H: list) -> bool:
    for j in range(1, len(H)):
        if H[(j - 1) // 2] < H[j]:
            return False
    return True

heaps(H)
