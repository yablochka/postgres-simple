import os

from fastapi import FastAPI, HTTPException
import psycopg2

app = FastAPI()

DATABASE_URL = os.environ.get("DATABASE_URL")


def get_connection():
    if not DATABASE_URL:
        raise HTTPException(
            status_code=500,
            detail="DATABASE_URL environment variable is not set",
        )
    return psycopg2.connect(DATABASE_URL)


@app.get("/")
def get_home():
    return {"message": "Welcome to home page"}


@app.get("/rooms")
def get_rooms():
    try:
        conn = get_connection()
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Database connection failed: {e}")

    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM rooms;")
                columns = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
                rooms = [dict(zip(columns, row)) for row in rows]
        return {"rooms": rooms}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch rooms: {e}")
    finally:
        conn.close()
