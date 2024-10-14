import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class Album:
    def __init__(self, name, artist, date):
        self.name = name
        self.artist = artist
        self.release_date = date

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=0)


class AlbumMethods:
    def __init__(self):
        self.upcoming_album_class = "albumBlock five small"
        self.aoty_albums_per_page = 60
        self.page_limit = 21

    def upcoming_releases_by_limit(self, total):
        min_page_number = 1
        max_page_number = total // self.aoty_albums_per_page
        if total % self.aoty_albums_per_page != 0:
            max_page_number += 1
        upcoming_albums = {}
        albums = []
        counter = total
        for page_number in range(min_page_number, max_page_number + 1):
            try:
                if counter < self.aoty_albums_per_page:
                    albums += self._get_upcoming_releases_by_page(page_number)[:counter]
                else:
                    albums += self._get_upcoming_releases_by_page(page_number)
                    counter -= self.aoty_albums_per_page
            except Exception as e:
                return json.dumps(
                    self._build_error_response(
                        "Page Limit Error",
                        "Number of albums exceeded page limit. Exception raise: ." + e,
                    )
                )
        json_albums = [album.to_JSON() for album in albums]
        upcoming_albums["albums"] = json_albums
        return json.dumps(upcoming_albums)

    def upcoming_releases_by_page(self, page_number):
        upcoming_albums = {}
        try:
            parsed_albums = self._get_upcoming_releases_by_page(page_number)
        except:
            return json.dumps(
                self._build_error_response(
                    "Page Limit Error", "The page number requested is out of range."
                )
            )
        json_albums = [album.to_JSON() for album in parsed_albums]
        upcoming_albums["albums"] = json_albums
        return json.dumps(upcoming_albums)

    def upcoming_releases_by_date(self, month, day):
        upcoming_albums = {}
        try:
            parsed_albums = self._get_upcoming_releases_by_date(month, day)
        except Exception as e:
            return json.dumps(
                self._build_error_response("Releases by date Error: ", e.message)
            )
        json_albums = [album.to_JSON() for album in parsed_albums]
        upcoming_albums["albums"] = json_albums
        return json.dumps(upcoming_albums)

    def _get_upcoming_releases_by_date(self, month, day):
        month_name = self._map_month_number_to_name(month)
        target_date = (month_name + " " + str(day)).strip()
        next_date = (month_name + " " + str(day + 1)).strip()
        page_number = 1
        result_albums = []

        complete = False
        while not complete:
            albums = self._get_upcoming_releases_by_page(page_number)
            for album in albums:
                if album.release_date == target_date:
                    result_albums.append(album)

                if album.release_date == next_date:
                    complete = True
            page_number += 1
        return result_albums

    def _build_error_response(self, error_type, msg):
        error_dict = {"error": error_type, "message": msg}
        return error_dict

    def _map_month_number_to_name(self, month_number):
        month_names = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
        try:
            return month_names[month_number - 1]
        except:
            raise Exception("Invalid month number")

    def _get_upcoming_releases_by_page(self, page_number):
        if page_number > self.page_limit:
            raise Exception("Page number out of range")
        if int(page_number) == 1:
            page_number = ""
        url = "https://www.albumoftheyear.org/upcoming/" + str(page_number) + "/"
        page = self._get_release_page_from_request(url)
        albums = page.find_all("div", {"class": self.upcoming_album_class})
        parsed_albums = self._parse_albums(albums)
        return parsed_albums

    def _get_release_page_from_request(self, url):
        request = Request(url, headers={"User-Agent": "Mozilla/6.0"})
        unparsed_page = urlopen(request).read()
        release_page = BeautifulSoup(unparsed_page, "html.parser")
        return release_page

    def _parse_albums(self, unparsed_albums):
        parsed_albums = []
        for album in unparsed_albums:
            artist = str(album.find("div", {"class": "artistTitle"}).getText())
            title = str(album.find("div", {"class": "albumTitle"}).getText())
            date = str(album.find("div", {"class": "type"}).getText())
            parsed_albums.append(Album(title, artist, date))
        return parsed_albums
