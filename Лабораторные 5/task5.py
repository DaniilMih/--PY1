import random
import string


def get_random_password() -> str:
    random_password = "".join(random.sample(string.hexdigits, 8))  # TODO написать функцию генерации случайных паролей
    return (random_password)

print(get_random_password())
