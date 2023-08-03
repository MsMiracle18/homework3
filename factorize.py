
def factorize_number(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_sync(*numbers):
    result = []
    for num in numbers:
        result.append(factorize_number(num))
    return result

def factorize_parallel(*numbers):
    num_cores = cpu_count()
    with Pool(num_cores) as pool:
        result = pool.map(factorize_number, numbers)
    return result

if __name__ == "__main__":
    def test_factorize(factorize_func):
        a, b, c, d = factorize_func(128, 255, 99999, 10651060)

        assert a == [1, 2, 4, 8, 16, 32, 64, 128]
        assert b == [1, 3, 5, 15, 17, 51, 85, 255]
        assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
        assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    start_time = time.time()
    factorize_sync(128, 255, 99999, 10651060)
    sync_time = time.time() - start_time
    print(f"Synchronous execution time: {sync_time} seconds")

    start_time = time.time()
    factorize_parallel(128, 255, 99999, 10651060)
    parallel_time = time.time() - start_time
    print(f"Parallel execution time: {parallel_time} seconds")

    print(f"Speedup: {sync_time / parallel_time}")

    test_factorize(factorize_sync)
    test_factorize(factorize_parallel)
