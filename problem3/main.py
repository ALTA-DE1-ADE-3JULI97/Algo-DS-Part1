def fibonacci(number):
    if number <= 0:
        return "Nomor number harus lebih besar dari 0"
    
    fib_seq = [0, 1]
    for i in range(2, number):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    
    return fib_seq[number-1]
    # elif number == 1:
    #     return 0
    # elif number == 2:
    #     return 1
    # else:
    #     return fibonacci(number-1) + fibonacci(number-2)

if __name__ == "__main__":
    print(fibonacci(0))  # 0
    print(fibonacci(2))  # 1
    print(fibonacci(9))  # 34
    print(fibonacci(10)) # 55
    print(fibonacci(12)) # 144