numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
length = len(numbers)
numbers_new = numbers[:4]+numbers[5:]
summa = sum(numbers_new)
numbers[4] = summa / length


print("Измененный список:", numbers)