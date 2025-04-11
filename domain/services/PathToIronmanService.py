class PathToIronmanService:
    WIND = "Viento en contra"
    RAIN = "Lluvia"
    STORM ="Tormenta"

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
        if weather == self.WIND:
            return 1.5
        elif weather == self.RAIN:
            return 0.2
        elif weather == self.STORM:
            return 2.0
        return 0.0
    
    def find_path(self) -> tuple[list[str], float]:
        # This is the starting city to go to the destination
        current_location = self._get_satellite_by_location("New York")

        # If New York is not found return an empty path and full fuel
        if not current_location:
            return [], self.fuel

        to_explore = [(
            current_location,
            [current_location["location"]],
            self.fuel,
            {current_location["id"]}
        )]

        valid_paths = []

        # Loop until destinations available to explore
        while to_explore:
            current_location, path, fuel, visited = to_explore.pop()

            if current_location["location"] == self.destination:
                valid_paths.append((path, fuel))
                continue

            neighbours = current_location["nearest_sats"]
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
                if fuel - cost >= 0:
                    candidates.append((candidate, cost))
            # We check which neighbour has the minimum cost and we choose this one
            for candidate, cost in candidates:
                # We add the new location to the path
                new_path = path + [candidate["location"]]
                new_visited = visited.copy()
                # Mark this satellite as visited
                new_visited.add(candidate["id"])
                to_explore.append((candidate, new_path, fuel - cost, new_visited))
        
        if not valid_paths:
            return [], self.fuel
        
        # We check which candidate has the minimum cost and we choose this one
        self.path, self.fuel = max(valid_paths, key=lambda x: x[1])
        return self.path, round(self.fuel, 2)