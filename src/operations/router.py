import os
from fastapi import APIRouter, HTTPException, UploadFile, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from .database_connection import get_database
from .types_casting import read_file, write_data

router = APIRouter()
DATA_FRAME = ["id", "Статус", "Вид ДОП", "Подразделение", "Форма обучения", "Восстановление", "Год рождения", "Пол",
              "Гражданство", "Страна", "Регион", "Город", "Образование", "Образовательное учреждение",
              "Направление подготовки", "Квалификация", "Категория слушателей 1", "Категория слушателей 2",
              "Категория слушателей 3", "Студент ТУСУРа", "Должность", "Место работы", "Дата договора", "Курс", "Часов",
              "Юр. лицо", "Начало обучения", "Окончание обучения", "Название организации", "Стоимость", "Оплачено",
              "Причина отчисления", "Как узнал о курсе"]


def _upload_data(upload_file: UploadFile, filename: str):
    if not os.path.exists('excel_files'):
        os.makedirs('excel_files')

    filepath = f"excel_files/{filename}"

    with open(filepath, "wb") as file_object:
        file_object.write(upload_file.file.read())

    return filepath


@router.post("/post_data")
def post_data(upload_file: UploadFile, database: Session = Depends(get_database)):
    if upload_file:
        filename = upload_file.filename
    else:
        raise HTTPException(status_code=400, detail="Не был добавлен ни один файл")

    filepath = _upload_data(upload_file, filename)
    data = read_file(filepath)
    filepath_correct, filepath_incorrect = write_data(data, filename, database)

    response_filename = filepath_incorrect.split("\\")[-1]
    return FileResponse(path=filepath_incorrect, filename=response_filename, media_type='multipart/form-data')
