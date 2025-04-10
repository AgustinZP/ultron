class PathToIronmanService:
    def __init__(self, satellites: list, destination: str):
        self.satellites = satellites
        self.destination = destination
        self.fuel = 100
        self.path = []

    # returns a satellite by its location name
    def _get_satellite_by_location(self, location: str):
        for sat in self.satellites:
            if sat["location"] == location:
                return sat
        return None
    
    # returns a satellite by its ID
    def _get_satellite_by_id(self, sat_id):
        for sat in self.satellites:
            if sat["id"] == sat_id:
                return sat
        return None
    
    # Returns additional fuel cost based on weather conditions
    def _get_weather_penalty(self, weather):
        if weather == "Viento en contra":
            return 1.5
        elif weather == "Lluvia":
            return 0.2
        elif weather == "Tormenta":
            return 2.0
        return 0.0
    

    def find_path(self) -> tuple[list[str], float]:
        # This is the starting city to go to the destination
        current_location = self._get_satellite_by_location("New York")

        # If New York is not found return an empty path and full fuel
        if not current_location:
            return [], self.fuel
        
        visited=set()
        self.path.append(current_location["location"])
        visited.add(current_location["id"])

        # Loop until destination is reached
        while current_location["location"] != self.destination:
            neighbours = current_location["nearest_sats"]

            next_neighbour = None

            candidates = []

            for neighbour_id in neighbours:
                if neighbour_id in visited:
                    continue
                
                candidate = self._get_satellite_by_id(neighbour_id)

                if not candidate:
                    continue
                
                # Calculate total fuel cost to reach this neighbour
                cost = 10 + self._get_weather_penalty(candidate["weather"])

                # If we have enough fuel, we added as a valid candidate
                if self.fuel - cost >= 0:
                    candidates.append((candidate, cost))

            if candidates:
                # We check which neighbour has the minimum cost and we choose this one
                next_neighbour, cost = min(candidates, key=lambda x: x[1])
                self.fuel -= cost
                self.path.append(next_neighbour["location"])
                visited.add(next_neighbour["id"])
                current_location = next_neighbour
            else:
                break

        return self.path, round(self.fuel, 2)
