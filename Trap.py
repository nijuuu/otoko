#Trap link generator
from lxml import html
import requests
from random import randint
import sys

#starts with link
link = "sorry, something REALLY went wrong with this code..."
url = "http://gelbooru.com/index.php?page=post&s=list&tags=trap";
if sys.argv[0] == "!trap":
    url += "+rating:questionable+rating:safe"

#look for random page or additional search term
if len(sys.argv) < 2:
    url += "&pid=" + str(randint(0, 14742))
else:
    for i in range(2, len(sys.argv)):
        url += "+" + sys.argv[i]

page = requests.get(url)
tree = html.fromstring(page.content)

#xpath search for the @href of a picture
links = tree.xpath('//a[@id]/@href')

if len(links) == 0:
    errmsg = ["S-sorry, I couldn't find anything!!!", "You're a fucking perv.",
              "There's! Nothing! Here!", "Look it up yourself, idiot.",
              "W-Why would you want to look at THAT?", "Can't you just look at ME?",
              "Please don't...", "I can't find EVERYTHING for you!",
              "Hmm... Can you try something else?", "Gross."]
    print(errmsg[randint(0, len(errmsg)-1)])
    exit()

link = "http://gelbooru.com/" + links[randint(0, len(links)-1)]

print(link)