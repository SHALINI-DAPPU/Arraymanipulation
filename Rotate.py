def rotateArray(arr: list, k: int) -> list:

    n = len(arr)

    k = k % n

    return arr[k:] + arr[:k]