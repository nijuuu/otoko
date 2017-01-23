#Pun Generator
from lxml import html
import requests
import random


#Returns whether or not the program should try again
def joke():
    #go into celebs page
    page = requests.get('http://people.com/celebrities/')
    tree = html.fromstring(page.content)
    celebrities = tree.xpath('//a[@id]/text()')
    if len(celebrities) == 0:
        return False
    
    #single celebrity
    fullName = celebrities[random.randint(0, len(celebrities)-1)]
    
    #broken up names
    names = fullName.split()
    index = random.randint(0, len(names)-1)
    name = names[index]
    del names[index]
    
    #go into rhyming dictionary
    rhymeURL = "http://www.rhymezone.com/r/rhyme.cgi?Word=" + name + "&typeofrhyme=perfect"
    page = requests.get(rhymeURL)
    tree = html.fromstring(page.content)
    rhymes = tree.xpath('//a[@class]/text()')
    if len(rhymes) == 0:
        return True
    
    #plug rhyme into name
    rhyme = rhymes[random.randint(0, len(rhymes)-1)]
    if len(rhyme) <= 2:
        return True
    
    #format the rhyme
    if len(rhyme.split()) > 1:
        rhyme = rhyme[-1]
    rhyme = rhyme.capitalize()
    names.insert(index, rhyme)
    
    #go into dictionary
    dictURL = "http://www.thefreedictionary.com/" + rhyme
    page = requests.get(dictURL)
    tree = html.fromstring(page.content)
    definition = tree.xpath('//*[@id="Definition"]/section[1]/div[1]/div[1]/text()')
    if len(definition) < 2 or \
        (definition[0].find("symbol") != -1) or \
        (definition[0].find("plural") != -1) or \
        (definition[0].find("variant") != -1):
        return True
    
    #format output
    out = "What would you call it if "
    for i in fullName:
        out += i
        
    out += " were"
    definition[0] = definition[0].lower()
    definition[-1] = definition[-1][:-1]
    for i in definition:
        out += i
    
    out += "?\n\t"
    
    for i in names:
        out += i + " "
    
    print(out)
    return False

while True:
    
    go = True
    response = input("Enter for more, exit to exit")
    if response == "exit":
        break
    else:
        while go:
            go = joke()