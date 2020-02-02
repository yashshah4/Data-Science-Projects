def collatz(number):
    if number%2 == 0:
        print (number//2)
        return (number//2)
    else:
        print (number*3+1)
        return (number*3+1)

try:

    n = int(input("Enter a number : "))
    p=n
    while True:
        p = collatz(p)
        if p == 1:
            break
        else:
            continue

except ValueError:
    print("Invalid input: Enter a number")
