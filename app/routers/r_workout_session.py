from fastapi import APIRouter
from db import database_cursor
from models.m_workout_session import WorkoutSession
from datetime import datetime


router = APIRouter(prefix="/workout_session", tags=['Workout Session'])




@router.get("/fetch_all")
async def fetch_all_workout_session():
    sql_query = """
    SELECT *
    FROM workout_sessions
    """
    database_cursor.execute(sql_query)
    data = database_cursor.fetchall()
    response = [WorkoutSession(**{key: row[k] for k, key in enumerate(WorkoutSession.model_fields.keys())}) for row in data]
    return {"status": "SUCCESS", "data": response}



@router.post("/create")
async def create_workout_session(workout_history_id: int, workout_session_name: str, crt_date: str):
    
    sql_query = """
    INSERt INTO workout_sessions (workout_history_id, session_name, crt_date)
    VALUES (%s, %s, %s)
    """
    values = (workout_history_id, workout_session_name, crt_date)


    another_query = """
    update workout_histories set session_count = session_count + 1
    where workout_history_id = %s
    """

    value = (workout_history_id,)

    database_cursor.execute(sql_query, values)
    database_cursor.execute(another_query, value)

    return {"status": "SUCCESS"}


@router.delete("/delete")
async def delete_workout_session(workout_session_id: int):
    sql_query = """
    DELETE FROM workout_sessions
    WHERE session_id = %s
    """
    values = (workout_session_id,)
    database_cursor.execute(sql_query, values)
    return {"status": "SUCCESS"}