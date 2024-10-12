from sqlalchemy import null
from albumoftheyearapi import AOTY
import pytest, json, datetime

@pytest.mark.first
def test_initialize():
    c = AOTY()
    pytest.client = c
    assert pytest.client != null

def test_upcoming_albums_limit():
    albums_json = pytest.client.upcoming_releases_by_limit(62)
    albums = json.loads(albums_json)
    assert (len(albums['albums'])) == 62

def test_upcoming_albums_page():
    albums_json = pytest.client.upcoming_releases_by_page(3)
    albums = json.loads(albums_json)
    assert (len(albums['albums'])) == 60

def test_upcoming_albums_date():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow_month = tomorrow.month
    tomorrow_day = tomorrow.day
    albums_json = pytest.client.upcoming_releases_by_date(tomorrow_month, tomorrow_day)
    albums = json.loads(albums_json)
    assert len(albums['albums']) < 60

if __name__ == "__main__":
    pytest.main