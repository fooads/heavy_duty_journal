from fastapi import FastAPI
from routers import r_workout_history


app = FastAPI(
    title="Heavy Duty API",
    version="0.1.0",
    docs_url="/docs"
)

app.include_router(r_workout_history.router)


@app.get("/")
async def root():
    return {"message":"Hello World"}