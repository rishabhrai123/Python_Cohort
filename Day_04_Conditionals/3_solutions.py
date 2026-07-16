score=input("Enter the score:")

score=int(score)

if(score>=101):
    print("please verify your scores")
    exit() # used to come out 
if (score>=90):
    grade="A"
elif(score>=80):
    grade="B"
elif(score>=70):
    grade="C"
elif(score>=60):
    grade="D"
else:
    grade="F"

print("Grade:",grade)
