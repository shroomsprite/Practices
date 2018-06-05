import sys

def main():
    choice = input("sequence to that number or to the Nth number(0 for number, 1 for Nth number): ")
    if choice == 0:
        dat_number()
    elif choice == 1:
        nth_number()
    else:
        main()

def dat_number():
    num = input("Pick a number for that number: ")
    seq = [1]
    while seq[-1] < num:
        if len(seq) == 1:
            seq.append(1)
        else:
            if num >= seq[-1]+seq[-2]:
                seq.append(seq[-1]+seq[-2])
            else:
                break
    print seq

def nth_number():
    num = input("Pick a number for N: ")
    seq = [1]
    while len(seq) < num:
        if len(seq) == 1:
            seq.append(1)
        else:
            seq.append(seq[-1]+seq[-2])
    print seq
    

def fibonacci_sum(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    main()
