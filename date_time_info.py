from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Получение текущей даты и времени
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # Отображение даты и времени на главной странице
    return f"<h1>Текущая дата и время:</h1><p>{current_time}</p>"

if __name__ == '__main__':
    app.run()
