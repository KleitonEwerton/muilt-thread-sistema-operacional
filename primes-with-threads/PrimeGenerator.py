# -*- coding: utf-8 -*-
import time

def main():
    a = 1; b = 10000
    
    primes = []
    
    for i in range(a, b):
        if (i == 1) or (i == 0):
            continue
        
        isPrime = True
        
        for j in range(2, int((i / 2)) + 1):
            if ((i % j) == 0):
                isPrime = False
                break
            
        if (isPrime):
            primes.append(i)
            
    with open("primes.txt", 'w') as outputFile:
        for prime in primes:
            outputFile.write(str(prime) + " ")

if __name__ == "__main__":
    inicio = time.time()
    main()
    fim = time.time()
    tempo_total = fim - inicio
    print("O tempo de execução foi de", tempo_total, "segundos")
