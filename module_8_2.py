def persanal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            print(f'Некорректный тип данных для подсчета суммы - {item}')
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        result, incorrect_data = persanal_sum(numbers)
        count_numbers = len(numbers) - incorrect_data
        return result / count_numbers
    except ZeroDivisionError:
        return 0

    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Еще строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
