from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load CSV data
students = []

with open("q-fastapi.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        students.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })

@app.get("/api")
async def get_students(
    class_: list[str] | None = Query(default=None, alias="class")
):

    if class_:
        filtered = [
            s for s in students
            if s["class"] in class_
        ]
        return {"students": filtered}

    return {"students": students}