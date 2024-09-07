from typing import Any


class Vacancy:
    """
    Класс для работы с вакансиями
    """

    __list_vacancies: list = []
    __slots__ = ("__name", "__url", "__snippet", "__salary")

    def __init__(
        self,
        name: str = "Не указан",
        url: str = "Не указан",
        salary: str | None | dict = None,
        snippet: str = "Не указан",
    ):
        """Конструктор инициализации объекта класса Vacancy (вакансия работника)"""
        self.__name = name
        self.__url = url
        self.__snippet = snippet
        self.__salary = self.__validate(salary)  # метод для проверки валидации зарплаты

        dict_vacancy = {"name": self.__name, "url": self.__url, "salary": self.__salary, "snippet": self.__snippet}
        self.__list_vacancies.append(dict_vacancy)

    def __validate(self: object, salary: Any) -> dict[Any, Any]:
        """Метод валидации зарплаты"""
        if salary is not None:
            self.__salary = salary
            if type(salary) is str:
                salary_split = salary.split(" ")
                self.__salary = {"from": int(salary_split[0]), "to": int(salary_split[2])}
        else:
            self.__salary = {"from": 0, "to": 0}

        return self.__salary

    def __eq__(self: object, other: object) -> bool:
        """Магический метод, который проверяет равны ли два объекта"""
        if not isinstance(other, Vacancy):
            raise TypeError("Неправильный тип для сравнения")
        return (
            self.__name == other.__name
            and self.__url == other.__url
            and self.__snippet == other.__snippet
            and self.__salary["to"] == other.__salary["to"]
        )

    def __lt__(self: object, other: object) -> bool:
        """Магический метод, который проверяет какой из объектов меньше"""
        if isinstance(other, Vacancy):
            return self.__salary["to"] < other.__salary["to"]
        else:
            raise ValueError

    def __gt__(self: object, other: object) -> bool:
        """Магический метод, который проверяет какой из объектов больше"""
        if isinstance(other, Vacancy):
            return self.__salary["to"] > other.__salary["to"]
        else:
            raise ValueError

    @classmethod
    def cast_to_object_list(cls, list_vacancies: list[dict]) -> list[dict]:
        """Метод добавления вакансий из списка вакансий"""
        for vacancies in list_vacancies:
            if vacancies["salary"] is None:
                vacancies["salary"] = {"from": 0, "to": 0}
            elif vacancies["salary"]["from"] is None:
                vacancies["salary"] = {"from": 0, "to": vacancies["salary"]["to"]}
            elif vacancies["salary"]["to"] is None:
                vacancies["salary"] = {"from": vacancies["salary"]["from"], "to": 0}

            cls(
                name=vacancies["name"],
                url=vacancies["url"],
                salary=vacancies["salary"],
                snippet=vacancies["snippet"]["requirement"] if vacancies["snippet"]["requirement"] is not None else "",
            )
        return cls.__list_vacancies

    @classmethod
    def filtered_salary(cls, from_salary: int = 0, to_salary: int = float("inf")) -> None:
        """Метод фильтрации вакансий по зарплате (от и до вилка)"""
        for vacancies in cls.__list_vacancies:
            if vacancies["salary"].get("from", 0) >= from_salary and vacancies["salary"]["to"] <= to_salary:
                print(vacancies)

    @classmethod
    def list_vacancies(cls) -> list[dict]:
        """Метод для получения строкового вывода вакансий"""
        return cls.__list_vacancies

    @classmethod
    def clear_list(cls) -> list:
        """Метод для очищения списка"""
        cls.__list_vacancies = []

    @property
    def name(self):
        """Метод получения имени вакансии"""
        return self.__name

    @property
    def url(self):
        """Метод получения ссылки вакансии"""
        return self.__url

    @property
    def salary(self):
        """Метод получения зарплаты вакансии"""
        return self.__salary

    @property
    def snippet(self):
        """Метод получения описания вакансии"""
        return self.__snippet
