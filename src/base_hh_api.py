from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseHeadHunterApi(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def connect(self) -> None:
        """Абстрактный метод для подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict[str, Any]]:
        """Абстрактный метод для получения вакансий"""
        pass
