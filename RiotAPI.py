from pickle import TRUE
from weakref import proxy

from attr import define
import RiotConsts as consts
import requests
import random
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

    def requestKDA(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(consts.URL['base2'].format(url=api_url), params=args)
        print(response.url)
        return response.json()
    # summonerLevel = 147 (int), name = ff15open (string)
    def getSummonerID(self, name):
        response = self.getSummonerByName(name)
        try:
            return response['id']
        except: # response['status']['status_code'] == 404:
            return None
    def getSummonerPID(self, name):
        response = self.getSummonerByName(name)
        try:
            print(response['puuid'])
            return response['puuid']
        except: # response['status']['status_code'] == 404:
            return None 
    # tier = Gold, rank = I, leaguePoints = 51, wins = 56, losses = 50
    def getSummonerRank(self, name):
        response = self.getSummonerRankInfo(name)
        if(not response):
            return "Unranked"
        try:
            return response[0]
        except:
            return None
    def getTopChamps(self, name):
        response = self.getTopChampsHelper(name)
        responseTop5 = []
        try:
            for i in range(5):
                champ = str(response[i]['championId'])
                mpt = str(response[i]['championPoints'])
                responseTop5.append(consts.CHAMP_ID[champ][0])
                responseTop5.append(mpt)
            return responseTop5
        except:
            return None
    def getAllChamps(self, name):
        response = self.getTopChampsHelper(name)
        noChestChamps = []
        for i in response:
            if(not bool(i['chestGranted'])):
                champ = str(i['championId'])
                noChestChamps.append(consts.CHAMP_ID[champ][0] + ' ???')
            else:
                champ = str(i['championId'])
                noChestChamps.append(consts.CHAMP_ID[champ][0] + ' ???')
        # Python uses Timsort, which the best case time complexity is O(N)
        # Best case occurs when array elements are jumbled
        # Most of the time the best case will occur since it is very unlikely
        # A users most popular champions are in any particular order
        noChestChamps.sort()
        return noChestChamps

    def getRandomChampKey(self):
        lists = list(consts.CHAMP_ID)
        randoms = random.choice(lists)
        return randoms
    
    def getQuote(self, key):
        return consts.CHAMP_ID[key][1]

    def checkChamp(self, input, key):
        if(input == consts.CHAMP_ID[key][0]):
            return TRUE
    
    def getChamp(self, key):
        return consts.CHAMP_ID[key][0]

    # O(N^2), maybe improve?
    # def getKDA(self, name):
    #     kda = 0 # [[kills], [deaths], [assists]]
    #     index = 0
    #     pid = self.getSummonerPID(name)
    #     while index < 5:
    #         gameNum = 0
    #         gameID = self.getGameID(name)[index]
    #         game = self.getGame(gameID)
    #         while pid != game['metadata']['participants'][gameNum]:
    #             gameNum+=1
    #         kda += game['info']['participants'][gameNum]['challenges']['kda']
    #         index+=1
    #     return kda
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

    def getTopChampsHelper(self, name):
        iden = self.getSummonerID(name)
        api_url = consts.URL['topChamps'].format(
            id = iden
        )
        return self.request(api_url)

    def getRankImg(self, name):
        return consts.IMAGES[name]
    
    def getGameID(self, name):
        puid = self.getSummonerPID(name)
        api_url = consts.URL['kda'].format(
            pid = puid 
        )
        return self.requestKDA(api_url)

    def getGame(self, gameID):
        api_url = consts.URL['kdaCalc'].format(
            gameIden = gameID
        )
        return self.requestKDA(api_url)

    def formatChampsTop5(self, arr):
        str = ""
        for i in range(0, 10, 2):
            str+= arr[i] + ' (' + arr[i+1] + ' Mastery Points)\n'
        return str

    def formatChamps(self, arr, firstHalf):
        str = ""
        size = int(len(arr))
        if(firstHalf == 0):
            for i in range(int(size/2)):
                str+= arr[i] + '\n'
            return str
        elif (firstHalf == 1):
            for i in range(int(size/2), size):
                str+= arr[i] + '\n'
        return str

    


