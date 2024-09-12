fibonacci_atual = 0
fibonacci_proximo = 1

print(fibonacci_atual)

while fibonacci_proximo <= 500:
    print(fibonacci_proximo)
    fibonacci_atual, fibonacci_proximo = fibonacci_proximo, fibonacci_atual + fibonacci_proximo