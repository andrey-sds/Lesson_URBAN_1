def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        k = 0
        for i in range(2, result // 2 + 1):
            if result % i == 0:
                k += 1
        if k <= 0:
            return f"Простое\n{result}"
        else:
            return f"Составное\n{result}"
    return wrapper


@is_prime
def sum_three(*args):
    res = 0
    for i in args:
        res += i
    return res


result = sum_three(2, 5, 6)
print(result)
