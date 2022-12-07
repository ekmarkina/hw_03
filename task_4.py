import cmath


def main():
    """ Main function. """
    print("Решение квадратного уравнения вида ax^2 + bx + c = 0")
    a_str = input("Введите a: ")
    b_str = input("Введите b: ")
    c_str = input("Введите c: ")
    a = float(a_str) if "j" not in a_str else complex(a_str)
    b = float(b_str) if "j" not in b_str else complex(b_str)
    c = float(c_str) if "j" not in c_str else complex(c_str)
    solve_quadratic_equation_complex(a, b, c)


def solve_quadratic_equation_complex(a, b, c):
    """ Solves quadratic equation also with complex roots. """
    if a == 0 and b == 0 and c == 0:
        print("Уравнение имеет бесконечное кол-во корней")
    elif a == 0 and b == 0:
        print("Уравнение не имеет корней")
    elif a == 0 and c == 0:
        print("Уравнение имеет один корень: 0")
    elif a == 0:
        result = -c / b
        print("Уравнение имеет один корень: ", result)
    elif b == 0:
        result = (-c / a) ** 0.5
        print("Уравнение имеет один корень: ", result)
    else:
        d = b ** 2 - 4 * a * c
        if isinstance(d, complex) or d < 0:
            result = (-b + cmath.sqrt(d)) / (2 * a), (-b - cmath.sqrt(d)) / (2 * a)
            print("Уравнение имеет два корня:", result[0], result[1])
        elif d == 0:
            result = -b / (2 * a)
            print("Уравнение имеет один корень:", round(result, 2))
        else:
            result = (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
            print("Уравнение имеет два корня:", round(result[0], 2), round(result[1], 2))


if __name__ == "__main__":
    main()
