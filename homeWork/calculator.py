print("add sub mul div fact")

choice = input("Enter your choice: ")

match choice:

    case "add":
        n = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        print(f"Addition = {n + n2}")

    case "sub":
        n = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        print(f"Subtraction = {n - n2}")

    case "mul":
        n = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        print(f"Multiplication = {n * n2}")

    case "div":
        n = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        print(f"Division = {n / n2}")

    case "fact":
        factNo = int(input("Enter the number to find its factorial: "))

        fact = 1

        for i in range(1, factNo + 1):
            fact = fact * i

        print(f"Factorial = {fact}")

    case _:
        print("Invalid choice")