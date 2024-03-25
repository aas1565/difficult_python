import logging

import task1_utils

logger=logging.getLogger('logger-app')

def configure_logging() -> None:
    formatter = logging.Formatter('%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    handler_info = logging.FileHandler('info_debug.txt', mode='a')
    handler_info.setLevel(logging.INFO)
    handler_info.setFormatter(formatter)

    handler_error = logging.FileHandler('error_debug.txt', mode='a')
    handler_error.setLevel(logging.ERROR)
    handler_error.setFormatter(formatter)

    logging.basicConfig(level=logging.INFO, handlers=[console_handler, handler_info, handler_error])

configure_logging()

def show_list_of_commands() -> None:
    logger.info("Доступные команды:\n"
          "\"+\" - сложение\n"
          "\"-\" - вычитание\n"
          "\"*\" - умножение\n"
          "\"/\" - деление\n"
          "\"^\" - возведение в степень\n")
    #print("Доступные команды:\n"
          #"\"+\" - сложение\n"
          #"\"-\" - вычитание\n"
          #"\"*\" - умножение\n"
          #"\"/\" - деление\n"
          #"\"^\" - возведение в степень\n")


def get_command_from_user() -> str:
    command: str = input("Введите выражение с пробелами: ")
    return command


def process_command(command: str) -> tuple[float, float, str] | None:
    command_split: [str] = command.split()
    if len(command_split) != 3:
        return None
    number_1 = float(command_split[0])
    number_2 = float(command_split[2])
    operation = command_split[1]
    return number_1, number_2, operation


def get_result(command: tuple[float, float, str] | None) -> str:
    if command is None:
        logger.error("Вы ввели не корректную строку, повторите попытку.")
        #return "Вы ввели не корректную строку, повторите попытку."
    number_1, number_2, operation = command
    result: float = task1_utils.calculate(number_1, number_2, operation)
    return str(result)


def give_result_to_user(result: str) -> None:
    print(result)


if __name__ == '__main__':
    show_list_of_commands()
    while True:
        command: str = get_command_from_user()
        processed_command = process_command(command)
        result: str = get_result(processed_command)
        give_result_to_user(result)