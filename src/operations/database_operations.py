from fastapi import Depends
from .database_connection import Course, Listener, Assignment, get_database
from sqlalchemy.orm import Session
import pandas as pd

COURSE_DATA_FRAME = ["Курс", "Часов"]
LISTENER_DATA_FRAME = ["id", "Год рождения", "Пол", "Гражданство"]
ASSIGNMENT_DATA_FRAME = ["id", "Курс", "Часов", "Статус", "Вид ДОП", "Подразделение", "Формат", "Форма обучения",
                         "Восстановление",
                         "Дата договора", "Начало обучения", "Окончание обучения", "Стоимость", "Оплачено", "Страна",
                         "Регион", "Город", "Образование", "Образовательное учреждение", "Направление подготовки",
                         "Квалификация", "Категория слушателей 1", "Категория слушателей 2", "Категория слушателей 3",
                         "Студент ТУСУРа", "Должность", "Место работы", "Юр. лицо", "Название организации",
                         "Причина отчисления", "Как узнал о курсе"]
DATA_FRAME = ["id", "Статус", "Вид ДОП", "Подразделение", "Формат", "Форма обучения", "Восстановление", "Год рождения",
              "Пол", "Гражданство", "Страна", "Регион", "Город", "Образование", "Образовательное учреждение",
              "Направление подготовки", "Квалификация", "Категория слушателей 1", "Категория слушателей 2",
              "Категория слушателей 3", "Студент ТУСУРа", "Должность", "Место работы", "Дата договора", "Курс", "Часов",
              "Юр. лицо", "Начало обучения", "Окончание обучения", "Название организации", "Стоимость", "Оплачено",
              "Причина отчисления", "Как узнал о курсе"]


def _load_to_course_table(courses: dict, database: Session):
    courses_df = pd.DataFrame(courses)

    for i in range(len(courses_df)):
        title: str = courses_df.iloc[i]["Курс"]
        duration: int = int(courses_df.iloc[i]["Часов"])

        # Делаем запрос к базе данных
        course_id = database.query(Course).filter(Course.course_title == title).first()

        if not course_id:
            # Если курс не найден, создаем новый объект Course
            course_note = Course(course_title=title, duration_hours=duration)
            database.add(course_note)  # Добавляем в сессию
            database.commit()  # Коммитим изменения
            database.refresh(course_note)  # Обновляем объект с новыми значениями


def _load_to_listener_table(listeners: dict, database: Session = Depends(get_database)):
    listeners_df = pd.DataFrame(listeners)

    for i in range(len(listeners_df)):
        _id: int = int(listeners_df.iloc[i]["id"])
        birth_year: int = int(listeners_df.iloc[i]["Год рождения"])
        sex: str = listeners_df.iloc[i]["Пол"]
        citizenship: str = listeners_df.iloc[i]["Гражданство"]

        listener_id = database.query(Listener).filter(Listener.listener_id == _id).first()

        if not listener_id:
            listener_note = Listener(listener_id=_id, birth_year=birth_year, sex=sex, citizenship=citizenship)
            database.add(listener_note)
            database.commit()
            database.refresh(listener_note)


def _load_to_assignment_table(assignments: dict, database: Session = Depends(get_database)):
    assignments_df = pd.DataFrame(assignments)

    for i in range(len(assignments_df)):
        course_title: str = assignments_df.iloc[i]["Курс"]
        course = database.query(Course).filter(Course.course_title == course_title).first()

        listener_note = Assignment(listener_id=int(assignments_df.iloc[i]["id"]),
                                   course_id=course.course_id,
                                   assignment_status=assignments_df.iloc[i]["Статус"],
                                   additional_educational_program_type=assignments_df.iloc[i]["Вид ДОП"],
                                   department=assignments_df.iloc[i]["Подразделение"],
                                   education_format=assignments_df.iloc[i]["Формат"],
                                   education_form=assignments_df.iloc[i]["Форма обучения"],
                                   reinstatement=assignments_df.iloc[i]["Восстановление"],
                                   assignment_date=str(assignments_df.iloc[i]["Дата договора"]),
                                   is_an_organization=assignments_df.iloc[i]["Юр. лицо"],
                                   organization_name=assignments_df.iloc[i]["Название организации"],
                                   study_start=str(assignments_df.iloc[i]["Начало обучения"]),
                                   study_end=str(assignments_df.iloc[i]["Окончание обучения"]),
                                   price=int(assignments_df.iloc[i]["Стоимость"]),
                                   paid=int(assignments_df.iloc[i]["Оплачено"]),
                                   expulsion_reason=assignments_df.iloc[i]["Причина отчисления"],
                                   country=assignments_df.iloc[i]["Страна"],
                                   region=assignments_df.iloc[i]["Регион"],
                                   city=assignments_df.iloc[i]["Город"],
                                   education=assignments_df.iloc[i]["Образование"],
                                   education_institution=assignments_df.iloc[i]["Образовательное учреждение"],
                                   discipline=assignments_df.iloc[i]["Направление подготовки"],
                                   qualification=assignments_df.iloc[i]["Квалификация"],
                                   listener_category_one=assignments_df.iloc[i]["Категория слушателей 1"],
                                   listener_category_two=assignments_df.iloc[i]["Категория слушателей 2"],
                                   listener_category_three=assignments_df.iloc[i]["Категория слушателей 3"],
                                   tusur_student=assignments_df.iloc[i]["Студент ТУСУРа"],
                                   post=assignments_df.iloc[i]["Должность"],
                                   job=assignments_df.iloc[i]["Место работы"],
                                   where_had_known_about_course=assignments_df.iloc[i]["Как узнал о курсе"])
        database.add(listener_note)
        database.commit()
        database.refresh(listener_note)


def load_to_database(data: dict, database: Session):
    courses = dict.fromkeys(COURSE_DATA_FRAME, [])
    listeners = dict.fromkeys(LISTENER_DATA_FRAME, [])
    assignments = dict.fromkeys(ASSIGNMENT_DATA_FRAME, [])

    for key in courses.keys():
        if key != '':
            courses[key] = data[key]

    for key in listeners.keys():
        if key != '':
            listeners[key] = data[key]

    for key in assignments.keys():
        if key != '':
            assignments[key] = data[key]

    _load_to_course_table(courses, database)
    _load_to_listener_table(listeners, database)
    _load_to_assignment_table(assignments, database)
