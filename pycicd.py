from flask import Flask
from datetime import datetime

app = Flask(__name__)
now = datetime.now().strftime("%H:%M:%S")

# Комментарий был изменен!
@app.route("/")
def home():
    # Используем f-строку для вставки HTML/CSS
    return f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #cccccc; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
            .card {{ background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-align: center; border-top: 5px solid #28a745; }}
            h1 {{ color: #333; margin-bottom: 10px; }}
            .status {{ color: #28a745; font-weight: bold; font-size: 1.2rem; }}
            .time {{ color: #666; font-size: 0.9rem; margin-top: 15px; }}
            .badge {{ display: inline-block; padding: 5px 12px; background: #e8f5e9; color: #2e7d32; border-radius: 20px; font-size: 0.8rem; margin-top: 10px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Flask CI/CD App</h1>
            <div class="status">● Система активна</div>
            <div class="badge">Пример выполняющегося приложения с использованием микрофреймворка Flask</div>
            <div class="time">Последний старт: {now}</div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "up", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
