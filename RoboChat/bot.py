import json
import random

from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.console import Console
from rich.traceback import install
from rich import print

install(show_locals=True)
con = Console()

def bot():
    json_file = open('bot.json')

    bot_data = json.load(json_file)

    
    while True:
        user_resp = input("Talk to the bot 🤖 : ")
        input_panel = Panel.fit(f"{user_resp}", border_style = "bold blue", title = "User", subtitle = "   ...   ")
        con.print(input_panel)
        
        if user_resp in bot_data['data']['welcomes']:

            WR = bot_data['data']['welcome_resp']

            welcome_responses = random.choice(WR)
            welcome_bot_resp = Panel.fit(f"{welcome_responses}", title = "✋🏻", subtitle = "   ...   ", border_style = "bold red")
            print(welcome_bot_resp)
            
        if user_resp in bot_data['data']['byes']:

            BR = bot_data['data']['bye_resp']

            bye_responses = random.choice(BR)
            bye_bot_resp = Panel.fit(f"{bye_responses}", title = " 🙋 ", subtitle = "   ...   ", border_style = "bold red")
            print(bye_bot_resp)
            exit()
            
        if user_resp in bot_data['data']["Hrw's"]:
            
            HR = bot_data['data']["Hrw's_resp"]
            
            Hrw_responses = random.choice(HR)
            Hrw_bot_resp = Panel.fit(f"{Hrw_responses}", title = "👌💻", subtitle = "  ...  ", border_style = "bold red")
            print(Hrw_bot_resp)
        
        if user_resp in bot_data['data']['Schedule_task']:
            schedule_date = input("Type the date you want me to remind you of in the DD/MM/YYYY order : " )
            schedule_name = input("What is the event : " )

            schedule_panel = Panel.fit(f"I'll remind you to {schedule_name} on {schedule_date}", title = "REMINDER", subtitle = "  ...  ", border_style = "bold red")
            print(schedule_panel)

            with open("tasks.txt", "a") as tk:
                tk.write(f"{schedule_date} {schedule_name}")

    
    json_file.close()


bot()
