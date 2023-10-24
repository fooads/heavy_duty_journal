from fastapi import APIRouter
from db import database_cursor
from models.m_workout_history import WorkoutHistory


router = APIRouter(prefix="/workout_history", tags=['Workout History'])


@router.get("/fetch_all")
async def fetch_all_workout_history():
    sql_query = """
    SELECT *
    FROM workout_histories
    """
    database_cursor.execute(sql_query)
    data = database_cursor.fetchall()
    response = [WorkoutHistory(**{key: row[k] for k, key in enumerate(WorkoutHistory.model_fields.keys())}) for row in data]
    return {"status": "SUCCESS", "data": response}


@router.post("/create")
async def create_workout_history(workout_history_name: str):
    sql_query = """
    INSERt INTO workout_histories (workout_history_name, session_count)
    VALUES (%s, 0)
    """
    values = (workout_history_name,)
    database_cursor.execute(sql_query, values)
    return {"status": "SUCCESS"}


@router.delete("/delete")
async def delete_workout_history(workout_history_id: int):
    sql_query = """
    DELETE FROM workout_histories
    WHERE workout_history_id = %s
    """
    values = (workout_history_id,)
    database_cursor.execute(sql_query, values)
    return {"status": "SUCCESS"}

