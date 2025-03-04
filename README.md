# ПРИ ПЕРВОМ ЗАПУСКЕ
### В терминале IDE ввести следующие команды:
1) python.exe -m venv .venv
2) .venv/Scripts/Activate.ps1 - для Python версии < 3.10;
   .venv/Scripts/activate.ps1 - для Python версии >= 3.10
3) python.exe -m pip install -r requirements.txt

### Программа работает как API с одним эндпоинтом, в который необходимо загрузить файл формата .xlsx
### Возвращает файл с некорректными данными