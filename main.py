from RiotAPI import RiotAPI

def main():
    api = RiotAPI('RGAPI-71b5db48-490e-42de-b196-49a5f7078b2e')
    r = api.getSummonerByName('ff15open')
    print(r)
if __name__ == "__main__":
    main()