from weakref import proxy
import RiotConsts as consts
import requests
class RiotAPI(object):
    def __init__(self, api_key, region=consts.REGIONS['north_america']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            consts.URL['base'].format(
                proxy=self.region,
                region=self.region,
                url=api_url
                ), 
            params=args
            )
        print(response.url)
        return response.json()
    
    def getSummonerByName(self, name):
        api_url = consts.URL['summonerByName'].format(
            version=consts.API_VERSIONS['summoner'],
            names=name
        )
        return self._request(api_url)