from typing import Any, Dict, List

import requests
from requests import Response

from src.base_hh_api import BaseHeadHunterApi


class HeadHunterAPI(BaseHeadHunterApi):
    """
    Класс для работы с API HeadHunter
    Класс BaseHeadHunterApi является родительским классом
    """

    def __init__(self, file_worker: str = "data/vacancies.json"):
        """Метод для инициализации экземпляра класса."""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []  # конечный список, в который складываются вакансии list[dict]
        super().__init__(file_worker)

    def connect(self) -> Response:
        """Метод для подключения к API. Проверка доступности"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code != 200:
            raise Exception(f"Ошибка подключения к API: {response.status_code}")
        return response

    def get_vacancies(self, keyword: str) -> List[Dict[str, Any]]:
        """Метод для получения вакансий"""
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            vacancies = self.connect().json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

        return self.__vacancies


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies(keyword="Python")
    print(vacancies)
