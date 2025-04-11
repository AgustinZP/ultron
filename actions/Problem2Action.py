from domain.repositories.JarvisClient import JarvisClient
from domain.services.SqlGeneratorService import SqlGeneratorService

class Problem2Action:
    def __init__(self, repository: JarvisClient):
        # Inject the repository
        self.repository = repository

    def execute(self):
        # Use the domain service to generate SQL queries
        solution = SqlGeneratorService().generate_SQL()
        # Send the solution to the API for validation
        response = self.repository.post_solution(2, solution)
        # Return the full result
        return {
            "solution": solution,
            "response": response
        }