from fastapi import FastAPI
import psycopg2
app = FastAPI()

@app.get("/")
def get_home():
    return {"message": "Welcome to home page"}

connect = psycopg2.connect(
    host="sakura.proxy.rlwy.net",
    port=5432,
    database="rooms",
    user="postgres",
    password="XUcHwwUHmaaFigVzOlpYIdrPZrGwpjKf"
)

cursor = connect.cursor()

@app.get("/rooms")
def get_rooms():
    cursor.execute("SELECT * FROM rooms")
    rows = cursor.fetchall()    
    return rows
