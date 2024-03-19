color1 = input("color1 красный, синий или желтый: ")
color2 = input("color2 красный синий или желтый: ")
if color1 == "красный" and color2 == "синий" or color1 == "синий" and color2 == "красный":
    print("Фиолетовый")
elif color1 == "красный" and color2 == "желтый" or color1 == "желтый" and color2 == "красный":
    print("Оранжевый")
elif color1 == "синий" and color2 == "желтый" or color1 == "желтый" and color2 == "синий":
    print("Зеленый")
else:
    print("Ошибка! Введите название одного из основных цветов: красный, синий или желтый")