import pandas as pd
import json
import os
from datetime import datetime

DATA_FRAME = ["id", "Статус", "Вид ДОП", "Подразделение", "Форма обучения", "Восстановление", "Год рождения", "Пол",
              "Гражданство", "Страна", "Регион", "Город", "Образование", "Образовательное учреждение",
              "Направление подготовки", "Квалификация", "Категория слушателей 1", "Категория слушателей 2",
              "Категория слушателей 3", "Студент ТУСУРа", "Должность", "Место работы", "Дата договора", "Курс", "Часов",
              "Юр. лицо", "Начало обучения", "Окончание обучения", "Название организации", "Стоимость", "Оплачено",
              "Причина отчисления", "Как узнал о курсе"]
COUNTRIES_VARIANTS = "operations\\countries.json"
SYMBOLS_REMOVE = "/|:;*&?$#^@!~"


def read_file(route: str):
    excel_file = pd.read_excel(route)
    data = pd.DataFrame(excel_file, columns=DATA_FRAME)
    return data


def _edit_data(data: pd.DataFrame):
    new_data = {"id": [],
                "Статус": [],
                "Вид ДОП": [],
                "Подразделение": [],
                "Форма обучения": [],
                "Восстановление": [],
                "Год рождения": [],
                "Пол": [],
                "Гражданство": [],
                "Страна": [],
                "Регион": [],
                "Город": [],
                "Образование": [],
                "Образовательное учреждение": [],
                "Направление подготовки": [],
                "Квалификация": [],
                "Категория слушателей 1": [],
                "Категория слушателей 2": [],
                "Категория слушателей 3": [],
                "Студент ТУСУРа": [],
                "Должность": [],
                "Место работы": [],
                "Дата договора": [],
                "Курс": [],
                "Часов": [],
                "Юр. лицо": [],
                "Начало обучения": [],
                "Окончание обучения": [],
                "Название организации": [],
                "Стоимость": [],
                "Оплачено": [],
                "Причина отчисления": [],
                "Как узнал о курсе": []}
    incorrect_new_data = {"id": [],
                          "Статус": [],
                          "Вид ДОП": [],
                          "Подразделение": [],
                          "Форма обучения": [],
                          "Восстановление": [],
                          "Год рождения": [],
                          "Пол": [],
                          "Гражданство": [],
                          "Страна": [],
                          "Регион": [],
                          "Город": [],
                          "Образование": [],
                          "Образовательное учреждение": [],
                          "Направление подготовки": [],
                          "Квалификация": [],
                          "Категория слушателей 1": [],
                          "Категория слушателей 2": [],
                          "Категория слушателей 3": [],
                          "Студент ТУСУРа": [],
                          "Должность": [],
                          "Место работы": [],
                          "Дата договора": [],
                          "Курс": [],
                          "Часов": [],
                          "Юр. лицо": [],
                          "Начало обучения": [],
                          "Окончание обучения": [],
                          "Название организации": [],
                          "Стоимость": [],
                          "Оплачено": [],
                          "Причина отчисления": [],
                          "Как узнал о курсе": []}
    for i in range(len(data)):
        note = {"id": 0,
                "Статус": "",
                "Вид ДОП": "",
                "Подразделение": "",
                "Форма обучения": "",
                "Восстановление": False,
                "Год рождения": 0,
                "Пол": "",
                "Гражданство": "",
                "Страна": "",
                "Регион": "",
                "Город": "",
                "Образование": "",
                "Образовательное учреждение": "",
                "Направление подготовки": "",
                "Квалификация": "",
                "Категория слушателей 1": "",
                "Категория слушателей 2": "",
                "Категория слушателей 3": "",
                "Студент ТУСУРа": False,
                "Должность": "",
                "Место работы": "",
                "Дата договора": "",
                "Курс": "",
                "Часов": 0,
                "Юр. лицо": False,
                "Начало обучения": "",
                "Окончание обучения": "",
                "Название организации": "",
                "Стоимость": 0,
                "Оплачено": 0,
                "Причина отчисления": "",
                "Как узнал о курсе": ""}
        flag = 0

        birth_year = _cast_birth_year(data.iloc[i]["Год рождения"])
        if birth_year == -1:
            birth_year_result = data.iloc[i]["Год рождения"]
            flag = 1
        else:
            birth_year_result = birth_year
        note["Год рождения"] = birth_year_result

        citizenship = _cast_country(data.iloc[i]["Гражданство"])
        if citizenship == "Ошибка":
            citizenship_result = data.iloc[i]["Гражданство"]
            flag = 1
        else:
            citizenship_result = citizenship
        note["Гражданство"] = citizenship_result

        country = _cast_country(data.iloc[i]["Страна"])
        if country == "Ошибка":
            country_result = data.iloc[i]["Страна"]
            flag = 1
        else:
            country_result = country
        note["Страна"] = country_result

        region = _cast_region(data.iloc[i]["Регион"])
        if region == "Ошибка":
            region_result = data.iloc[i]["Регион"]
            flag = 1
        else:
            region_result = region
        note["Регион"] = region_result

        city = _cast_city(data.iloc[i]["Город"])
        if city == "Ошибка":
            city_result = data.iloc[i]["Город"]
            flag = 1
        else:
            city_result = city
        note["Город"] = city_result

        note["Город"] = _cast_city(data.iloc[i]["Город"])
        note["id"] = data.iloc[i]["id"]
        note["Статус"] = data.iloc[i]["Статус"]
        note["Вид ДОП"] = data.iloc[i]["Вид ДОП"]
        note["Подразделение"] = data.iloc[i]["Подразделение"]
        note["Форма обучения"] = data.iloc[i]["Форма обучения"]
        note["Восстановление"] = _cast_logicals(data.iloc[i]["Восстановление"])
        note["Пол"] = data.iloc[i]["Пол"]
        note["Образование"] = data.iloc[i]["Образование"]
        note["Образовательное учреждение"] = data.iloc[i]["Образовательное учреждение"]
        note["Направление подготовки"] = data.iloc[i]["Направление подготовки"]
        note["Квалификация"] = data.iloc[i]["Квалификация"]
        note["Категория слушателей 1"] = data.iloc[i]["Категория слушателей 1"]
        note["Категория слушателей 2"] = data.iloc[i]["Категория слушателей 2"]
        note["Категория слушателей 3"] = data.iloc[i]["Категория слушателей 3"]
        note["Студент ТУСУРа"] = _cast_logicals(data.iloc[i]["Студент ТУСУРа"])
        note["Должность"] = data.iloc[i]["Должность"]
        note["Место работы"] = data.iloc[i]["Место работы"]
        note["Дата договора"] = data.iloc[i]["Дата договора"]
        note["Курс"] = data.iloc[i]["Курс"]
        note["Часов"] = data.iloc[i]["Часов"]
        note["Юр. лицо"] = _cast_logicals(data.iloc[i]["Юр. лицо"]) if data.iloc[i]["Название организации"] != "" else True
        note["Начало обучения"] = data.iloc[i]["Начало обучения"]
        note["Окончание обучения"] = data.iloc[i]["Окончание обучения"]
        note["Название организации"] = data.iloc[i]["Название организации"]
        note["Стоимость"] = _cast_price(str(data.iloc[i]["Стоимость"]))
        note["Оплачено"] = _cast_price(str(data.iloc[i]["Оплачено"]))
        note["Причина отчисления"] = data.iloc[i]["Причина отчисления"]
        note["Как узнал о курсе"] = data.iloc[i]["Как узнал о курсе"]

        for x in note.keys():
            if flag == 0:
                new_data[x].append(note[x])
            elif flag == 1:
                incorrect_new_data[x].append(note[x])
    return new_data, incorrect_new_data


def _create_empty_excel(columns: list, filename: str, sheet_name: str = 'Sheet1'):
    df = pd.DataFrame(columns=columns)

    if not os.path.exists('excel_files'):
        os.makedirs('excel_files')

    filepath = os.path.join('excel_files', filename)
    excel_writer = pd.ExcelWriter(filepath, engine='xlsxwriter')
    df.to_excel(excel_writer, index=False, sheet_name=sheet_name)
    excel_writer._save()

    return filepath


def write_to_file(data: dict, filename: str):
    df_data = pd.DataFrame(data)
    new_data, incorrect_new_data = _edit_data(df_data)

    filepath_correct = _create_empty_excel(columns=DATA_FRAME, filename=(filename + '_correct_data.xlsx'))
    filepath_incorrect = _create_empty_excel(columns=DATA_FRAME, filename=(filename + '_incorrect_data.xlsx'))

    new_correct_df = pd.DataFrame(new_data)
    new_incorrect_df = pd.DataFrame(incorrect_new_data)

    with pd.ExcelWriter(filepath_correct, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
        new_correct_df.to_excel(writer, sheet_name='Sheet1',
                                startrow=writer.sheets['Sheet1'].max_row, header=False, index=False)

    with pd.ExcelWriter(filepath_incorrect, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
        new_incorrect_df.to_excel(writer, sheet_name='Sheet1',
                                  startrow=writer.sheets['Sheet1'].max_row, header=False, index=False)

    return filepath_correct, filepath_incorrect


def _cast_country(country: str):
    result = ""
    with open(COUNTRIES_VARIANTS) as file:
        countries = json.load(file)
        if isinstance(country, str):
            for x in countries.keys():
                variants = countries.get(x)
                for variant in variants:
                    if country.find(variant) != -1:
                        result = x
                        break
    return result if result != "" else "Ошибка"


def _cast_city(city: str) -> str:
    if isinstance(city, float):
        return "Ошибка"
    if isinstance(city, int):
        return "Ошибка"
    city = city[city.find('..'):] if '..' in city else city
    city = city[city.find('г.'):] if 'г.' in city else city
    city = city[city.find('д.'):] if 'д.' in city else city
    city = city[city.find('с.'):] if 'с.' in city else city
    city = city[city.find('с/п'):] if 'с/п' in city else city
    city = city[city.find('дер.'):] if 'дер.' in city else city
    city = city[city.find('о.'):] if 'о.' in city else city
    city = city[city.find('пгт'):] if 'пгт' in city else city

    city = city.replace('_', " ") if '_' in city else city
    city = city.replace('г.', "") if 'г.' in city else city
    city = city.replace('д.', "") if 'д.' in city else city
    city = city.replace('г ', "") if 'г ' in city else city
    city = city.replace('д ', "") if 'д ' in city else city
    city = city.replace('с.', "") if 'с.' in city else city
    city = city.replace('с/п', "") if 'с/п' in city else city
    city = city.replace('дер.', "") if 'дер.' in city else city
    city = city.replace('о.', "") if 'о.' in city else city
    city = city.replace('пгт.', "") if 'пгт' in city else city
    city = city.replace('пгт', "") if 'пгт' in city else city

    city = city[:city.find(',')] if ',' in city else city
    city = city[:city.find('(')] if '(' in city else city
    city = city[:city.find('/')] if '/' in city else city
    city = city.replace(SYMBOLS_REMOVE, "")
    city = city.strip()
    result = city
    return result


def _cast_region(region: str):
    if isinstance(region, float):
        return "Ошибка"
    if isinstance(region, int):
        return "Ошибка"
    region = region.replace('АР', "Автономная Республика") if 'АР' in region and 'еспулика' not in region and region[region.find('АР') - 1] != "" and region[region.find('АР') + 2] == " " else region
    region = region.replace('АО', "автономная область") if 'АО' in region and 'область' not in region and region[region.find('АО') - 1] == " " and region[region.find('АО') - 2] == "я" else region
    region = region.replace('АО', "автономный округ") if 'АО' in region and 'округ' not in region and region[region.find('АО') - 1] == " " else region
    region = region.replace('АО', "") if 'АО' in region and 'округ' in region else region
    region = region.replace('а.о.', "автономная область") if 'а.о.' in region and 'область' not in region and region[region.find('а.о.') - 1] == " " and region[region.find('а.о.') - 2] == "я" else region
    region = region.replace('а.о.', "автономный округ") if 'а.о.' in region and 'округ' not in region and region[region.find('а.о.') - 1] == " " else region
    region = region.replace('а.о.', "") if 'а.о.' in region and 'округ' in region else region
    region = region.replace('Обл.', "область") if 'Обл.' in region and 'область' not in region else region
    region = region.replace('Обл ', "область") if 'Обл' in region and 'область' not in region else region
    region = region.replace('обл.', "область") if 'обл.' in region and 'область' not in region else region
    region = region.replace('обл ', "область") if 'обл' in region and 'область' not in region else region
    region = region.replace(' обл', "область") if 'обл' in region and 'область' not in region and region[-1] == "л" else region
    region = region.replace('Область', "область") if 'Область' else region
    region = region.replace('Р.', "Республика") if 'Р.' in region and 'еспублика' not in region else region
    region = region.replace('Р ', "Республика ") if 'Р ' in region and 'еспублика' not in region else region
    region = region.replace('р.', "Республика") if 'р.' in region and 'еспублика' not in region else region
    region = region.replace('р ', "Республика ") if 'р ' in region and 'еспублика' not in region else region
    region = region.replace('Респ.', "Республика") if 'Респ.' in region and 'еспублика' not in region else region
    region = region.replace('Респ ', "Республика") if 'Респ' in region and 'еспублика' not in region else region
    region = region.replace('респ.', "Республика") if 'респ.' in region and 'еспублика' not in region else region
    region = region.replace('респ ', "Республика") if 'респ' in region and 'еспублика' not in region else region
    region = region.replace('Рес.', "Республика") if 'Рес.' in region and 'еспублика' not in region else region
    region = region.replace('Рес ', "Республика") if 'Рес' in region and 'еспублика' not in region else region
    region = region.replace('рес.', "Республика") if 'рес.' in region and 'еспублика' not in region else region
    region = region.replace('рес ', "Республика") if 'рес' in region and 'еспублика' not in region else region
    region = region.replace('область', " область") if 'область' in region and region[region.find('область') - 1] != "" and region[region.find('область') - 1] != " " else region
    region = region.replace('Республика', "Республика ") if 'Республика' in region and " Республика" not in region and region[region.find('Республика') + 10] != "" and region[region.find('Республика') + 10] != " " else region
    region = region.replace('республика', "Республика") if 'республика' in region else region
    for symbol in SYMBOLS_REMOVE:
        region = region.replace(symbol, "")

    region = region[:region.find(',')] if ',' in region else region
    region = region[:region.find('(')] if '(' in region else region
    region = region.strip()
    result = region
    return result


def _cast_birth_year(year: int):
    return -1 if (datetime.now().year - year <= 16) or (datetime.now().year - year >= 120) else year


def _cast_logicals(yes_no: str):
    return True if yes_no == "Да" else False


def _cast_price(price: str):
    return int(price.replace(" ", "")) if " " in price else price
