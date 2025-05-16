def leap_year(n):
    if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
        print(f"{n} is a leap year!")
    else:
        print(f"{n} is not a leap year!")

def main():
    n = int(input("Enter a year: "))
    leap_year(n)

if __name__ == '__main__':
    main()