from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class BaseJSONSaver(ABC):
    """
    Абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
    получения данных из файла по указанным критериям и удаления информации о вакансиях.
    """

    @abstractmethod
    def add_vacancy(self: object, vacancy: Vacancy) -> None:
        """Абстрактный метод для добавления вакансий в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self: object, vacancy: Vacancy) -> None:
        """Абстрактный метод для удаления информации о вакансиях"""
        pass
