# ff15open: Basic League of Legends Discord Bot 
League of Legends Discord bot made using Python, Riot API and Discord API. WIP. Made by Sean Yoon.

# About
Simple bot based on the game League of Legends by Riot Games that can track basic statistics from any account. However, there are some limitations:
- The account must exist on NA servers (will update this soon)
- If the account is unranked, you will not get that much information

This bot was created using Python, the Discord API (discord.py), and the Riot API (accessed using requests library). Its main purpose was for me to refresh my memory on Python, as well as create something that anyone who plays League of Legends could use for their benefit. It was a fun learning experience!

# How it Works
There are 4 basic commands the bot can use:
- **!stats {name}**, which returns a bunch of statistics a player might find useful/interesting in a competitive context
![image](https://user-images.githubusercontent.com/92048016/167331357-73bbf095-67c9-4aad-a6f0-3710a283f5a0.png)
- **!chest {name}**, which returns which champions the user has gotten a Hextech Chest on for that Season (players know that we have too many keys but too little chests so this tool allows you to play the champions you need!)
![image](https://user-images.githubusercontent.com/92048016/167331519-4dda6b2c-681d-4c1f-88f1-2ef0a7729248.png)
- **!quote**, where the bot will give you a quote from a random champion for the user to guess
![image](https://user-images.githubusercontent.com/92048016/167333393-a2018fbb-bcbf-4a12-8043-fc91f5e90217.png)
- **!ping**, which returns your ping relative to the bot
![image](https://user-images.githubusercontent.com/92048016/167333407-4bd802f9-278d-4c16-806e-af13c6eb82ea.png)

# Technologies Used
[**Python 3.5**](https://www.python.org/downloads/release/python-350/) was the language used to code this entire bot.

[**Discord.py**](https://discordpy.readthedocs.io/en/stable/) was an API referenced to help with setting up the basic functionalities of the bot (backend).

[**Riot Games API**](https://developer.riotgames.com/) was an API referenced to help with finding League of Legends statistics that otherwise would not be possible to access.

[**Google Cloud**](https://cloud.google.com/) was used to host the website so I would not have to host it locally on my computer. This is done through a Linux VM instance in the Cloud environment.

# Want to Use This Bot?

The setup is pretty straightforward:

**1.** You first must clone or fork this repository

**2.** Install all dependencies using *npm install* or install *python3, discord.py, requests, and dotenv* using **pip3**

**3.** Create a Discord application using the [**Discord Developer Portal**](https://discord.com/developers/docs/intro) and create a new application. Click on the 
'bot' tab and copy the token.

**4.** Go to the [**Riot Developer Portal**](https://developer.riotgames.com/) and copy the 24hr API development key.

**5.** Create a **.env file** (environment variable) and paste the following properties into it (same directory as bot.py):

> DISCORD_TOKEN={yourDiscordToken}
> 
> DISCORD_GUILD={yourDiscordServerName}
> 
> RIOT_TOKEN={yourRiotToken}

  - Be sure to remove the squiggly brackets.
 
**6.** You're pretty much done! Just go back to the Discord Developer Portal, go to your bot, OAuth2, and then add it to your server (make sure you give your bot permissions)

