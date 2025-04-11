from fastapi import APIRouter
from actions.Problem3Action import Problem3Action
from infrastructure.repositories.JarvisApiClient import JarvisApiClient


router = APIRouter()

# Define a GET endpoint to sove problem 3
@router.get("/problem3",
    summary="Solve Problem 3: Find the path to Ironman",
    description="""
This endpoint solves the third problem by retrieving 
a list of satellites and the current location of Ironman. It calculates
a valid path from New York to Ironman using the available satellite
connections and taking weather penalties.

The goal is to reach Ironman with at least 30 units of fuel remaining.
""", 
    tags=["Problems"],
    response_description="Route taken, final fuel and validation response from JARVIS."
)
def solve_problem_3():
    repository = JarvisApiClient()
    action = Problem3Action(repository)
    return action.execute()