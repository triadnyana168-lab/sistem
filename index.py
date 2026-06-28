from fastapi import FastAPI, Query, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from src.ApiCheckGames import ApiCheckGames

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

api_checker = ApiCheckGames(debug=True)

class CheckIDBody(BaseModel):
    type_name: str
    userId: str
    zoneId: Optional[str] = ""

@app.get("/api/check-id-game")
def check_id_game_get(type_name: str, userId: str, zoneId: Optional[str] = ""):
    return api_checker.validate_game_id(type_name, userId, zoneId)

@app.post("/api/check-id-game")
def check_id_game_post(data: CheckIDBody = Body(...)):
    return api_checker.validate_game_id(data.type_name, data.userId, data.zoneId)
