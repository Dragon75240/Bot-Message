from discordwebhook import *
webhookurlin = input('Webhook URL : ')
webhookurl = webhookurlin
discord = Discord(url=webhookurl)
title = input("Title : ")
description = input("Description : ")
BotName = input("Bot Name : ")
Avatar = input("Avatar URL : ")
Field1Name = input("Field 1 name : ")
Field1Text = input("Field 1 Text : ")
InlineCheck = bool("Inline, True or False : ")
discord.post(
    username=BotName,
    avatar_url=Avatar,
    embeds=[
        {
            "username": BotName,
            "title": title,
            "description": description,
            "fields": [
                {"name": Field1Name, "Value": Field1Text, "inline": InlineCheck}
            ],
        }
    ],
)