from actions.Problem2Action import Problem2Action

class MockRepository:
    def post_solution(self, problemId: int, solution: dict):
        return {"response": "SQLs submitted successfully"}
    
def test_problem2_action():
    action = Problem2Action(MockRepository())
    result = action.execute()

    assert isinstance(result["solution"], list)
    assert len(result["solution"]) == 3

    for sql in result["solution"]:
        assert isinstance(sql, str)

    assert result["response"]["response"] == "SQLs submitted successfully"