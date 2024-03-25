import logging
import math
logger=logging.getLogger('logger-utils')

def calculate(a: float, b: float, operation: str) -> float:
    match operation:
        case "+":
            return _addition(a, b)
        case "-":
            return _subtraction(a, b)
        case "*":
            return _multiplication(a, b)
        case "/":
            return _division(a, b)
        case "^":
            return _pow(a, b)


def _addition(a: float, b: float) -> float:
    logger.info('сложение')
    result: float = a + b
    return result


def _subtraction(a: float, b: float) -> float:
    logger.info('вычитание')
    result: float = a - b
    return result


def _multiplication(a: float, b: float) -> float:
    logger.info('умножение')
    result: float = a * b
    return result


def _division(a: float, b: float) -> float:
    logger.info('деление')
    result: float = a / b
    return result


def _pow(a: float, b: float) -> float:
    logger.info('возведение в степень')
    result: float = math.pow(a, b)
    return result