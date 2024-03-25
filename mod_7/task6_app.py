import logging
from logging.config import dictConfig

import logging_tree
import task1_utils

logger=logging.getLogger('logger-app')

# Define a custom formatter
class CustomFormatter(logging.Formatter):
    def format(self, record):
        return f"{record.levelname} - {record.name} - {record.message}"

# Redirect stdout to a file
with open('logging_tree.txt', 'w') as file:
    import sys
    sys.stdout = file

    # Get the root logger
    root_logger = logging.getLogger()

    # Configure default loggers
    logging.basicConfig(level=logging.DEBUG)

    # Set the custom formatter for the root logger
    root_logger.handlers[0].setFormatter(CustomFormatter())

    # Print the tree structure of loggers with the custom format
    logging_tree.printout()

    # Reset stdout back to normal
    sys.stdout = sys.__stdout__

# Update logging configuration to include a file handler
def configure_logging() -> None:
    dictConfig({
        'version': 1,
        'handlers': {
            'file_handler': {
                'class': 'logging.FileHandler',
                'filename': 'logging_tree.txt',
                'formatter': 'custom_formatter'
            }
        },
        'loggers': {
            '': {
                'handlers': ['file_handler'],
                'level': 'DEBUG'
            }
        },
        'formatters': {
            'custom_formatter': {
                'format': '%(levelname)s - %(name)s - %(message)s'
            }
        }
    })

configure_logging()


def show_list_of_commands() -> None:
    logger.info("Доступные команды:\n"
          "\"+\" - сложение\n"
          "\"-\" - вычитание\n"
          "\"*\" - умножение\n"
          "\"/\" - деление\n"
          "\"^\" - возведение в степень\n")



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