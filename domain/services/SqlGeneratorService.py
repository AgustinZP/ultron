class SqlGeneratorService:

    # Returns a list of strings, in this case sql queries
    def generate_SQL(self) -> list[str]:
        # Get the name of the current location of the Avengers
        sql_1 = (
            "SELECT l.name" \
            "FROM avenger a" \
            "JOIN location l ON a.current_location_id = l.id"
        )

        # Get the locations where an avenger has been more than three times
        sql_2 = (
            "SELECT l.name" \
            "FROM location l" \
            "JOIN avenger_location_log log ON l.id = log.location_id" \
            "GROUP BY l.name" \
            "HAVING COUNT(DISTINCT log.avenger_id) > 3"
        )

        # Modify stark_satellite table setting in_maintenance = TRUE where satellite location is the same that an avenger location
        sql_3 = (
            "UPDATE stark_satellite" \
            "SET in_maintenance = TRUE" \
            "WHERE location_id IN(" \
            "SELECT current_location_id FROM avenger)"
        )

        return [sql_1, sql_2, sql_3]