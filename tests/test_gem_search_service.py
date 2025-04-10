from domain.services.GemSearchService import GemSearchService


def test_gem_search_service():
    matrix= [
        list("SPACEMIND"),
        list("REALITYXX"),
        list("XXXXXXXXX"),
        list("XXXXXXXXX"),
        list("XXXXXXXXX"),
        list("XXXXXXXXX"),
        list("XXXXXXXXX"),
    ]

    service = GemSearchService()
    result = service.find_gems(matrix)

    expected = ["SPACE","MIND","REALITY"]

    for gem in expected:
        assert gem in result