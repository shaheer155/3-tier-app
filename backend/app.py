from flask import Flask
import psycopg2
from flask_cors import CORS  # ✅ new line

app = Flask(__name__)
CORS(app)  # ✅ new line

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(
            host="db",
            database="mydb",
            user="postgres",
            password="postgres"
        )
        return "✅ Backend connected successfully to the database!"
    except Exception as e:
        return f"❌ Database connection failed: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

