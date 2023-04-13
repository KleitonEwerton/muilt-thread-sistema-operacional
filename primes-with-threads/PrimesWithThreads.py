from threading import Thread, Lock
import time

def is_prime(n):
    if (n == 1) or (n == 0):
        return False
    for j in range(2, int(n**0.5) + 1):
        if ((n % j) == 0):
            return False
    return True

def find_primes_in_range(start, end, primes, lock):
    local_primes = []
    for i in range(start, end):
        if is_prime(i):
            local_primes.append(i)
    with lock:
        primes.extend(local_primes)

def main():
    a = 1; b = 10000
    num_threads = 4
    primes = []
    lock = Lock()
    threads = []
    chunk_size = (b - a) // num_threads
    for i in range(num_threads):
        start = a + i*chunk_size
        end = a + (i+1)*chunk_size
        t = Thread(target=find_primes_in_range, args=(start, end, primes, lock))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    primes.sort()
    with open("primes-with-threads.txt", 'w') as outputFile:
        for prime in primes:
            outputFile.write(str(prime) + " ")

if __name__ == "__main__":
    inicio = time.time()
    main()
    fim = time.time()
    tempo_total = fim - inicio
    print("O tempo de execução foi de", tempo_total, "segundos")