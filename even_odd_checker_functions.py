def check_number(num):
    if num % 2 == 0:
        print(f"{num} is an Even number.")
    else:
        print(f"{num} is an Odd number.")

num = int(input("Enter an integer: "))
check_number(num)
