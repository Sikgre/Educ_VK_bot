
keyboard_command = {
    "start": "Старт",
    "beginning": "Начать",
    "document": "Заказать документ",
    "consulting": "Заказать консультацию",
    "more": "Дополнительная информация",
    "project": "Узнать о проекте",
    "conditions": "Условия работы",
    "refs": "Отзывы",
    "contract_type": "Договор",
    "trust_type": "Доверенность",
    "declaration_type": "Декларация",
    "labor_law": "Трудовое право",
    "private_law": "Гражданское право",
    "other": "Другое",
    "menu": "В главное меню",
    "back": "На предыдущую страницу"
}

keyboard_answer = {
    "beginning": "Выберите тип заказа или нажмите кнопку \"Узнать о проекте\", чтобы узнать больше",
    "document": "Выберите типы документов, которые вы хотите оформить",
    "consulting": "Выберите тематику вопроса, по которому вам необходима консультация",
    "more": "Вы можете узнать о проекте, об условиях работы или посмотреть отзывы о наших услугах",
    "project": "Здесь должен быть текст о проекте",
    "conditions": "Здесь должен быть текст об условиях работы",
    "refs": "Здесь должен быть текст про отзывы",
    "contract_type": "Приложите необходимые документы для оформления",
    "trust_type": "Приложите необходимые документы для оформления",
    "declaration_type": "Приложите необходимые документы для оформления",
    "labor_law": "Вопрос по трудовому праву",
    "private_law": "Вопрос по гражданскому праву",
    "other": "Задайте свой вопрос",
    "menu": "В главное меню"
}

error_messages = {
    "unknown_command_start": "Для начала диалога нажмите или наберите \"Начать\" (без кавычек)",
    "unknown_command": "Извините, не знаю такой команды. Попробуйте ещё раз"
}


def beginning():
    return keyboard_answer["beginning"]


def document():
    return keyboard_answer["document"]


def consulting():
    return keyboard_answer["consulting"]


def more():
    return keyboard_answer["more"]


def project():
    return keyboard_answer["project"]


def conditions():
    return keyboard_answer["conditions"]


def refs():
    return keyboard_answer["refs"]


def contract_type():
    return keyboard_answer["contract_type"]


def trust_type():
    return keyboard_answer["trust_type"]


def declaration_type():
    return keyboard_answer["declaration_type"]


def labor_law():
    return keyboard_answer["labor_law"]


def private_law():
    return keyboard_answer["private_law"]


def other():
    return keyboard_answer["other"]


def menu():
    return keyboard_answer["menu"]


def error():
    return error_messages["unknown_command"]


answer = {
    keyboard_command["beginning"]: beginning,
    keyboard_command["document"]: document,
    keyboard_command["consulting"]: consulting,
    keyboard_command["more"]: more,
    keyboard_command["project"]: project,
    keyboard_command["conditions"]: conditions,
    keyboard_command["refs"]: refs,
    keyboard_command["contract_type"]: contract_type,
    keyboard_command["trust_type"]: trust_type,
    keyboard_command["declaration_type"]: declaration_type,
    keyboard_command["labor_law"]: labor_law,
    keyboard_command["private_law"]: private_law,
    keyboard_command["other"]: other,
    keyboard_command["menu"]: menu
}
