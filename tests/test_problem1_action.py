from actions.Problem1Action import Problem1Action

class MockRepository:
    def get_problem(self, problemId: int):
        return {
            "matrix": [
                list("SPACEMIND"),
                list("REALITYXX"),
                list("XXXXXXXXX"),
                list("XXXXXXXXX"),
                list("XXXXXXXXX"),
                list("XXXXXXXXX"),
                list("XXXXXXXXX"),
            ]
        }

    def post_solution(self, problemId: int, solution: dict):
        return {"response": "Success"}

def test_problem1_action():
    action = Problem1Action(MockRepository())
    result = action.execute()

    assert "solution" in result
    assert set(result["solution"]).issubset(["SPACE", "MIND", "REALITY", "TIME", "POWER", "SOUL"])
    assert result["response"]["response"] == "Success"