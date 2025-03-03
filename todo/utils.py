import time
import hashlib


def generate_pk():
    """
    Генерирует строковый первичный ключ на основе хэша текущего времени.
    (Ограничения: не используется UUID, random, стандартные функции Postgres или целочисленные автоинкременты.)
    """
    now = str(time.time())
    return hashlib.sha256(now.encode('utf-8')).hexdigest()[:16]