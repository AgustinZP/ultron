from fastapi import FastAPI
from infrastructure.controllers import Problem1Controller, Problem2Controller, Problem3Controller

app = FastAPI(title = "Ultron API")

app.include_router(Problem1Controller.router)
app.include_router(Problem2Controller.router)
app.include_router(Problem3Controller.router)