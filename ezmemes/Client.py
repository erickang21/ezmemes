import aiohttp
import requests
import random
from box import Box

class MemeError(Exception):
    """
    Raised for any error while requesting memes.
    """
    pass


class Client:
    """
    Class object for the meme API.

    Params:
    -----------
    is_async: bool
        Whether to make the session async or not.
        Defaults to False.
    """

    def __init__(self, is_async=False):
        self.session = aiohttp.ClientSession() if is_async else requests.Session()
        self.is_async = is_async


    async def get_meme(self, limit=500, position=None):
        """
        Gets a meme from Reddit.
        
        Params:
        ------
        limit (int):
            How many posts to collect from Reddit. The greater this is, the longer it will take.

        position: (int)
            The position the meme shoudld be taken from. Defaults to a random position.
        """ 
        try:
            r = None
            if self.is_async:
                r = await self.session.get(f"https://api.reddit.com/u/kerdaloo/m/dankmemer/top/.json?sort=top&t=day&limit={str(limit)}")
            else:
                r = self.session.get(f"https://api.reddit.com/u/kerdaloo/m/dankmemer/top/.json?sort=top&t=day&limit={str(limit)}")
            r = await r.json()
            meme_pos = position or random.randint(0, len(r['data']['children']) - 1)
            meme = r['data']['children'][meme_pos]['data']
            meme_img = meme['preview']['images'][0]['source']['url']
            meme_title = meme['title']
            box_meme = {
                "image_url": meme_img,
                "url": meme_img,
                "title": meme_title,
                "name": meme_title,
                "thumbsup": meme['ups'],
                "thumbsdown": meme['downs'],
                "subreddit": meme['subreddit']
            } 
            return Box(box_meme)
        except Exception as e:
            raise MemeError(f"An unexpected error occurred:\n{type(e).__name__}: {e}")
        