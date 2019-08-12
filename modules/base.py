import datetime


class Album(object):
    __slots__ = (
        "name",
        "track_list",
        "artist",
        "link",
        "release_date",
        "cover_url",
        "service",
    )

    def __init__(
        self, name, track_list, artist, link, release_date, cover_url, service
    ):
        self.name = name
        self.track_list = track_list
        self.artist = artist
        self.link = link
        self.release_date = release_date
        self.cover_url = cover_url
        self.service = service

    @property
    def to_dict(self):
        dictionary = {
            "name": self.name,
            "track_list": self.track_list,
            "artist": self.artist,
            "link": self.link,
            "cover_url": self.cover_url,
            "service": self.service,
        }

        if isinstance(self.release_date, datetime.datetime):
            dictionary["release_date"] = self.release_date.strftime("%B %-d, %Y")
        else:
            dictionary["release_date"] = str(self.release_date)

        return dictionary


class Song(object):
    __slots__ = (
        "name",
        "artist",
        "link",
        "cover_url",
        "release_date",
        "track_album",
        "service",
    )

    def __init__(
        self, name, artist, link, cover_url, release_date, track_album, service
    ):
        self.name = name
        self.artist = artist
        self.link = link
        self.cover_url = cover_url
        self.release_date = release_date
        self.track_album = track_album
        self.service = service

    @property
    def to_dict(self):
        dictionary = {
            "name": self.name,
            "track_album": self.track_album,
            "artist": self.artist,
            "link": self.link,
            "cover_url": self.cover_url,
            "service": self.service,
        }

        if isinstance(self.release_date, datetime.datetime):
            dictionary["release_date"] = self.release_date.strftime("%B %-d, %Y")
        else:
            dictionary["release_date"] = str(self.release_date)

        return dictionary


class Artist(object):
    __slots__ = (
        "first_name",
        "last_name",
        "biography",
        "date_birth",
        "latest_release",
        "home_town",
        "genre",
    )

    def __init__(
        self,
        first_name,
        last_name,
        biography,
        date_birth,
        latest_release,
        home_town,
        genre,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.biography = biography
        self.date_birth = date_birth
        self.latest_release = latest_release
        self.home_town = home_town
        self.genre = genre

    @property
    def to_dict(self):
        dictionary = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "biography": self.biography,
            "home_town": self.home_town,
            "genre": self.genre,
            "latest_release": self.latest_release,
        }

        if isinstance(self.date_birth, datetime.datetime):
            dictionary["date_of_birth"] = self.date_birth.strftime("%B %-d %Y")
        else:
            dictionary["date_of_birth"] = str(self.date_birth)

        return dictionary


class Band(object):
    __slots__ = (
        "band_name",
        "band_members",
        "biography",
        "home_town",
        "latest_release",
        "group_creation_date",
        "genre",
    )

    def __init__(
        self,
        band_name,
        band_members,
        biography,
        home_town,
        latest_release,
        group_creation_date,
        genre,
    ):
        self.band_name = band_name
        self.band_members = band_members
        self.biography = biography
        self.home_town = home_town
        self.latest_release = latest_release
        self.group_creation_date = group_creation_date
        self.genre = genre

    @property
    def to_dict(self):
        dictionary = {
            "band_name": self.band_name,
            "band_members": self.band_members,
            "biography": self.biography,
            "home_town": self.home_town,
            "latest_release": self.latest_release,
            "genre": self.genre,
        }
        if isinstance(self.group_creation_date, datetime.datetime):
            dictionary["group_creation_date"] = self.group_creation_date.strftime("%B %-d %Y")
        else:
            dictionary["group_creation_date"] = str(self.group_creation_date)
        return dictionary
