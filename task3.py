def generate_fibonacci(n):#This code defines a function called generate_fibonacci that takes a single argument n, which represents the desired length of the Fibonacci sequence.
    fibonacci_sequence = [1, 1]

    while len(fibonacci_sequence) < n: #Inside the function, a list called fibonacci_sequence is initialized with the first two elements of the Fibonacci sequence, which are both 1.
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])#A while loop is then used to keep appending elements to the fibonacci_sequence list until its length is equal to the input n. Each new element is calculated by adding the last two elements of the sequence together.

    return fibonacci_sequence


n = int(input("Пожалуйста, введите длину последовательности Фибоначчи: "))
fibonacci_sequence = generate_fibonacci(n)

print("Длина Фибоначчи для {} это \n{}".format(n, ', '.join(map(str, fibonacci_sequence))))