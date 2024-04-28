year = int(input("Which year do you want to check? "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year.")
    if year % 4 == 0 and year % 100 != 0:
        print(f"Because {year} is cleanly divisible by 4 and not by 100.")       
    elif year % 400 == 0:
        print(f"Because {year} is cleanly divisible by 400.")
else:
    print("Normal year.")
    print(f"Because {year} is NOT divisible by 4 or is divisible by 100 but not by 400.")
