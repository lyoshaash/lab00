#задание 1
print("Ответ:", 3 * 4**3)

#задание 2
n = 9**8 + 3**5 - 9
string = ''
while n > 0:
    string+=str(n%3)
    n //= 3
print(string.count('2'))

#задание 3
def is_prime(n):
    return all(n % i != 0 for i in range(2,n))

def numbers(m, n):
    i = 3
    while True:
        if is_prime(i):
            j = i ** 4
            if n < j:
                break
            while j <= n:
                if m <= j:
                    yield j
                j *= 2
        i += 2
print(*sorted(numbers(45_000_000, 50_000_000)), sep='\n')