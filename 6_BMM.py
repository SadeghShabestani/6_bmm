import termcolor2

x = int(input("Enter First Number: "))  # 20
y = int(input("Enter second Number: "))  # 40

if x > y:
    print(termcolor2.colored("Error! TryAgain", color="red"))
else:
    for i in range(1,x+1):
        if x % i == 0 and y % i == 0:
            bmm = i

print(f"BMM: {bmm}")

