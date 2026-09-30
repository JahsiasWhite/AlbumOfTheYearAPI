"""Overall highest-rated album rankings from albumoftheyear.org."""

import json
import datetime
from bs4 import BeautifulSoup

from albumoftheyearapi.http import fetch_html


class RatingsMethods:
    """Methods for getting overall highest-rated album rankings from albumoftheyear.org."""

    def __init__(self):
        self._ratings_page_url = ""
        self._ratings_page = None

    def __set_ratings_page(self, url):
        self._ratings_page_url = url
        ugly_page = fetch_html(url)
        self._ratings_page = BeautifulSoup(ugly_page, "html.parser")

    def __ensure_ratings_page(self, url):
        if self._ratings_page_url != url or self._ratings_page is None:
            self.__set_ratings_page(url)

    def __parse_albums(self):
        albums = []
        for row in self._ratings_page.find_all("div", class_="albumListRow"):
            rank_span = row.find("span", itemprop="position")
            rank = rank_span.getText().strip() if rank_span else None

            name_meta = row.find("meta", itemprop="name")
            name = name_meta["content"] if name_meta else None

            date_div = row.find("div", class_="albumListDate")
            date = date_div.getText().strip() if date_div else None

            score_div = row.find("div", class_="scoreValue")
            score = int(score_div.getText().strip()) if score_div else None

            score_text_div = row.find("div", class_="scoreText")
            review_count = int(score_text_div.getText().split()[0]) if score_text_div else None

            albums.append({
                "rank": rank,
                "name": name,
                "date": date,
                "score": score,
                "review_count": review_count,
            })
        return albums

    def top_albums_by_year(self, year=None):
        """Return the highest critic-rated albums for a given year.

        Fetches the critic rankings from https://www.albumoftheyear.org/ratings/6-highest-rated/{year}/1

        Args:
            year (int or str, optional): A 4-digit year (e.g. 2026), a decade
                (e.g. "2020s"), "all" for all-time rankings, or None to use
                the current calendar year.

        Returns:
            list[dict]: Each dict contains:
                - rank (str): Chart position, e.g. "1".
                - name (str): "Artist - Album" as shown on the site.
                - date (str): Release date, e.g. "February 13, 2026".
                - score (int or None): Critic score, e.g. 87.
                - review_count (int or None): Number of critic reviews, e.g. 11.
        """
        if year is None:
            year = datetime.date.today().year
        url = f"https://www.albumoftheyear.org/ratings/6-highest-rated/{year}/1"
        self.__ensure_ratings_page(url)
        return self.__parse_albums()

    def top_albums_by_year_json(self, year=None):
        """Return top_albums_by_year as a JSON string under the key "albums".

        Args:
            year (int or str, optional): Same as top_albums_by_year.

        Returns:
            str: JSON string with a single key "albums" containing the list.
        """
        return json.dumps({"albums": self.top_albums_by_year(year)})
