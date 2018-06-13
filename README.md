# ezmemes

A wrapper in Python designed to give memes in a hassle-free way.
High-quality meme APIs aren't easy to find, so this will grab memes from Reddit through the Reddit API.

It can be used in both Sync (Requests) and Asnyc (Aiohttp).

**Getting Started**
Run this on your command prompt:
`pip install git+https://github.com/bananaboy21/ezmemes`
(PyPi coming soon)

**Updating to new versions**
Run this on your command prompt:
`pip install -U https://github.com/bananaboy21/ezmemes`

**Example Usage**
```py
import ezmemes

memey_stuff_of_life = ezmemes.Client(is_async=True)

await memey_stuff_of_life.get_meme()
```

**Endpoints**
`async def get_meme(self, limit=500, position=None)`
Gets a meme from Reddit.

Params:
limit (int):
    How many posts to collect from Reddit. The greater this is, the longer it will take
position: (int)
    The position the meme shoudld be taken from. Defaults to a random position.

Return type: dict

__Attributes__
(one|two used to represent two different attribute names with the same function, or an alias.)
image_url | url (str): The URL of the image.
title | name (str): The title of the image. Great for a short descriptive text of your meme.
thumbsup (int): The number of thumbs up that the meme got on Reddit.
thumbsdown (int): The number of thumbs down that the meme got on Reddit.
subreddit (str): THe subreddit that the meme came from.
