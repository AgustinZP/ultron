from actions.Problem1Action import Problem1Action

class MockRepository:
    def get_problem(self, problemId: int):
        return {
            "matrix": [
                list("SPACEMIND"),
                list("REALITYXX"),
                list("PXXXXXXXX"),
                list("OXXXXXXXX"),
                list("WXXXXXXXX"),
                list("EXXXXXXXX"),
                list("RXXXXXXXX"),
            ]
        }

    def post_solution(self, problemId: int, solution: dict):
        return {"response": "Success"}

def test_problem1_action():
    action = Problem1Action(MockRepository())
    result = action.execute()

    assert "solution" in result

    expected = ["SPACE", "MIND", "REALITY", "POWER"]
    for gem in expected:
        assert gem in result["solution"]
        
    assert result["response"]["response"] == "Success"