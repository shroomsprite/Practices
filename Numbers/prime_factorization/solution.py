def main():
    num = input("Enter a number for prime factorization: ")
    factor(num)

def factor(n):
    res = []
    for i in range(2, (n/2)+1):
        if n % i ==0 and isPrime(i):
            res.append(i)
    if len(res)>0:
        print res
    else:
        print "no prime factors for this number"

def isPrime(n):
    flag=True
    for i in range(2, (n/2)+1):
        if n % i == 0:
            flag=False
            break
    return flag

if __name__ == "__main__":
    main()