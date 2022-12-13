x = int(input("Введите координаты х: "))
y = int(input("Введите координаты y: "))

if x > 0 and y > 0 and x !=0 and y != 0 :
    print("1 четверть")
elif x < 0 and y > 0 and x !=0 and y != 0:
    print("2 четверть")
elif x < 0 and y < 0 and x !=0 and y != 0:
    print("3 четверть")
elif x > 0 and y < 0 and x !=0 and y != 0: 
    print("4 четверть")
else: print("Лежит на оси")
    