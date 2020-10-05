"""
Реалізуйте інтерфей асоційованого масиву, ключами якого є цілі числа, а значеннями - рядки.
"""
from HashTables.Linear_probing.Realization import *

table = HashTable()

def init():
    """ Викликається 1 раз на початку виконання програми. """

    pass


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """

    table[key] = value


def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
    """

    return table[key]

def delete(key: int) -> None:
    """ Видаляє пару ключ-значення за заданим ключем.
    Якщо ключ у структурі відсутній - нічого не робить.
    :param key: Ключ
    """
    table.delete(key)
