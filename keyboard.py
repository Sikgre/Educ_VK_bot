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
    create_keyboard.add_button('Начать', color=colors("blue"))
    create_keyboard = create_keyboard.get_keyboard()
    return create_keyboard


def keyboard_begin():
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard.add_button(button["document"], color=colors("blue"))
    create_keyboard.add_button(button["consulting"], color=colors("green"))
    create_keyboard.add_line()
    create_keyboard.add_button(button["more"], color=colors("red"))
    create_keyboard = create_keyboard.get_keyboard()
    return create_keyboard


def keyboard_about():
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard.add_button(button["project"], color=colors("blue"))
    create_keyboard.add_button(button["conditions"], color=colors("white"))
    create_keyboard.add_line()
    create_keyboard.add_button(button["refs"], color=colors("green"))
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
    handlers.keyboard_answer['cancel']: keyboard_start,
    handlers.keyboard_answer['beginning']: keyboard_begin,
    handlers.keyboard_answer['more']: keyboard_about,
}


def keyboard_choice(send_message):
    return keyboard_map.get(send_message, keyboard_empty)
