from fastapi import APIRouter
from actions.Problem2Action import Problem2Action
from infrastructure.repositories.JarvisApiRepository import JarvisApiRepository


router = APIRouter()

# Define a GET endpoint to sove problem 2
@router.get("/problem2")
def solve_problem_2():
    repository = JarvisApiRepository()
    action = Problem2Action(repository)
    return action.execute()