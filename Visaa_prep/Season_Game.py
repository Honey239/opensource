n = int(input())
if n <= 12:
    if n > 2 and n < 6:
        print("Spring")
    elif n > 5 and n < 9:
        print("Summer")
    elif n > 8 and n < 12:
        print("Autumn")
    else:
        print("Winter")
else:
    print("Invalid")
