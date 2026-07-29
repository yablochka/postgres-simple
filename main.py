from fastapi import FastAPI
app = FastAPI()
import psycopg2

@app.get("/")
def get_home():
    return {"message": "Welcome to home page"}

try:
    conn = psycopg2.connect(
        host="sakura.proxy.rlwy.net:52174",
        port=5432,
        database="rooms",
        user="postgres",
        password="XUcHwwUHmaaFigVzOlpYIdrPZrGwpjKf"
    )

    print("✅ Connected to PostgreSQL!")

except Exception as e:
    print("❌ Connection failed!")
    print(e)
