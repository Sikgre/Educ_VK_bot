from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import buttons_and_messages

'''
Функция для упрощённого указания цвета кнопок
'''


def colors(col):
    color = {
        "green": VkKeyboardColor.POSITIVE,
        "red": VkKeyboardColor.NEGATIVE,
        "white": VkKeyboardColor.SECONDARY,
        "blue": VkKeyboardColor.PRIMARY
    }
    col_func = color.get(col)
    return col_func

'''
Ниже идут несколько функций, определяющих, какая клавиатура выводится
в ответ на различные сообщения. Функции написаны для клавиатур,
которые должны выводиться в ответ на команды с клавиатуры
'''


def keyboard_begin():
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard.add_button('Начать', color=colors("red"))
    create_keyboard = create_keyboard.get_keyboard()
    return create_keyboard


def keyboard_start():
    button = buttons_and_messages.start_buttons
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard.add_button(button["document"], color=colors("red"))
    create_keyboard.add_button(button["consulting"], color=colors("white"))
    create_keyboard.add_button(button["more"], color=colors("green"))
    create_keyboard = create_keyboard.get_keyboard()
    return create_keyboard


def keyboard_back():
    button = buttons_and_messages.service_button
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard.add_button(button["back"], color=colors("blue"))
    create_keyboard = create_keyboard.get_keyboard()
    return create_keyboard


def keyboard_about():
    button = buttons_and_messages.about_buttons
    service = buttons_and_messages.service_button
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard.add_button(button["project"], color=colors("red"))
    create_keyboard.add_button(button["conditions"], color=colors("white"))
    create_keyboard.add_button(button["refs"], color=colors("green"))
    create_keyboard.add_button(service["back"], color=colors("blue"))
    create_keyboard = create_keyboard.get_keyboard()
    return create_keyboard


def keyboard_document():
    button = buttons_and_messages.document_buttons
    service = buttons_and_messages.service_button
    start = buttons_and_messages.start_buttons
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard.add_button(button["contract_type"], color=colors("red"))
    create_keyboard.add_button(button["trust_type"], color=colors("white"))
    create_keyboard.add_button(button["declaration_type"], color=colors("green"))
    create_keyboard.add_button(service["back"], color=colors("blue"))
    create_keyboard.add_button(start["more"], color=colors("blue"))
    create_keyboard = create_keyboard.get_keyboard()
    return create_keyboard


def keyboard_consulting():
    button = buttons_and_messages.consulting_buttons
    service = buttons_and_messages.service_button
    start = buttons_and_messages.start_buttons
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard.add_button(button["labor_law"], color=colors("red"))
    create_keyboard.add_button(button["private_law"], color=colors("white"))
    create_keyboard.add_button(button["other"], color=colors("green"))
    create_keyboard.add_button(service["back"], color=colors("blue"))
    create_keyboard.add_button(start["more"], color=colors("blue"))
    create_keyboard = create_keyboard.get_keyboard()
    return create_keyboard


'''
Словарь функций для клавиатур и функция, задающая
выбор клавиатуры в зависимости от того, какая команда пришла
от пользователя (обработаны только команды с клавиатуры)
'''

keyboard_map = {
    'open_dialog_buttons': keyboard_begin(),
    'start_buttons': keyboard_start(),
    'about_buttons': keyboard_about(),
    'document_buttons': keyboard_document(),
    'consulting_buttons': keyboard_consulting()
}


def keyboard_choice(message_from_user):
    message = buttons_and_messages.answer_command(message_from_user)
    choice_key = str(list(message.keys())[0])
    return keyboard_map.get(choice_key, 'No such key in keyboard map')