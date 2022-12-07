current_position = (0, 0)

while True:
    command = input("Введите направление движения [вверх / вниз / влево / вправо] или ВЫХОД для окончания движения: ")
    assert command in ["вверх", "вниз", "влево", "вправо", "ВЫХОД"], "Неверная команда"

    if command == "ВЫХОД":
        print("Движение окончено")
        break
    if command == "вверх":
        current_position = (current_position[0], current_position[1] + 1)
    elif command == "вниз":
        current_position = (current_position[0], current_position[1] - 1)
    elif command == "влево":
        current_position = (current_position[0] - 1, current_position[1])
    elif command == "вправо":
        current_position = (current_position[0] + 1, current_position[1])

    print("Текущая позиция:", current_position)
