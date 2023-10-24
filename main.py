from fastapi import FastAPI
from db import database_cursor
from pydantic import BaseModel


app = FastAPI(
    title="Heavy Duty API",
    version="0.1.0",
    docs_url="/docs"
)


class WorkoutHistory(BaseModel):
    workout_history_id: int
    workout_history_name: str
    workout_history_session_count: int



@app.get("/")
async def root():
    return {"message":"Hello World"}


@app.get("/fetch_all")
async def fetch():
    sql_query = """
    SELECT *
    FROM students
    """
    database_cursor.execute(sql_query)
    students_data = database_cursor.fetchall()
    row = students_data[0]

    # students = [Student(**student) for student in students_data]
    return students_data


@app.get("/workout_history/fetch_all")
async def fetch_all_workout_history():
    sql_query = """
    SELECT *
    FROM workout_histories
    """
    database_cursor.execute(sql_query)
    data = database_cursor.fetchall()
    response = [WorkoutHistory(**{key: row[k] for k, key in enumerate(WorkoutHistory.model_fields.keys())}) for row in data]
    return {"status": "SUCCESS", "data": response}


@app.post("/workout_history/create")
async def create_workout_history(workout_history_name: str):
    sql_query = """
    INSERt INTO workout_histories (workout_history_name, session_count)
    VALUES (%s, 0)
    """
    values = (workout_history_name,)
    database_cursor.execute(sql_query, values)
    return {"status": "SUCCESS"}


@app.delete("/workout_history/delete")
async def delete_workout_history(workout_history_id: int):
    sql_query = """
    DELETE FROM workout_histories
    WHERE workout_history_id = %s
    """
    values = (workout_history_id,)
    database_cursor.execute(sql_query, values)
    return {"status": "SUCCESS"}

