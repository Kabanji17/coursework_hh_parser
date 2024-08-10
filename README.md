## coursework_hh_parser

Программа, которая получает информацию о вакансиях с платформы hh.ru в России, сохраняет ее в файл и позволяет удобно работать с ней: добавлять, фильтровать, удалять.

### Структура проекта
```
.
├── src
│ ├── __init__.py
│ ├── utils.py
│ ├── main.py
│ ├── views.py
│ ├── reports.py
│ └── services.py
├── data
│ ├── operations.xlsx
├── tests
│ ├── __init__.py
│ ├── test_utils.py
│ ├── test_views.py
│ ├── test_reports.py
│ └── test_services.py
├── user_settings.json
├── .venv/
├── .env
├── .env_template
├── .git/
├── .idea/
├── .flake8
├── .gitignore
├── pyproject.toml
├── poetry.lock
└── README.md
```