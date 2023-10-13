numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missing_index = numbers.index(None)
sum_of_num = sum([num for num in numbers if num is not None])
count_of_elements = len(numbers)
average = sum_of_num / count_of_elements
numbers[missing_index] = average

print("Измененный список:", numbers)
