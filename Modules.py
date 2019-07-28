""" 
    This is the Modeles for the the main file of Sarah
    This Doctype needs changes
""" 

#imports :
from googletrans import Translator
from Data import *
from webbrowser import open_new_tab as ont
import requests 
from bs4 import BeautifulSoup as bs
from emoji import emojize


class STranslator():

    def Translate(Content, Dest) :
        translator = Translator()
        try :
            translations = translator.translate([Content], src="auto", dest=Dest)
            for translation in translations :
                if Dest == "fa" or Dest == "ar" :           
                    return (translation.origin + " -> " + translation.text[::-1])
                else :
                    return (translation.origin + " -> " + translation.text)
        except :
            return ("Ooops connection failed \nMaybe you need to check your network connection") 


class SWebscraper():

    def Piratebay(asked):
        url = "https://247tpb.club/s/?q="+asked+"&page=0&orderby=99"
        try :
            page = requests.get(url) #Downloading That url's main html page
            page = page.content #extracting
            soup = bs(page, "html.parser") #making a valid html code
            link = soup.find(class_="detLink") #finding the first link

            if link != None :
                href = link['href']
                url = "https://247tpb.club"+href
                page = requests.get(url)
                page = page.content
                soup = bs(page, 'html.parser')
                div = soup.find('div', class_="download")
                links  = div.find_all('a')
                global magnet
                magnet = links[0]['href']
                global stream
                stream = links[1]['href']
                return magnet
            else :
                return ("Coudn't find it in Pirate Bay")
        
        except :
            return ("Ooops connection failed \nMaybe you need to check your network connection")

    def Wikipedia(subject, language):
        pass


class SEmoji():
    def Emoji(emoname):
        if emoname == "fuck":
            return emojize(":middle_finger:")
        elif emoname == "thumb":
            return emojize(":+1:")
        elif emoname == "smile":
            return emojize(":simple_smile:")        
        elif emoname == "wink":
            return emojize(":wink:")        
        elif emoname == "sad":
            return emojize(":pensive:")        
        elif emoname == "heart":
            return emojize(":heart:")        
        elif emoname == "question":
            return emojize(":questino:")        
        elif emoname == "sleep":
            return emojize(":zzz:")
        elif emoname == "sun":
            return emojize(":sunny:")   
        elif emoname == "cloud":
            return emojize(":cloud:")   
        elif emoname == "snow":
            return emojize(":snowflake:")
        elif emoname == "thunder":
            return emojize(":zap:")
        

