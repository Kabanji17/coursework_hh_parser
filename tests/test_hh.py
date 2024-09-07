import unittest
from unittest.mock import MagicMock, patch

from src.hh import HeadHunterAPI


class TestGetVacancies(unittest.TestCase):
    """
    Класс для тестирования метода подключения к API HeadHanter
    """

    @patch.object(HeadHunterAPI, "connect")
    def test_get_vacancies(self, mock_connect):
        # Настроим мок, чтобы он возвращал фейковые данные
        mock_connect.return_value = MagicMock(
            json=lambda: {"items": [{"id": 1, "title": "Developer"}, {"id": 2, "title": "Tester"}]}
        )

        fetcher = HeadHunterAPI()
        result = fetcher.get_vacancies("developer")

        # Ожидаем 20 страниц по 2 вакансии
        expected_vacancies_count = 20 * 2
        self.assertEqual(len(result), expected_vacancies_count)

        # Проверяем, что connect был вызван 20 раз
        self.assertEqual(mock_connect.call_count, 20)

        # Проверяем, что переданный ключевое слово действительно используется
        self.assertIn("text", fetcher._HeadHunterAPI__params)
        self.assertEqual(fetcher._HeadHunterAPI__params["text"], "developer")


if __name__ == "__main__":
    unittest.main()
