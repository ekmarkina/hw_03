current_position = (0, 0)

command = input("Введите направление движения [вверх / вниз / влево / вправо]: ")
assert command in ["вверх", "вниз", "влево", "вправо"], "Неверное направление движения"

if command == "вверх":
    current_position = (current_position[0], current_position[1] + 1)
elif command == "вниз":
    current_position = (current_position[0], current_position[1] - 1)
elif command == "влево":
    current_position = (current_position[0] - 1, current_position[1])
elif command == "вправо":
    current_position = (current_position[0] + 1, current_position[1])

print("Текущая позиция:", current_position)
