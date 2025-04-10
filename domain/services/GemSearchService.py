class GemSearchService:
    # List of gems to look for in the matrix
    gems = ["SPACE", "MIND", "REALITY", "TIME", "POWER", "SOUL"]

    def find_gems(self, matrix):
        # Set to store found gems  
        found_gems = set()
        # Size of the matrix
        n = len(matrix)
        
        # Convert a list of chars in a single string
        rows = ["".join(row) for row in matrix]
        cols = ["".join([matrix[i][j] for i in range (n)]) for j in range(n)]

        # Search all gems in rows and columns
        for gem in self.gems:
            for line in rows + cols:
                # Check if gem is present in normal or reversed direction
                if gem in line or gem in line[::-1]:
                    found_gems.add(gem)
                    break
        
        return list(found_gems)