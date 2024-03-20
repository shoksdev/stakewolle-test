# API Реферальной системы

### 🎯Цель

Необходимо разработать простой RESTful API сервис для реферальной системы.

---

### 📝Description

**Функциональные требования:**  
1) Регистрация и аутентификация пользователя (JWT, Oauth 2.0);
2) Аутентифицированный пользователь должен иметь возможность создать или удалить свой реферальный код. Одновременно может быть активен только 1 код. При создании кода обязательно должен быть задан его срок годности;
3) Возможность получения реферального кода по email адресу реферера;
4) Возможность регистрации по реферальному коду в качестве реферала;	
5) Получение информации о рефералах по id реферера;
6) UI документация (Swagger/ReDoc).

---

### 🛠Стек

**Языки**: Python;  
**Фреймворки**: Django, Django REST Framework;  
**Библиотеки**: djoser, psycopg2, python-dotenv, drf-yasg, simpleJWT, OAuth 2.0;  
**База данных**: PostgreSQL;  
**Инструменты**: Docker, docker-compose, Git.

---

### ⚙Установка используя Docker

---

1) **Клонируйте репозиторий**: `git clone https://github.com/shoksdev/stakewolle-test.git`  
2) **Перейдите в проект**: `cd referal`  
3) **Создайте .env файл в папке `referal` с переменными**: 
SECRET_KEY (секретный ключ приложения)  
SOCIAL_AUTH_VK_OAUTH2_KEY (ID приложения в VK API)  
SOCIAL_AUTH_VK_OAUTH2_SECRET (секретный ключ приложения в VK API)  
SQL_ENGINE (движок SQL)  
POSTGRES_DB (название базы данных)  
POSTGRES_USER (имя пользователя базы данных)  
POSTGRES_PASSWORD (пароль пользователя базы данных)  
POSTGRES_HOST (хост базы данных)  
POSTGRES_PORT (порт базы данных)  
4) **Запустите проект с созданием суперпользователя**: `docker-compose run django python manage.py createsuperuser`  
5) **Поднимите проект**: `docker-compose up`  

### ⚙Установка без Docker

---

1) **Клонируйте репозиторий**: `git clone https://github.com/shoksdev/stakewolle-test.git`  
2) **Перейдите в проект**: `cd referal`  
3) **Установите зависимости**: `pip install -r requirements.txt`  
4) **Создайте базу данных в PgAdmin**: можете воспользоваться видео https://www.youtube.com/watch?v=h5wgbJiSy7Q;
5) **Создайте .env файл в папке `referal` с переменными**: 
SECRET_KEY (секретный ключ приложения)  
SOCIAL_AUTH_VK_OAUTH2_KEY (ID приложения в VK API)  
SOCIAL_AUTH_VK_OAUTH2_SECRET (секретный ключ приложения в VK API)  
SQL_ENGINE (движок SQL)  
POSTGRES_DB (название базы данных)  
POSTGRES_USER (имя пользователя базы данных)  
POSTGRES_PASSWORD (пароль пользователя базы данных)  
POSTGRES_HOST (хост базы данных)  
POSTGRES_PORT (порт базы данных)  
6) **Создайте суперпользователя**: `python manage.py createsuperuser`
7) **Выполните миграции**: `python manage.py migrate`  
8) **Запустите проект**: `python manage.py runserver`  

---

### 📙Инструкция по тестированию

1) Отправьте POST запрос по адресу http://127.0.0.1:8000/auth/users/ с параметрами `username`, `email` и `password` для регистрации;
2) Запомните токен из шага №1;
3) Отправьте POST запрос по адресу http://127.0.0.1:8000/create/referral/code/ и введите параметры `referral_code_title` и `referral_code_due_date` для добавления реферального кода пользователю;
4) Отправьте DELETE запрос по адресу http://127.0.0.1:8000/delete/referral/code/<int:pk>/ и в качестве pk передайте ID пользователя для удаления реферального кода;
5) Отправьте GET запрос по адресу http://127.0.0.1:8000/get/referral/code/<str:email>/ и в качестве email передайте email реферера для получения реферального кода;
6) Отправьте GET запрос по адресу http://127.0.0.1:8000/get/referrals/list/<int:referrer_id>/ и в качестве referrer_id передайте ID реферера для получения информации обо всех рефералах;

**ИЛИ**

**Перейдите по адресу http://127.0.0.1:8000/swagger/ и используйте его для тестирования API**

---

#### Большое спасибо за возможность продемонстрировать свои навыки. Буду рад любой обратной связи. Всего доброго!
