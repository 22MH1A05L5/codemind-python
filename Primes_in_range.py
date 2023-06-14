def count_primes(m, n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2

    while p ** 2 <= n:
        if is_prime[p]:
            for i in range(p ** 2, n + 1, p):
                is_prime[i] = False
        p += 1
    count = sum(1 for i in range(m, n + 1) if is_prime[i])
    return count
m = int(input())
n = int(input())
result = count_primes(m, n)
print(result)
