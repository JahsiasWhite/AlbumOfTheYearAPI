"""Genre album rankings from albumoftheyear.org."""

import json
import datetime
from bs4 import BeautifulSoup

from albumoftheyearapi.http import fetch_html


# Maps friendly genre names to their URL slugs.
# Accepts either a key from this map (e.g. "rock") or a raw slug (e.g. "7-rock").
GENRE_MAP = {
    "indie rock":           "1-indie-rock",
    "electronic":                 "6-electronic",
    "rock":                 "7-rock",
    "pop":                  "15-pop",
    "metal":               "40-metal",
}


class GenreMethods:
    """Methods for getting genre album rankings from albumoftheyear.org."""

    def __init__(self):
        self.genre_page_url = ""
        self.genre_page = None
        self.genre_base_url = "https://www.albumoftheyear.org/genre/"

    def __resolve_genre(self, genre):
        """Return the URL slug for genre, accepting friendly names or raw slugs."""
        return GENRE_MAP.get(genre.lower(), genre)

    def __build_url(self, genre, year=None):
        if year is None:
            year = datetime.date.today().year
        return f"{self.genre_base_url}{genre}/{year}/"

    def __set_genre_page(self, url):
        self.genre_page_url = url
        ugly_page = fetch_html(url)
        self.genre_page = BeautifulSoup(ugly_page, "html.parser")

    def __ensure_genre_page(self, url):
        if self.genre_page_url != url or self.genre_page is None:
            self.__set_genre_page(url)

    def __parse_albums(self):
        albums = []
        for row in self.genre_page.find_all("div", class_="albumListRow"):
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

    def genre_albums(self, genre, year=None):
        """Return the critic-ranked album list for a genre and time period.

        genre can be a friendly name ("rock") or a raw slug ("7-rock").
        year can be a 4-digit year, decade ("2020s"), "all", or None for the current year.
        Each album dict has: rank (str), name (str), date (str), score (int|None), review_count (int|None).
        """
        slug = self.__resolve_genre(genre)
        url = self.__build_url(slug, year)
        self.__ensure_genre_page(url)
        return self.__parse_albums()

    def genre_albums_json(self, genre, year=None):
        """Return genre_albums as a JSON string."""
        return json.dumps({"albums": self.genre_albums(genre, year)})
