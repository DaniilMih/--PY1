import random

def get_unique_list_numbers() -> list[int]:
    current_range = range(-10, 10)
    random_numbers = random.sample(current_range, 15)

    return random_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
