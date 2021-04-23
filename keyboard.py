from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import messages
from messages import steps
from messages import keyboard_command as button


def colors(col):
    color = {
        "green": VkKeyboardColor.POSITIVE,
        "red": VkKeyboardColor.NEGATIVE,
        "white": VkKeyboardColor.SECONDARY,
        "blue": VkKeyboardColor.PRIMARY
    }
    col_func = color.get(col)
    return col_func


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


def keyboard_cancel():
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard.add_button(button["cancel"], color=colors("red"))
    create_keyboard = create_keyboard.get_keyboard()
    return create_keyboard


def keyboard_empty():
    create_keyboard = VkKeyboard(one_time=True)
    create_keyboard = create_keyboard.get_empty_keyboard()
    return create_keyboard


steps_answers = []
for i in list(steps)[:-2]:
    for j in steps.get(i).values():
        steps_answers.append(j)


keyboard_map = {
    messages.keyboard_answer['cancel']: keyboard_start,
    messages.keyboard_answer['beginning']: keyboard_begin,
    messages.keyboard_answer['more']: keyboard_about,
}


def keyboard_choice(send_message):
    if send_message in steps_answers:
        return keyboard_cancel
    else:
        return keyboard_map.get(send_message, keyboard_empty)
