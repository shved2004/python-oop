class Automobile:
    """
    Атрибуты:
    ----------
    brand : str
        Марка автомобиля (например, 'Toyota').
    model : str
        Модель автомобиля (например, 'Camry').
    year : int
        Год выпуска автомобиля.
    _engine_started : bool
        Флаг, указывающий, запущен ли двигатель автомобиля.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализирует базовый автомобиль.

        Параметры:
        ----------
        brand : str
            Марка автомобиля.
        model : str
            Модель автомобиля.
        year : int
            Год выпуска автомобиля.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self._engine_started = False

    def __str__(self) -> str:
        return f"Автомобиль {self.brand} {self.model}, {self.year} год выпуска."

    def __repr__(self) -> str:
        return f"Automobile(brand='{self.brand}', model='{self.model}', year={self.year})"

    def start_engine(self) -> None:
        self._engine_started = True
        print(f"Двигатель {self.brand} {self.model} запущен.")

    def stop_engine(self) -> None:
        self._engine_started = False
        print(f"Двигатель {self.brand} {self.model} остановлен.")

    def is_engine_started(self) -> bool:
        """
        Проверяет, запущен ли двигатель автомобиля.

        Возвращает:
        ----------
        bool
            True, если двигатель запущен, иначе False.
        """
        return self._engine_started


class PassengerCar(Automobile):
    """

    Атрибуты:
    ----------
    brand : str
        Марка автомобиля, унаследована от Automobile.
    model : str
        Модель автомобиля, унаследована от Automobile.
    year : int
        Год выпуска автомобиля, унаследован от Automobile.
    passenger_capacity : int
        Количество пассажиров, которое может вместить автомобиль.
    """

    def __init__(self, brand: str, model: str, year: int, passenger_capacity: int) -> None:
        """

        Параметры:
        ----------
        brand : str
            Марка автомобиля.
        model : str
            Модель автомобиля.
        year : int
            Год выпуска автомобиля.
        passenger_capacity : int
            Количество пассажиров, которое может вместить автомобиль.
        """
        super().__init__(brand, model, year)
        self.passenger_capacity = passenger_capacity

    def __str__(self) -> str:
        base_info = super().__str__()
        return f"{base_info} Вместимость пассажиров: {self.passenger_capacity}."

    def __repr__(self) -> str:
        return (f"PassengerCar(brand='{self.brand}', model='{self.model}', "
                f"year={self.year}, passenger_capacity={self.passenger_capacity})")

    def start_engine(self) -> None:
        self._run_safety_check()
        super().start_engine()

    def _run_safety_check(self) -> None:
        """
        Непубличный метод, который имитирует проверку безопасности.
        """
        print("Выполнена проверка безопасности перед запуском двигателя.")

    def fold_rear_seats(self) -> None:
        """
        Складывает задние сиденья для увеличения багажного отделения.
        
        Возвращает:
        ----------
        None
        """
        print("Задние сиденья сложены, багажное отделение увеличено.")
