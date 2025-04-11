from domain.repositories.JarvisClient import JarvisClient
from domain.services.PathToIronmanService import PathToIronmanService

class Problem3Action:
    def __init__(self, repository: JarvisClient):
        # Inject the repository
        self.repository = repository

    def execute(self):
        # Retrieve satellites for problem 3
        satellites = self.repository.get_problem(3)["satellites"]
        # Get current location of Ironman to set the destination target
        destination = self.repository.get_where_is_ironman()["ironman_location"]

        # Use the domain service to calculate the path and remaining fuel
        service = PathToIronmanService(satellites, destination)
        path, final_fuel = service.find_path()

        # Check if we successfully arrived the destination and we have enough fuel
        if path and path[-1] == destination and final_fuel >= 30:
            # Send the solution to the API for validation
            response = self.repository.post_solution(3, {
                "solution": path,
                "final_fuel": final_fuel
            })

            # Return the full result
            return {
                "ironman_location": destination,
                "response": response
            }
        
        else:
            # If no valid path or insuficient fuel return error
            return {
                "error": "Didn´t find a valid path or not enough fuel.",
                "ironman_location": destination,
                "route": path,
                "final_fuel": final_fuel
            }