# Midrand Speedster
speed = int(input("What was you speed in km/h? "))
limit = int(input("What was the allowed speed on the road? "))
print("")
if speed <= limit:
    print("OK")
elif speed > limit:
    points = (speed - limit)/5
    print("Points:", int(points))
    if points > 12:
        print("Time to go to jail!")
