n = int(input("Введите номер места: "))
print()
if n>=54:
    print('такого места нет')
else:
    if n > 36:
        print("боковое")
    elif n % 2:
        print("купе низ")
    else:
        print("купе верх")