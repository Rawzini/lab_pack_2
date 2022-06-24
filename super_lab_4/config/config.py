import os
# Переносим секретный ключ в конфиги, начинаем генерировать его случайным образом (чтобы нельзя было подобрать)
SECRET_KEY = os.urandom(32)
# Сохраняем в переменную basedir папку, в которой лежит наш сервис
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

photos_subpath = '/static/storage'

photosdir = basedir + photos_subpath
# Активируем debug-mode
DEBUG = True
# Строка подключения к бд sqlite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
# Отключаем нотификации об изменениях, т.к. мы не будем это использовать
SQLALCHEMY_TRACK_MODIFICATIONS = False