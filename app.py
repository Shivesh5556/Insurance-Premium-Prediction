from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from schema.user_input import UserInput
from Model.predict import predict_premium

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

@app.post("/predict")
def predict(data: UserInput):
    prediction = predict_premium({
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    })

    return JSONResponse(content={"predicted_category": prediction}, status_code=200)

static_dir = BASE_DIR / "static"
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
def health():
    return {"status": "ok"}
