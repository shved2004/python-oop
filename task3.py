class Book:
    def __init__(self, name: str, author: str) -> None:
        """
        :param name: Название книги (строка).
        :param author: Автор книги (строка).
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f'Книга "{self.name}", автор {self.author}'

    def __repr__(self) -> str:
        return f"Book(name={repr(self.name)}, author={repr(self.author)})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int) -> None:
        """
        :param name: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц (должно быть положительным целым числом).
        """
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self._pages = value

    def __str__(self) -> str:
        return f'Бумажная книга "{self.name}", автор {self.author}, страниц: {self.pages}'

    def __repr__(self) -> str:
        return (f"PaperBook(name={repr(self.name)}, "
                f"author={repr(self.author)}, pages={self.pages})")


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float) -> None:
        """
        :param name: Название книги.
        :param author: Автор книги.
        :param duration: Продолжительность аудиокниги (в часах),
                         должна быть положительным числом.
        """
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        """Продолжительность аудиокниги в часах."""
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом (int или float).")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной.")
        self._duration = float(value)

    def __str__(self) -> str:
        return f'Аудиокнига "{self.name}", автор {self.author}, продолжительность: {self.duration} ч.'

    def __repr__(self) -> str:
        return (f"AudioBook(name={repr(self.name)}, "
                f"author={repr(self.author)}, duration={self.duration})")
