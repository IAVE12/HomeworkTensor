print("Введите x")
x = float(input())
print("Введите y")
y = float(input())
print("Сложение:", x+y)
if (x > y ) : 
    print("Вычитание:", x - y)
    print("Деление:",x / y)
    print("Целочисленное деление:",x // y)  
    print("Деление по модулю:", x % y)
else:
    print("Целочисленное деление:",y // x)
    print("Деление по модулю:", y % x)
    print("Вычитание:", y - x)
    print("Деление:",y / x)

print ("Умножени:", x * y)
print ("Возведение в степень x в степени y:",x ** y)
print("Возведение в степень y в степени x:",y ** x)
