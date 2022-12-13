x = int(input("Введите координаты х: "))
y = int(input("Введите координаты y: "))

if x > 0 and y > 0:
    print("1 четверть")
elif x < 0 and y > 0:
    print("2 четверть")
elif x < 0 and y < 0:
    print("3 четверть")
else: print("4 четверть")