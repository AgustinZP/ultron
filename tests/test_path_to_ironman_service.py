from domain.services.PathToIronmanService import PathToIronmanService

def test_path_to_ironman_service():
    satellites = [  
        {
            "id": 1,
            "location": "New York",
            "weather": "Despejado",
            "nearest_sats": [2]
        },
        {
            "id": 2,
            "location": "Paris",
            "weather": "Tormenta",
            "nearest_sats": [1,3]
        },
        {
            "id": 3,
            "location": "Moscow",
            "weather": "Lluvia",
            "nearest_sats": [2]
        }
 ]
    
    service = PathToIronmanService(satellites, destination="Moscow")
    path, fuel = service.find_path()

    assert path[-1] == "Moscow"

    assert fuel < 100

    assert "New York" in path
    assert "Paris" in path
    assert "Moscow" in path

    assert fuel >= 30

