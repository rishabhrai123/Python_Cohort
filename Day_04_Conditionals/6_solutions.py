distance=input("Enter the distance:")

distance=int(distance)

if distance<3:
    medium="Walk"
elif distance>=3:
    medium="Bike"
elif distance>15:
    medium="Car"

print(medium)