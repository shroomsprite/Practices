def main():
    choice = input("First prime number? (0 for yes, others to stop): ")
    num = 2
    while True:
        if choice == 0:
            if isPrime(num) == True:
                print num
                choice = input("Next prime number after " + str(num) + "? (0 for yes, 1 for stop): ")
                num = num+1
            else:
                while not isPrime(num):
                    num = num+1
        else:
            break

def isPrime(n):
    flag=True
    for i in range(2, (n/2)+1):
        if n % i == 0:
            flag=False
            break
    return flag
    
if __name__ == "__main__":
    main()