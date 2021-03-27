
'''
Ниже описаны названия кнопок клавиатуры (в словарях с частью "buttons") 
и сообщения, которые показываются в чате при нажатии на эти кнопки (в словарях с частью messages).
'''

open_dialog_buttons = {
    "beginning": "Начать",
}

open_dialog_messages = {
    "beginning": "Выберите тип заказа или нажмите кнопку \"Дополнительная информация\", чтобы узнать больше",
}

start_buttons = {
    "document": "Заказать документ",
    "consulting": "Заказать консультацию",
    "more": "Дополнительная информация"
}

start_messages = {
    "document": "Выберите типы документов, которые вы хотите оформить",
    "consulting": "Выберите тематику вопроса, по которому вам необходима консультация",
    "more": "Вы можете узнать о проекте, об условиях работы или посмотреть отзывы о наших услугах"
}

about_buttons = {
    "project": "Узнать о проекте",
    "conditions": "Условия работы",
    "refs": "Отзывы",
}

about_messages = {
    "project": "Здесь должен быть текст о проекте",
    "conditions": "Здесь должен быть текст об условиях работы",
    "refs": "Здесь должен быть текст про отзывы",
}

document_buttons = {
    "contract_type": "Договор",
    "trust_type": "Доверенность",
    "declaration_type": "Декларация",
}

document_messages = {
    "contract_type": "Приложите необходимые документы для оформления",
    "trust_type": "Приложите необходимые документы для оформления",
    "declaration_type": "Приложите необходимые документы для оформления"
}

consulting_buttons = {
    "labor_law": "Трудовое право",
    "private_law": "Гражданское право",
    "other": "Другое",
}

consulting_messages = {
    "labor_law": "Вопрос по трудовому праву",
    "private_law": "Вопрос по гражданскому праву",
    "other": "Задайте свой вопрос"
}


def answer_command(message_from_user):
    commands = [open_dialog_buttons, start_buttons, about_buttons, document_buttons, consulting_buttons]
    l_commands = ['open_dialog_buttons', 'start_buttons', 'about_buttons', 'document_buttons', 'consulting_buttons']
    answer_to_commands = [open_dialog_messages, start_messages, about_messages, document_messages, consulting_messages]
    keys_list = []
    for d in commands:
        for key in d.keys():
            keys_list.append(key)
    commands_list = []
    for d in commands:
        for key in d:
            commands_list.append(d[key])
    key = keys_list[commands_list.index(message_from_user)]
    step = 0
    for d in commands:
        step += 1
        for value in d.values():
            if message_from_user == value:
                break
        if message_from_user == value:
            break
    command_dict = eval(l_commands[step-1])
    key_position = list(command_dict.values()).index(message_from_user)
    command_key = list(command_dict.keys())[key_position]

    answer = {}
    answer[str(command_key)] = answer_to_commands[step-1].get(str(command_key), 'Getting command key error')

    return answer


'''
Значения ключей для сообщений об ошибках и сервисных кнопках и сообщениях
'''

error_messages = {
    "unknown_command_start": "Для начала диалога нажмите или наберите \"Начать\" (без кавычек)",
    "unknown_command": "Извините, не знаю такой команды. Попробуйте ещё раз"
}

service_button = {
    "back": "Назад в меню"
}

service_message = {
    "back": ""
}
