import os
# Переносим секретный ключ в конфиги, начинаем генерировать его случайным образом (чтобы нельзя было подобрать)
SECRET_KEY = os.urandom(32)
# Сохраняем в переменную basedir папку, в которой лежит наш сервис
basedir = os.path.abspath(os.path.dirname(__file__))
# Активируем debug-mode
DEBUG = True