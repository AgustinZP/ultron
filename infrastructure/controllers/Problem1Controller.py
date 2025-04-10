from fastapi import APIRouter
from actions.Problem1Action import Problem1Action
from infrastructure.repositories.JarvisApiRepository import JarvisApiRepository

router = APIRouter()

# Define a GET endpoint to sove problem 1
@router.get("/problem1")
def solve_problem_1():
    repository = JarvisApiRepository()
    action = Problem1Action(repository)
    return action.execute()