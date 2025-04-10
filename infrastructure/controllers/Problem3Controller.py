from fastapi import APIRouter
from actions.Problem3Action import Problem3Action
from infrastructure.repositories.JarvisApiRepository import JarvisApiRepository


router = APIRouter()

# Define a GET endpoint to sove problem 3
@router.get("/problem3")
def solve_problem_3():
    repository = JarvisApiRepository()
    action = Problem3Action(repository)
    return action.execute()