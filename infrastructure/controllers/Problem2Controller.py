from fastapi import APIRouter
from actions.Problem2Action import Problem2Action
from infrastructure.repositories.JarvisApiClient import JarvisApiClient


router = APIRouter()

# Define a GET endpoint to sove problem 2
@router.get(
    "/problem2",
    summary="Solve Problem 2: Send SQL Queries",
    description="""
This endpoint solves the second problem by sending a
list of three sql queries.
""", 
    tags=["Problems"],
    response_description="Validation response from JARVIS showing a message."
)
def solve_problem_2():
    repository = JarvisApiClient()
    action = Problem2Action(repository)
    return action.execute()