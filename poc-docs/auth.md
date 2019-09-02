# Authorization

Shit looks a bit complicated but it's supposed to make our lives easier when adding new updating keys, adding new services, disabling services.

Basically we have dynamic keys.
I wanted to encrypt them and there wasn't an easy way to do so so i did it my way.


I'll update this document when i get time but

# Adding new Service.


Two files are required

- The Auth Stuff about the service
located in /services/auth/services_auth
Organized in this manner


```python
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
```



- and the actual service object with the search_song and title stuff

```python
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
```

**having REF is extremely important and it will break if you don't have one**.

Bascially in a nutshell, the main spotify object inherits all the proper keys and inforamtion from the authorization module. 


Also this **must** be called from the same directory as ``api.py``. Python is so weird with
the relative imports, that it gave me a headache and i just said fuck it.