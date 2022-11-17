from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Получает число."""
    if your_number <= 0:
        return False
    else:
        sqrt_number = calculate_square_root(your_number)
        return print(f'Мы вычислили квадратный корень'
                     f'из введённого вами числа. Это будет: {sqrt_number}')


print(message)
calc(25.5)
