import doctest

class Truck:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Асфальт"
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

if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
