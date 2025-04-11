import requests
from domain.repositories.JarvisClient import JarvisClient
from infrastructure.config.settings import CANDIDATE_KEY, BASE_URL

class JarvisApiClient(JarvisClient):
    # HTTP headers with the candidate key used for atuhentication
    headers = {
        "candidate-key": CANDIDATE_KEY
    }

    # Get the problem by its ID from JARVIS API
    def get_problem(self, problemId: int):
        response = requests.get(f"{BASE_URL}/problem/{problemId}", headers=self.headers)
        return response.json()

    # Sends the solution of a problem to JARVIS API
    def post_solution(self, problemId: int, solution: dict):
        response = requests.post(f"{BASE_URL}/problem/solution/{problemId}", headers=self.headers, json={"solution": solution})
        return response.json()

    # Get the current location of Ironman from JARVIS API
    def get_where_is_ironman(self):
        response = requests.get(f"{BASE_URL}/where_is_ironman", headers=self.headers)
        return response.json()