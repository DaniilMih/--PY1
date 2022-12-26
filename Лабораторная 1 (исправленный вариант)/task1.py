import doctest

class Truck:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Самосвал"
        :param capacity_volume: объём кузова машины
        :param occupied_volume: объём занимаемого асфальта

        Пример:
        >>> truck = Truck(700, 0) # инициализация экземпляра класса
        """

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объём кузова машины должен быть типа int или float")
        if capacity_volume < 0:
            raise ValueError("Объём кузова машины должен быть положительным числом")

        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объём занимаемого асфальта должен быть типа int или float")
        if occupied_volume < 0:
            raise ValueError("Объём занимаемого асфальта должен быть положительным числом")

        self.occupied_volume = occupied_volume

    def add_asphalt_to_truck(self, asphalt: float) -> None:
        """
        Загружаем асфальт в самосвал.
        :param asphalt: Объём добавляемого асфальта
        :raise ValueError: Вызываем ошибку если количество добавляемого асфальта превышает свободное место в кузове

        Пример:
        >>> truck = Truck(700, 0)
        >>> truck.add_asphalt_to_truck(500)
        """

        if not isinstance(asphalt, (int, float)):
            raise TypeError("Добавляемый асфальт должен быть типа int или float")
        if not asphalt > 0:
            raise ValueError("Добавляемый асфальт должен быть положительным числом")
        ...

    def is_full_truck(self) -> bool:
        """
        Функция проверяет является ли самосвал полностью загруженным
        :return: Является ли самосвал полным

        Пример:
        >>> truck = Truck(700, 700)
        >>> truck.is_full_truck()
        """
        ...

    def remove_asphalt_from_truck(self, retrievable_asphalt: float) -> None:
        """
        Выгрузка асфальта из самосвала

        :param retrievable_asphalt: Объём извлекаемого асфальта
        :raise ValueError: Возвращается ошибка, если количество выгруженного асфальта превышает количество асфальта в самосвале
        :return: Объём выгруженного асфальта

        Пример:
        >>> truck = Truck(700, 700)
        >>> truck.remove_asphalt_from_truck(500)
        """
        ...


class CarTrailer:
    def __init__(self, capacity_amount: int, occupied_amount: int):
        """
        Создание и подготовка к работе объекта "Автомобильный прицеп"
        :param capacity_amount: вместимость трала
        :param occupied_amount: количество занимаемого места техникой в прицепе

        Пример:
        >>> trailer = CarTrailer(2, 0) # инициализация экземпляра класса
        """

        if not isinstance(capacity_amount, int):
            raise TypeError("Вместимость прицепа должна быть типа int")
        if capacity_amount < 0:
            raise ValueError("Вместимость прицепа должна быть положительным числом")

        self.capacity_amount = capacity_amount

        if not isinstance(occupied_amount, int):
            raise TypeError("Количество занимаемого места техникой в прицепе должно быть типа int")
        if occupied_amount < 0:
            raise ValueError("Количество занимаемого места техникой в прицепе должно быть положительным числом")

        self.occupied_amount = occupied_amount

    def add_car_to_trailer(self, car: int) -> None:
        """
        Погрузка техники в прицеп.
        :param car: Количество погруженной техники
        :raise ValueError: Вызываем ошибку если количество погруженной техники превышает свободное место в прицепе

        Пример:
        >>> trailer = CarTrailer(2, 0)
        >>> trailer.add_car_to_trailer(1)
        """

        if not isinstance(car, int):
            raise TypeError("Добавляемая техника должна быть типа int")
        if not car > 0:
            raise ValueError("Добавляемая техника должна быть положительным числом")
        ...

    def is_empty_trailer(self) -> bool:
        """
        Функция проверяет является ли прицеп пустым
        :return: Является ли прицеп пустым

        Пример:
        >>> trailer = CarTrailer(2, 0)
        >>> trailer.is_empty_trailer()
        """
        ...

class Budget:
    def __init__(self, required_volume: float, current_volume: float):
        """
        Создание и подготовка к работе объекта "Бюджет"
        :param required_volume: Необходимый бюджет для реализации проекта
        :param current_volume: Текущий бюджет

        Пример:
        >>> budget = Budget(10000, 6000)
        """

        if not isinstance(required_volume, (int, float)):
            raise TypeError("Необходимый бюджет должен быть типа int или float")
        if required_volume < 0:
            raise ValueError("Необходимый бюджет должен быть положительным числом")

        self.required_volume = required_volume

        if not isinstance(current_volume, (int, float)):
            raise TypeError("Текущий бюджет должен быть типа int или float")
        if current_volume < 0:
            raise ValueError("Текущий бюджет должен быть положительным числом")

        self.current_volume = current_volume

    def is_full_budget(self) -> bool:
        """
        Функция проверяет хватает ли нам бюджета для реализации проекта
        :return: Хватает ли бюджета для реализации проекта

        Пример:
        >>> budget = Budget(10000, 6000)
        >>> budget.is_full_budget()
        """
        ...

    def add_money_to_current_budget(self, money: float) -> None:
        """
        Добавление материальных средств в текущий бюджет
        :param money: Добавляемое количество средств
        :raise ValueError: Вызываем ошибку если количество добавленных средств превышает необходимое количество бюджета

        Пример:
        >>> budget = Budget(10000, 6000)
        >>> budget.add_money_to_current_budget(4000)
        """

        if not isinstance(money, (int, float)):
            raise TypeError("Добавляемые средства должны быть типа int или float")
        if not money > 0:
            raise ValueError("Добавляемые средства должны быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
