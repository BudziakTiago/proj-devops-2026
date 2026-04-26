from fastapi.testclient import TestClient
from unittest.mock import patch
from src.main import *

@patch("requests.get")
def test_getUserStatistics(mock_get):
    mock_get.return_value.json.return_value = {
        "anime_statistics": {
            "num_items_watching": 5
        }
    }

    assert getUserStatistics() == 5

@patch("src.main.getUserStatistics")
@patch("requests.get")
def test_getUserAnimeList(mock_get, mock_stats):
    mock_stats.return_value = 2

    mock_get.return_value.json.return_value = {
        "data": ["anime1", "anime2"]
    }

    result = getUserAnimeList()
    assert result == ["anime1", "anime2"]

@patch("requests.get")
def test_getAnimeDetails(mock_get):
    mock_get.return_value.json.return_value = {
        "genres": [{"name": "Adventure"}],
        "alternative_titles": {"ja": "Dr.STONE SCIENCE FUTURE 第3クール", "en": "Dr. Stone: Science Future Part 3"}
    }

    url = "https://api.myanimelist.net/v2/anime/62568"
    result = getAnimeDetails(url)

    assert "genres" in result
    assert "alternative_titles" in result

client = TestClient(app)

@patch("src.main.getUserAnimeList")
@patch("src.main.getAnimeDetails")
def test_root(mock_details, mock_list):
    mock_list.return_value = [
        {
            "node": {
                "id": 62568,
                "my_list_status": {
                    "score": 7,
                    "status": "watching"
                }
            }
        }
    ]

    mock_details.return_value = {
        "genres": [{"name": "Adventure"}],
        "alternative_titles": {"ja": "Dr.STONE SCIENCE FUTURE 第3クール", "en": "Dr. Stone: Science Future Part 3"}
    }

    response = client.get("/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)