
keyboard_command = {
    "beginning": "Начать",
    "document": "Заказать документ",
    "consulting": "Заказать консультацию",
    "more": "Дополнительная информация",
    "project": "Узнать о проекте",
    "conditions": "Условия работы",
    "refs": "Отзывы",
    "cancel": "Отменить заказ"
}

keyboard_answer = {
    "beginning": "Выберите тип заказа или нажмите кнопку \"Узнать о проекте\", чтобы узнать больше",
    "document": "Выберите типы документов, которые вы хотите оформить",
    "consulting": "Выберите тематику вопроса, по которому вам необходима консультация",
    "more": "Вы можете узнать о проекте, об условиях работы или посмотреть отзывы о наших услугах",
    "project": "Здесь должен быть текст о проекте",
    "conditions": "Здесь должен быть текст об условиях работы",
    "refs": "Здесь должен быть текст про отзывы",
    "cancel": "Ваш заказ отменён."
}

error_messages = {
    "unknown_command_start": "Для начала диалога нажмите или наберите \"Начать\" (без кавычек)",
    "unknown_command": "Извините, не знаю такой команды. Попробуйте ещё раз",
    "incorrect_command": "На данном шаге нельзя использовать эту команду."
}

steps = {
    "document":
        {
            "type": "Сообщение о выборе типа документа",
            "file_1": "Сообщение о выборе файла №1",
            "file_2": "Сообщение о выборе файла №2"
        },
    "consulting":
        {
            "type": "Сообщение о выборе типа консультации",
            "your_question": "Напишите свой вопрос"
        },
    "finish_order": "Ваш заказ принят. Ожидайте ответа администратора"
}


answer = {
    keyboard_command["beginning"]: keyboard_answer["beginning"],
    keyboard_command["document"]: keyboard_answer["document"],
    keyboard_command["consulting"]: keyboard_answer["consulting"],
    keyboard_command["more"]: keyboard_answer["more"],
    keyboard_command["project"]: keyboard_answer["project"],
    keyboard_command["conditions"]: keyboard_answer["conditions"],
    keyboard_command["refs"]: keyboard_answer["refs"],
    keyboard_command["cancel"]: keyboard_answer["cancel"],
    "incorrect_command": error_messages["incorrect_command"],
    "unknown_command": error_messages["unknown_command"]
}
