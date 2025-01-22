class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Конструктор класса Book.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id_}, name={repr(self.name)}, pages={self.pages})"


class Library:
    def __init__(self, books=None):
        """

        :param books: Необязательный список книг. 
                      Если ничего не передано, инициализируется пустым списком.
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для добавления новой книги.
        Если книг в библиотеке нет, возвращается 1.
        Иначе возвращается id последней книги + 1.
        """
        if not self.books:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке, хранящемся в атрибуте экземпляра класса.
        Если книга с таким id не найдена, вызывается ошибка ValueError.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке self.books.
        :raises ValueError: если книги с запрашиваемым id не существует.
        """
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")
