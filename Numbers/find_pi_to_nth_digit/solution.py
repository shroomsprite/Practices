import sys
import math

def main():
    num = input("Pick a number between 0 and 11 of the decimal places to which you'd like PI printed: ")
    #print num
    #print math.pi
    print math.floor(math.pi * math.pow(10, num)) / math.pow(10, num)

if __name__ == "__main__":
    main()
