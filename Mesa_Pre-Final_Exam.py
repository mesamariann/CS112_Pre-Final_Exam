print("CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM")
print("Created by: Mariann S. Mesa")

def generate_prime(start, end):
    prime = []
    num = max(2, start)

    while num <= end:
        is_prime = True
        i = 2
        while i <= int(num**0.5):
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            prime += [num]
        num += 1

    return prime

def result_prime():
    while True:
        start = int(input("Enter a number [start]: "))

        if start == 0:
            print("Program terminated.")
            break
        end = int(input("Enter a number [end]: "))
        if start < 0:
            print("Please enter a non-negative number.")
            continue
        if end <= start:
            print(f"Please enter a number greater than {start}.")
            continue
        prime_numbers = generate_prime(start, end)
        print(f"Prime numbers between {start} and {end}:")
        print(*prime_numbers)
if __name__ == "__main__":
        result_prime()



