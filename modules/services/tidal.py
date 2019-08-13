import modules.base as base
#import modules.keys as keys
import requests

NAME = 'Tidal'
SID = 'cc.trackrr.service.tidal'
DESCRIPTION = 'Tidal is Jay-Z\'s premium streaming service built around providing the highest quality of audio and video.'

def search_song(title: str):
    return base.Song(
        'Example Song',
        'Duck Corps',
        'https://tidal.com/',
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
        'https://tidal.com/',
        'Christmas 9',
        'https://viktorkoves.com/apollo/album-art-placeholder.png',
        SID
    )
