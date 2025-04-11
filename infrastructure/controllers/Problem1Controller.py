from fastapi import APIRouter
from actions.Problem1Action import Problem1Action
from infrastructure.repositories.JarvisApiClient import JarvisApiClient

router = APIRouter()

# Define a GET endpoint to sove problem 1
@router.get(
    "/problem1",
    summary="Solve Problem 1: Find Gems",
    description="""
This endpoint solves the first problem by retrieving 
a matrix of characters and detecting which gems are hidden within.
""", 
    tags=["Problems"],
    response_description="Matrix, found gems and validation response from JARVIS."
)
def solve_problem_1():
    repository = JarvisApiClient()
    action = Problem1Action(repository)
    return action.execute()