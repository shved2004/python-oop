from abc import ABC, abstractmethod


class Table(ABC):
    """
    Абстрактный класс, описывающий предмет мебели "Стол".
    Содержит базовые характеристики: материал, количество ножек и цвет.
    """

    def __init__(self, material: str, number_of_legs: int, color: str) -> None:
        """
        Инициализатор абстрактного класса Table.

        :param material: Материал, из которого изготовлен стол (например, 'дерево', 'пластик').
        :param number_of_legs: Количество ножек стола, должно быть не меньше 1.
        :param color: Цвет стола (например, 'коричневый', 'белый', 'черный').
        """
        if number_of_legs < 1:
            raise ValueError("Стол не может иметь меньше одной ножки!")
        self.material = material
        self.number_of_legs = number_of_legs
        self.color = color

    @abstractmethod
    def place_object_on_top(self, object_name: str) -> None:
        """
        Кладёт объект на поверхность стола.

        :param object_name: Название объекта, который нужно положить на стол.
        :type object_name: str
        :return: Ничего не возвращает.
        :rtype: None

        Пример использования (через дочерний класс):
        >>> class WoodenTable(Table):
        ...     def place_object_on_top(self, object_name: str) -> None:
        ...         ...
        ...     def adjust_height(self, new_height: float) -> None:
        ...         ...
        ...     def repaint(self, new_color: str) -> None:
        ...         ...
        ...
        >>> t = WoodenTable('дерево', 4, 'коричневый')
        >>> t.place_object_on_top('книга')
        """
        ...

    @abstractmethod
    def adjust_height(self, new_height: float) -> None:
        """
        Регулирует высоту стола.

        :param new_height: Новая высота стола в сантиметрах. Должна быть положительным числом.
        :type new_height: float
        :return: Ничего не возвращает.
        :rtype: None

        Пример:
        >>> class OfficeTable(Table):
        ...     def place_object_on_top(self, object_name: str) -> None:
        ...         ...
        ...     def adjust_height(self, new_height: float) -> None:
        ...         ...
        ...     def repaint(self, new_color: str) -> None:
        ...         ...
        ...
        >>> office_table = OfficeTable('металл', 4, 'серый')
        >>> office_table.adjust_height(75.0)
        """
        ...

    @abstractmethod
    def repaint(self, new_color: str) -> None:
        """
        Перекрашивает стол в новый цвет.

        :param new_color: Цвет, в который нужно перекрасить стол.
        :type new_color: str
        :return: Ничего не возвращает.
        :rtype: None

        Пример:
        >>> class PlasticTable(Table):
        ...     def place_object_on_top(self, object_name: str) -> None:
        ...         ...
        ...     def adjust_height(self, new_height: float) -> None:
        ...         ...
        ...     def repaint(self, new_color: str) -> None:
        ...         ...
        ...
        >>> p_table = PlasticTable('пластик', 4, 'белый')
        >>> p_table.repaint('черный')
        """
        ...


class Tree(ABC):
    """
    Абстрактный класс, описывающий дерево (биологический объект).
    Содержит базовые характеристики: вид дерева, возраст, высоту.
    """

    def __init__(self, species: str, age: int, height: float) -> None:
        """
        Инициализатор абстрактного класса Tree.

        :param species: Вид дерева (например, 'береза', 'дуб', 'сосна').
        :param age: Возраст дерева в годах, не может быть отрицательным.
        :param height: Высота дерева в метрах, не может быть отрицательной.
        """
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным!")
        if height < 0:
            raise ValueError("Высота дерева не может быть отрицательной!")
        self.species = species
        self.age = age
        self.height = height

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева и, возможно, его высоту.

        :param years: Количество лет, на которое дерево становится старше.
                      Должно быть положительным.
        :type years: int
        :return: Ничего не возвращает.
        :rtype: None

        Пример использования (через дочерний класс):
        >>> class Oak(Tree):
        ...     def grow(self, years: int) -> None:
        ...         ...
        ...     def shed_leaves(self) -> None:
        ...         ...
        ...     def photosynthesize(self, hours: int) -> float:
        ...         return 0.0
        ...
        >>> oak = Oak('дуб', 50, 15.0)
        >>> oak.grow(5)
        """
        ...

    @abstractmethod
    def shed_leaves(self) -> None:
        """
        Имитация процесса сбрасывания листьев (для лиственных деревьев).

        :return: Ничего не возвращает.
        :rtype: None

        Пример:
        >>> class Birch(Tree):
        ...     def grow(self, years: int) -> None:
        ...         ...
        ...     def shed_leaves(self) -> None:
        ...         ...
        ...     def photosynthesize(self, hours: int) -> float:
        ...         return 0.0
        ...
        >>> birch = Birch('береза', 10, 7.5)
        >>> birch.shed_leaves()
        """
        ...


class Stack(ABC):
    """
    Абстрактный класс, описывающий структуру данных "Стек".
    Содержит базовые характеристики: максимальная вместимость и текущее количество элементов.
    """

    def __init__(self, capacity: int) -> None:
        """
        Инициализатор абстрактного класса Stack.

        :param capacity: Максимальное количество элементов, которое может хранить стек.
                         Должно быть больше или равно 1.
        """
        if capacity < 1:
            raise ValueError("Вместимость стека не может быть меньше 1!")
        self.capacity = capacity
        self.size = 0

    @abstractmethod
    def push(self, item: str) -> None:
        """
        Добавляет элемент (строку) в стек.

        :param item: Строка, которую необходимо добавить.
        :type item: str
        :return: Ничего не возвращает.
        :rtype: None

        Пример (через дочерний класс):
        >>> class StringStack(Stack):
        ...     def push(self, item: str) -> None:
        ...         if self.size >= self.capacity:
        ...             raise OverflowError("Стек заполнен!")
        ...         self.size += 1
        ...     def pop(self) -> str:
        ...         if self.size == 0:
        ...             raise IndexError("Стек пуст!")
        ...         self.size -= 1
        ...         return "item"
        ...     def peek(self) -> str:
        ...         if self.size == 0:
        ...             raise IndexError("Стек пуст!")
        ...         return "item"
        ...
        >>> s_stack = StringStack(2)
        >>> s_stack.push("Первый элемент")
        """
        ...

    @abstractmethod
    def pop(self) -> str:
        """
        Удаляет верхний элемент из стека и возвращает его.

        :return: Удалённый элемент из стека (строка).
        :rtype: str

        Пример:
        >>> class StringStack(Stack):
        ...     def push(self, item: str) -> None:
        ...         ...
        ...     def pop(self) -> str:
        ...         return "некоторая строка"
        ...     def peek(self) -> str:
        ...         return "некоторая строка"
        ...
        >>> s_stack = StringStack(2)
        >>> s_stack.pop()
        'некоторая строка'
        """
        ...

    @abstractmethod
    def peek(self) -> str:
        """
        Возвращает верхний элемент стека, не удаляя его.

        :return: Верхний элемент (строка) в стеке.
        :rtype: str

        Пример:
        >>> class StringStack(Stack):
        ...     def push(self, item: str) -> None:
        ...         ...
        ...     def pop(self) -> str:
        ...         return "некоторая строка"
        ...     def peek(self) -> str:
        ...         return "некоторая строка"
        ...
        >>> s_stack = StringStack(2)
        >>> s_stack.peek()
        'некоторая строка'
        """
        ...
