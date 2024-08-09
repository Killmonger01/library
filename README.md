# library
# Как запустить локально
После клонирования репозитория создайте и активируйте вертуальное окружение
```
python -m venv venv
source venv/Scripts/activate
```
Установите зависимости
```
python -m pip install --upgrade pip # если нужно обновить pip
pip install -r requirements.txt 
```
Перейдите в директерию с файлом manage.py
```
cd library/ 
```
Сделайте миграции
```
python manage.py makemigrations
python manage.py migrate
```
Запустите сервер
```
python manage.py runserver
```