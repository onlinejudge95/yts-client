import json

import requests


class YTSClient:
    def __init__(self, host):
        self.base_url = f"https://{host}/api/v2"
        self.movies = MoviesClient(self.base_url)

    def __str__(self):
        return f"<YTSClient dispatching to {self.base_url}>"


class MoviesClient:
    rule_book = {"limit": "in range(1, 51)"}

    def __init__(self, base_url):
        self.endpoint = "/list_movies.json"
        self.url = base_url + self.endpoint
        self.payload = dict()

    def all(
        self,
        limit=20,
        page=1,
        quality="All",
        minimum_rating=0,
        query_term="0",
        genre="All",
        sort_by="date_added",
        order_by="desc",
        with_rt_ratings=False,
    ):
        if not isinstance(limit, int):
            raise ValueError("limit should be an integer")
        elif not limit in range(1, 51):
            raise ValueError("limit should be in [1,..,50]")
        else:
            self.payload["limit"] = limit

        if not isinstance(page, int):
            raise ValueError("page should be an integer")
        elif not page > 0:
            raise ValueError("page should be a positive number")
        else:
            self.payload["page"] = page

        if not isinstance(quality, str):
            raise ValueError("quality should be a string")
        elif not quality in ["720p", "1080p", "2160p", "3D", "All"]:
            raise ValueError(
                "quality should be in ['720p', '1080p', '2160p', '3D', 'All']"
            )
        else:
            self.payload["quality"] = quality

        if not isinstance(minimum_rating, int):
            raise ValueError("minimum_rating should be an integer")
        elif not page > 0:
            raise ValueError("minimum_rating should be in [0,..,9]")
        else:
            self.payload["minimum_rating"] = minimum_rating

        if not isinstance(query_term, str):
            raise ValueError("query_term should be a string")
        else:
            self.payload["query_term"] = query_term

        if not isinstance(genre, str):
            raise ValueError("genre should be a string")
        else:
            self.payload["genre"] = genre

        if not isinstance(sort_by, str):
            raise ValueError("sort_by should be a string")
        elif not sort_by in [
            "title",
            "year",
            "rating",
            "peers",
            "seeds",
            "download_count",
            "like_count",
            "date_added",
        ]:
            raise ValueError(
                "sort_by should be in ['title', 'year', 'rating', 'peers', 'seeds', 'download_count', 'like_count', 'date_added']"
            )
        else:
            self.payload["sort_by"] = sort_by

        if not isinstance(order_by, str):
            raise ValueError("order_by should be a string")
        elif not order_by in ["asc", "desc"]:
            raise ValueError("order_by should be in ['asc', 'desc']")
        else:
            self.payload["order_by"] = order_by

        if not isinstance(with_rt_ratings, bool):
            raise ValueError("with_rt_ratings should be a boolean")
        else:
            self.payload["with_rt_ratings"] = with_rt_ratings

        response = requests.get(self.url, params=self.payload)

        data = json.loads(response.content)

        if data["status"] == "ok":
            return data["data"].get("movies")

        return data["status_message"]
