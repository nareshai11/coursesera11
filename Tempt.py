Temperature = int(input("Enter Temperature:"))
if Temperature < 10:
    print("It might be cold, Wear jacket")
elif 10 <= Temperature < 20:
    print("A light sweater should be fine!")
elif 20 <= Temperature < 30:
    print("It's hot, Stay hydrated")
else:
    print(" It's  Warm, Enjoy your day!")