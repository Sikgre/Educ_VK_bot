from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import handlers
from handlers import keyboard_command as button

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


def keyboard_start():
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard.add_button('Начать', color=colors("red"))
    create_keyboard = create_keyboard.get_keyboard()
    return create_keyboard


def keyboard_begin():
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard.add_button(button["document"], color=colors("red"))
    create_keyboard.add_button(button["consulting"], color=colors("white"))
    create_keyboard.add_line()
    create_keyboard.add_button(button["more"], color=colors("green"))
    create_keyboard = create_keyboard.get_keyboard()
    return create_keyboard


def keyboard_back():
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard.add_button(button["back"], color=colors("blue"))
    create_keyboard = create_keyboard.get_keyboard()
    return create_keyboard


def keyboard_about():
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard.add_button(button["project"], color=colors("red"))
    create_keyboard.add_button(button["conditions"], color=colors("white"))
    create_keyboard.add_line()
    create_keyboard.add_button(button["refs"], color=colors("green"))
    create_keyboard.add_line()
    create_keyboard.add_button(button["back"], color=colors("blue"))
    create_keyboard = create_keyboard.get_keyboard()
    return create_keyboard


def keyboard_document():
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard.add_button(button["contract_type"], color=colors("red"))
    create_keyboard.add_button(button["trust_type"], color=colors("white"))
    create_keyboard.add_line()
    create_keyboard.add_button(button["declaration_type"], color=colors("green"))
    create_keyboard.add_button(button["more"], color=colors("blue"))
    create_keyboard.add_line()
    create_keyboard.add_button(button["back"], color=colors("blue"))
    create_keyboard = create_keyboard.get_keyboard()
    return create_keyboard


def keyboard_consulting():
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard.add_button(button["labor_law"], color=colors("red"))
    create_keyboard.add_button(button["private_law"], color=colors("white"))
    create_keyboard.add_line()
    create_keyboard.add_button(button["other"], color=colors("green"))
    create_keyboard.add_line()
    create_keyboard.add_button(button["more"], color=colors("blue"))
    create_keyboard.add_line()
    create_keyboard.add_button(button["back"], color=colors("blue"))
    create_keyboard = create_keyboard.get_keyboard()
    return create_keyboard


def keyboard_empty():
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard = create_keyboard.get_empty_keyboard()
    return create_keyboard


'''
Словарь функций для клавиатур и функция, задающая
выбор клавиатуры в зависимости от того, какая команда пришла
от пользователя (обработаны только команды с клавиатуры)
'''

keyboard_map = {
    handlers.keyboard_command['start']: keyboard_start,
    handlers.keyboard_command['beginning']: keyboard_begin,
    handlers.keyboard_command['more']: keyboard_about,
    handlers.keyboard_command['document']: keyboard_document,
    handlers.keyboard_command['consulting']: keyboard_consulting
}


def keyboard_choice(message_from_user):
    return keyboard_map.get(message_from_user, keyboard_empty)
