from domain.repositories.JarvisClient import JarvisClient
from domain.services.GemSearchService import GemSearchService

class Problem1Action:
    def __init__(self, repository: JarvisClient):
        # Inject the repository
        self.repository = repository

    def execute(self):
        # Retrieve the matrix for problem 1 from JARVIS API
        data = self.repository.get_problem(1)
        matrix = data["matrix"]
        # Use the domain service to find all the gems
        solution = GemSearchService().find_gems(matrix)
        # Send the solution to the API for validation
        response = self.repository.post_solution(1, solution)
        # Return the full result
        return {
            "matrix": matrix,
            "solution": solution,
            "response": response
        }