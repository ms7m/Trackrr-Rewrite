

#rom modules.services.spotify import Spotify

class Service:
    NAME = 'Spotify'
    SID = 'cc.trackrr.service.spotify'
    DESCRIPTION = 'Spotify provides access to millions of music formats in an instant for viewing and listening.'

    CLIENT_AUTHENTICATION_TYPE = 0
    CLIENT_ID = "872f5f400897446ab5e029708794732e"
    CLIENT_SECRET = "b0b3a452d8064bc4bd877fea6a330fe3" 

    PERMITTED_ACTIONS = [
        'song_search',
        'album_search',
        'add_to_playlist'
    ]

    CORE = "modules.services.spotify"
    CORE_SUB = "Spotify"