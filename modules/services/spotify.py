import modules.base as base
#import modules.keys as keys
import requests

NAME = 'Spotify'
SID = 'cc.trackrr.service.spotify'
DESCRIPTION = 'Spotify provides access to millions of music formats in an instant for viewing and listening.'

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
