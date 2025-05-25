from fastapi import FastAPI
from pydantic import BaseModel, Field
from langchain_utils import generate_schedule
from db import insert_values

app = FastAPI(
    title="SmartSched API",
    description="An API that returns personalized study schedules using an LLM",
    version="1.0.0"
)

class ScheduleRequest(BaseModel):
    mood: str = Field(..., description="Your current energy or mood level")
    study_time: str = Field(..., description="How many hours can you dedicate to studying today?")
    busyness: str = Field(..., description="How packed is your day?")
    learning_topic: str = Field(..., description="Comma-separated learning topics")
    daily_schedule: str = Field(..., description="A rough plan or to-do list for today")
    

from fastapi.responses import JSONResponse
from fastapi import status

@app.post("/generate-schedule/")
def get_schedule(req: ScheduleRequest):
    try:
        result = generate_schedule(
            mood=req.mood,
            study_time=req.study_time,
            busyness=req.busyness,
            learning_topic=req.learning_topic,
            daily_schedule=req.daily_schedule
        )

        # Save to DB
        insert_values(req.learning_topic, result["db_ready_schedule"])

        return {"plan": result["full_schedule"]}
    except Exception as e:
        print(f"Error generating schedule: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": "Failed to generate schedule. Please try again later."}
        )




