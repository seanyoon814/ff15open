from RiotAPI import RiotAPI

def main():
    api = RiotAPI('')
    r = api.getSummonerByName('ff15open')
    print(r)
if __name__ == "__main__":
    main()
