# ПРИ ПЕРВОМ ЗАПУСКЕ
### В alembic.ini и в src/operations/database_connection.py в url внести свои данные авторизации на сервере PostgreSQL
### В терминале IDE ввести следующие команды:
1) python.exe -m venv .venv
2) .venv/Scripts/Activate.ps1 - для Python версии < 3.10;
   .venv/Scripts/activate.ps1 - для Python версии >= 3.10
3) python.exe -m pip install -r requirements.txt
4) python.exe -m alembic revision --autogenerate
5) python.exe -m alembic upgrade head

### Программа работает как API с одним эндпоинтом, в который необходимо загрузить файл формата .xlsx
### Возвращает файл с некорректными данными