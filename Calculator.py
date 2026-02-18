

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

print("---Профессиональный калькулятор v1.0---")
print("Доступные знаки: +, -, *, /")
while True:
    user_input = input("Введи первое число (или 'выход' для завершения): ").strip().lower()


    if user_input == "выход":
        print("Программа завершена. До встречи!")
        break
    try:
        oper1 = float(user_input)
        char = input("Выбери знак: ")
        oper2 = float(input("Введи второе число: "))



        if char in operations:
            selected_function = operations[char]
            result = selected_function(oper1, oper2)
            print(f"Результат: {result}")


        else:
            print("Не знаю такого знака")

    except ValueError:
        print("Ошибка! Нужно вводить только числа или слово 'выход'.")


    except ZeroDivisionError:
        print("На 0 делить нельзя!")



