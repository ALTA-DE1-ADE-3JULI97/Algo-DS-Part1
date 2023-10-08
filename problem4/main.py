def generate_primes_grid(width, height, start):
    result = []
    num = start

    while len(result) < (height * width):
        is_prime = True
        for prime in result:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)
        num += 1

    generate_primes_grid = []
    for i in range(height):
        row = result[i*width : (i+1)*width]
        generate_primes_grid.append(row)
    return generate_primes_grid

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """