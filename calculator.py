import math as math
import geometry


def add_lambda(x_num, y_num):
    return x_num + y_num


def subtract_lambda(x_num, y_num):
    return x_num - y_num


def multiply_lambda(x_num, y_num):
    return x_num * y_num


def divide_lambda(x_num, y_num):
    return x_num / y_num if y_num != 0 else 'Ты чего удамал-(а)? На ноль делить???'


while True:
    operation = input('Введи операцию (сложение, вычитание, умножение, деление, квадратное уравнение,'
                      ' степень, геометрия): ').strip().lower()

    if operation == 'степень':
        a = float(input('Какое число надо возвести в степень: '))
        b = int(input('Какую степень возьмем? '))
        result = a**b
        print(f'Результат: {result}')
        continue

    elif operation == 'геометрия':
        choise = input("Что будем искать (sin, cos, tan, периметр_тре-ка, площадь_тре-ка, "
                       "периметр_круга, площадь_круга, периметр_прям-ка, площадь_прям-ка): ").strip().lower()
        if choise == 'sin':
            angle = int(input("Введите угол для нахождения синуса: "))
            print(geometry.sin(angle))
        elif choise == 'cos':
            angle = int(input("Введите угол для нахождения косинуса: "))
            print(geometry.cos(angle))
        elif choise == 'tan':
            angle = int(input("Введите угол для нахождения тангенса: "))
            print(geometry.tan(angle))
        elif choise == 'периметр_тре-ка':
            a = float(input("Введите сторону а: "))
            b = float(input("Введите сторону b: "))
            c = float(input("Введите сторону c: "))
            print(geometry.p_triangle(a, b, c))
        elif choise == 'площадь_тре-ка':
            a = float(input("Введите сторону а: "))
            h = float(input("Введите высоту h: "))
            print(geometry.s_triangle(a, h))
        elif choise == 'периметр_круга':
            r = float(input("Введите радиус круга: "))
            print(geometry.p_circle(r))
        elif choise == 'площадь_круга':
            r = float(input("Введите радиус круга: "))
            print(geometry.s_circle(r))
        elif choise == 'периметр_прям-ка':
            a = float(input("Введите сторону а: "))
            b = float(input("Введите сторону b: "))
            print(geometry.p_prym(a, b))
        elif choise == 'площадь_прям-ка':
            a = float(input("Введите сторону а: "))
            b = float(input("Введите сторону b: "))
            print(geometry.s_prym(a, b))

    elif operation == 'сложение' or operation == 'вычитание' or operation == 'умножение' or operation == 'деление':
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))

        if operation == 'сложение':
            result = add_lambda(a, b)
            print(f'Результат: {result}')

        elif operation == 'вычитание':
            result = subtract_lambda(a, b)
            print(f'Результат: {result}')

        elif operation == 'умножение':
            result = multiply_lambda(a, b)
            print(f'Результат: {result}')

        elif operation == 'деление':
            result = divide_lambda(a, b)
            print(f'Результат: {result}')
        else:
            print('Ошибка: деление на ноль')

    elif operation == 'выход':
        break

    elif operation == 'квадратное уравнение':
        a = float(input('Введи коэф. [а]: '))
        b = int(input('Введи коэф. [b]: '))
        c = float(input('Введи коэф. [с]: '))
        dis = b**2 - 4 * a * c

        if dis > 0:
            x1 = (-b + math.sqrt(dis)) / (2 * a)
            x2 = (-b - math.sqrt(dis)) / (2 * a)
            print(f'X_1: {x1}. X_2: {x2}.')
            continue

        elif dis == 0:
            x = -b / (2 * a)
            print(f'X: {x}')
            continue

        else:
            print("Нет решений")
            continue

    else:
        print('Неизвестная операция')
        continue
