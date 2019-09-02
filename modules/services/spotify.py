

#from modules.services.auth.services_auth.spotify import Service as SpotifyService
from modules.base import Album, Song
from loguru import logger

class Spotify(object):
    def __init__(self, auth_obj):
        logger.info('method called.')
        logger.info(auth_obj.CLIENT_SECRET)

        def search_song(title: str):
            return base.Song(
                'Example Song',
                'Duck Corps',
                'https://spotify.com/',
                'https://viktorkoves.com/apollo/album-art-placeholder.png',
                'Christmas 9',
                'Example Album',
                SID
            )

        def search_album(title: str):
            return base.Album(
                'Example Album',
                [
                    'Feel The Love',
                    'Fire',
                    '4th Dimension',
                    'Freeee',
                    'Reborn',
                    'Kids See Ghosts',
                    'Cudi Montage'
                ],
                'Duck Corps',
                'https://spotify.com/',
                'Christmas 9',
                'https://viktorkoves.com/apollo/album-art-placeholder.png',
                SID
            )


class Ref:
    main_obj = Spotify
