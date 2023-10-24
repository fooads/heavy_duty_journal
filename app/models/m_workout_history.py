from pydantic import BaseModel


class WorkoutHistory(BaseModel):
    workout_history_id: int
    workout_history_name: str
    workout_history_session_count: int