if __name__ == "__main__":
    class Car:
        """ Базовый класс автомобили. """

        def __init__(self, engine: str, transmission: str, control: str):
            self.engine = engine
            self.transmission = transmission
            self.control = control

        def __str__(self):
            return f"Двигатель {self.engine}. Коробка передач {self.transmission}"

        def __repr__(self):
            return f"{self.__class__.__name__}(Двигатель={self.engine!r}, Коробка передач={self.transmission!r})"

        def is_full_fuel_tank(self) -> bool:
            """
            Функция проверяет заправлен ли автомобиль.

            :return:Заправлен ли автомобиль
            """

        def what_type_of_control(self):
            """
            Функция определяет тип управления автомобиля.

            :return: Какой выбран тип управления
            """
            return f'Классическое {self.control}'

    class PassengerVehicle(Car):
        """ Дочерний класс легковые автомобили. """

        def __init__(self, engine: str, transmission: str, control: str, speed: float):
            super().__init__(engine, transmission, control)
            super().is_full_fuel_tank()
            self.speed = speed

        def __str__(self):
            return f"Двигатель {self.engine}. Коробка передач {self.transmission}. Скорость {self.speed}"

        def __repr__(self):
            return f"{self.__class__.__name__}(Двигатель={self.engine!r}, Коробка передач={self.transmission!r}," \
                   f" Скорость={self.speed!r})"

        def what_type_of_control(self):
            """
            Функция определяет тип управления автомобиля.

            :return: Какой выбран тип управления
            """
            return f'Дистанционное {self.control}'


    class Truck(Car):
        """ Дочерний класс грузовые автомобили. """

        def __init__(self, engine: str, transmission: str, control: str, size: float):
            super().__init__(engine, transmission, control)
            super().is_full_fuel_tank()
            self.size = size

        def __str__(self):
            return f"Двигатель {self.engine}. Коробка передач {self.transmission}. Габариты {self.size}"

        def __repr__(self):
            return f"{self.__class__.__name__}(Двигатель={self.engine!r}, Коробка передач={self.transmission!r}," \
                   f" Габариты={self.size!r})"

        def what_type_of_control(self):
            """
            Функция определяет тип управления автомобиля.

            :return: Какой выбран тип управления
            """
            return f'Автоматическое {self.control}'

    pass
