# Домовенок – сайт аренды квартир

![Django](https://img.shields.io/badge/Django-4.2-green)
![Python](https://img.shields.io/badge/Python-3.12.8-blue)

## 📌 О проекте
Проект доступен по ссылке https://domovenok.onrender.com

Веб-приложение для аренды жилья с возможностью размещения объявлений, поиска и бронирования квартир.

## ✨ Возможности
- Для арендаторов
  - 🔍 Поиск квартир с фильтрами
  - 📅 Система бронирования
  - ⏰ Просмотр истории просмотров
  - 📝 Добавление квитанций об оплате различных услуг

- Для владельцев
  - ➕ Публикация объявлений
  - ✏️ Редактирование предложений
  - 💰 просмотр статистиски заработка

- Общие
  - 👤 Личные кабинеты
  - ⚙️ Настройки использования

## 🛠️ Технологии
- Backend: Django 4.2, Django REST Framework
- Frontend: JS, CSS,HTML
- База данных: SQLite

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.12.8
- SQLite (опционально)

### Установка
```bash
# 1. Клонировать репозиторий
git clone https://gitlab.informatics.ru/2024-2025/mytischi/s103/yandex/house-checker.git
cd house-checker

# 2. Настроить виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# или venv\Scripts\activate  # Windows

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Миграции
python manage.py migrate

# 5. Создать админа
python manage.py createsuperuser

# 6. Запустить сервер
python manage.py runserver