password=input("Enter your password:")

l=len(password)

if (l<6):
    print("Weak")
elif(l<=10):
    print("Medium")
else:
    print("Strong")

