from discordwebhook import *
webhookurlin = input('Webhook URL : ')
webhookurl = webhookurlin
discord = Discord(url=webhookurl)
title = input("Title : ")
description = input("Description : ")
BotName = input("Bot Name : ")
Avatar = input("Avatar URL : ")
discord.post(
    username=BotName,
    avatar_url=Avatar,
    embeds=[
        {
            "username": BotName,
            "title": title,
            "description": description,
        }
    ],
)
