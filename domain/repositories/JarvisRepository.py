from abc import ABC, abstractmethod

# Abstract class that defines the interface for accessing JARVIS API
class JarvisRepository(ABC):

    @abstractmethod
    def get_problem(self, problemId: int) -> dict:
        pass

    @abstractmethod
    def post_solution(self, problemId: int, solution: dict) -> dict:
        pass

    @abstractmethod
    def get_where_is_ironman(self) -> dict:
        pass