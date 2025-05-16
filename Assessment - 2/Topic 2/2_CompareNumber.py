def compare(n1,n2):
    if n1 > n2:
        print(f"{n1} greater than {n2}")
    elif n1 < n2:
        print(f"{n1} smaller than {n2}")
    else:
        print(f"{n1} is equal to {n2}")

def main():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    compare(n1, n2)

if __name__ == '__main__':
    main()