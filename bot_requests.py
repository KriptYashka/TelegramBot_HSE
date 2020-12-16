import Classes.DB_class as DataTool

def add_worker(params): # Передается 6 параметров
    name, is_conf, contact, edu, post_id, workplace_id = (item for item in params)
    if not(is_conf == "0" or is_conf == "1"):
        return "Параметр(2) **Нал. Конф. Инф.** должен быть 0 или 1."
    if not post_id.isdigit:
        return "Параметр(5) **ID зарплаты** должен быть числом."
    if not workplace_id.isdigit:
        return "Параметр(6) **ID место работы** должено быть числом."
    # Выполняется, если все данные впорядке
    db = DataTool.DataBase()
    table_params = ["name", "is_confidential", "contacts", "education", "post_id", "workplace_id"]
    error = db.add_item("workers", params, table_params)

def add_workplace(params): # Передается 3 параметра
    monitor, level, address = (item for item in params)
    if not(monitor == "0" or monitor == "1"):
        return "Параметр(1) **монитор** должен быть 0 или 1."
    if not level.isdigit:
        return "Параметр(2) **этаж** должен быть числом."
    # Выполняется, если все данные впорядке
    db = DataTool.DataBase()
    table_params = ["monitor", "level", "address"]
    db.add_item("workplace", params, table_params)

def add_post(params): # Передается 3 параметра
    name, salary, vacancy_rate = (item for item in params)
    if not(vacancy_rate == "0" or vacancy_rate == "1"):
        return "Параметр(2) **вакантность** должен быть 0 или 1."
    if not salary.isdigit:
        return "Параметр(3) **оклад** должен быть числом."
    # Выполняется, если все данные впорядке
    db = DataTool.DataBase()
    table_params = ["name", "salary", "vacancy_rate"]
    db.add_item("post", params, table_params)

def select_worker(id):
    if not id.isdigit:
        return "ID должен быть числом"
