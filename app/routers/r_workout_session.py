from fastapi import APIRouter
from db import database_cursor
from models.m_workout_history import WorkoutHistory


router = APIRouter(prefix="/workout_session", tags=['Workout Session'])





