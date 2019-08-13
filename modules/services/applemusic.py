import modules.base as base
#import modules.keys as keys
import requests

NAME = 'Apple Music'
SID = 'cc.trackrr.service.apple'
DESCRIPTION = 'Apple Music is Apple\'s answer to music streaming, providing high quality music information and media for its subscribers.'

def search_song(title: str):
    return base.Song(
        'Example Song',
        'Duck Corps',
        'https://apple.com/',
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
        'https://apple.com/',
        'Christmas 9',
        'https://viktorkoves.com/apollo/album-art-placeholder.png',
        SID
    )
