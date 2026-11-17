
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


limit = int(input())

for i in range(1, limit + 1):
    if is_prime(i):
        print(i, end=" ")
