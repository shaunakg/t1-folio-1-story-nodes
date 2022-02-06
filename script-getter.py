
from bs4 import BeautifulSoup
import requests

script_links = [
    "https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_Philosopher%27s_Stone/Transcript",
    "https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_Chamber_of_Secrets/Transcript",
    "https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_Prisoner_of_Azkaban/Transcript",
    "https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_Goblet_of_Fire/Transcript",
    "https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_Order_of_the_Phoenix/Transcript",
    "https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_Half-Blood_Prince/Transcript",
    "https://warnerbros.fandom.com/wiki/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2/Transcript"
]

script = ""

for i in script_links:
    print("Getting script from: " + i)

    page = BeautifulSoup(requests.get(i).content, 'html.parser')
    script += page.find('div', {'class': 'mw-parser-output'}).getText() + "\n"

with open('hp-script.txt', 'w') as f:
    f.write(script)