import hashlib
import time
import random


def generate_unique_id():
    """
    Генерирует уникальный первичный ключ, используя текущее время и
    случайное число.
    Возвращает SHA-256 хэш от объединенной строки.
    """
    unique_string = f"{time.time()}{random.randint(1000, 9999)}"
    return hashlib.sha256(unique_string.encode()).hexdigest()
