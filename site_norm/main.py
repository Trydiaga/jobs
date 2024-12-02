import psycopg2
import requests

# Параметры подключения к базе данных
hostname = 'localhost'
database = 'postgres'
username = 'postgres'
password = '12345'
port = '5432'  # По умолчанию используется порт 5432

try:
    # Установка соединения с базой данных
    connection = psycopg2.connect(
        host=hostname,
        database=database,
        user=username,
        password=password,
        port=port
    )
    
    # Создание курсора
    cursor = connection.cursor()
    
    # Пример выполнения запроса к базе данных
    cursor.execute("SELECT version();")
    
    # Получение результата
    db_version = cursor.fetchone()
    print("Database version:", db_version)

except Exception as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    # Закрытие курсора и соединения с базой данных
    if cursor:
        cursor.close()
    if connection:
        connection.close()

# Подключение к локальному веб-сайту
url = "http://localhost:5000"  # Замените на ваш локальный URL

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Successfully connected to the website. Response:")
        print(response.text) 
        raise GeneratorExit # Печатаем текст ответа
    else:
        print(f"Failed to connect to the website. Status code: {response.status_code}")

except Exception as e:
    print("Error while connecting to the website:", e)
