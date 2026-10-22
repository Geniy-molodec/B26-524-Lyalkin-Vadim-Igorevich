def parse_number(value):
    return float(value)

try:
    result = parse_number(input("Введите число: "))
    print(f"Число: {result}")
except ValueError:
    print("Ошибка: введено некорректное значение")