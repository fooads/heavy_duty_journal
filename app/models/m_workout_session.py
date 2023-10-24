from pydantic import BaseModel
from datetime import date


class WorkoutSession(BaseModel):
    session_id: int
    workout_history_id: int
    session_name: str
    crt_date: date