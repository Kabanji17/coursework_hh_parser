from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def filter_vacancies(vacancies_list: list, filter_words: list) -> list:
    """Функция фильтрует вакансии по ключевым словам"""
    filtered_vacancies = []

    for vacancy in vacancies_list:
        for word in filter_words:
            if word.lower() in vacancy["name"].lower() or word.lower() in vacancy["snippet"].lower():
                filtered_vacancies.append(vacancy)

    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies: list, salary_range: str) -> list:
    """Функция сортирует вакансии по вилке зарплаты(от и до)"""
    filtered_salary_vacancies = []
    from_to_salary = salary_range.split()

    for vacancy in filtered_vacancies:
        if vacancy["salary"]["from"] >= int(from_to_salary[0]) and vacancy["salary"]["to"] <= int(from_to_salary[2]):
            filtered_salary_vacancies.append(vacancy)

    return sorted(filtered_salary_vacancies, key=lambda to: to["salary"]["to"], reverse=True)


def get_top_vacancies(filtered_vacancies: list, top_n: int) -> list:
    """Функция вывода топ вакансий по выбору пользователя"""
    filtered_vacancies = filtered_vacancies[0:top_n]
    return filtered_vacancies


def print_vacancies(vacancies: list) -> None:
    """Функция вывода отфильтрованных вакансий в консоль"""
    for vacancy in vacancies:
        print("***********************************************************")
        print(f"Название вакансии: {vacancy["name"]}")
        print(f"Ссылка на вакансию: {vacancy["url"]}")
        print(f"Зарплата: {vacancy["salary"]["from"]} - {vacancy["salary"]["to"]} руб.")
        print(f"Требования: {vacancy["snippet"]}")
        print("-----------------------------------------------------------")
