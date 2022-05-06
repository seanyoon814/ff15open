from weakref import proxy
import RiotConsts as consts
import requests
class RiotAPI(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(consts.URL['base'].format(url=api_url), params=args)
        print(response.url)
        return response.json()
    
    def getSummonerByName(self, name):
        api_url = consts.URL['summonerByName'].format(
            names=name
        )
        return self.request(api_url)
    
    # summonerLevel = 147 (int), name = ff15open (string)
    def getSummonerID(self, name):
        response = self.getSummonerByName(name)
        try:
            return response['id']
        except: # response['status']['status_code'] == 404:
            return None
    # tier = Gold, rank = I, leaguePoints = 51, wins = 56, losses = 50
    def getSummonerRank(self, name):
        response = self.getSummonerRankInfo(name)
        try:
            return response[0]
        except:
            return None
    
    # Helper Functions
    def getSummonerByName(self, name):
        api_url = consts.URL['summonerByName'].format(
            names=name
        )
        return self.request(api_url)
    
    def getSummonerRankInfo(self, name):
        iden = self.getSummonerID(name)
        api_url = consts.URL['rankStats'].format(
            id = iden
        )
        return self.request(api_url)

