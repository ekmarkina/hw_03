def main():
    """ Main function. """
    print("Решение квадратного уравнения вида ax^2 + bx + c = 0")
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))
    result = solve_quadratic_equation(a, b, c)
    if result is None:
        print("Уравнение не имеет корней")
    elif isinstance(result, tuple):
        print("Уравнение имеет два корня:", round(result[0], 2), round(result[1], 2))
    else:
        print("Уравнение имеет один корень:", round(result, 2))


def solve_quadratic_equation(a, b, c):
    """ Solves quadratic equation. """
    d = b ** 2 - 4 * a * c
    if a == 0 or d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)


if __name__ == "__main__":
    main()
