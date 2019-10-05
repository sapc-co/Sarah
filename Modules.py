# -*- coding: utf-8 -*-
""" 
This is the Modeles for the the main file of Sarah
#TODO: This Doctype needs changes
""" 

#imports :
from googletrans import Translator
from Data import *
from webbrowser import open_new_tab as ont
from bs4 import BeautifulSoup as bs
from emoji import emojize
import requests 
import wikipedia


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
        url = "https://247tpb.club/s/?q={}&page=0&orderby=99".format(asked)
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

class SWikipedia:
    def Wikipedia(Subject):
        return wikipedia.summary(Subject)
    
    def Compliter(Subject):
        return ("""Acording To Wikipedia,\n{}""".format(Subject))

    def GetURL(Subject):
        return wikipedia.page(Subject).url
        
class SEmoji():
    def Emoji(emoname):
        if emoname == "fuck":
            return emojize(":middle_finger:") #🖕
        elif emoname == "thumb":
            return emojize(":thumbs_up:") #👍
        elif emoname == "smile":
            return emojize(":slightly_smiling_face:") #🙂   
        elif emoname == "wink":
            return emojize(":winking_face:") #😉
        elif emoname == "sad":
            return emojize(":pensive_face:") #😔
        elif emoname == "heart":
            return emojize(":red_heart:") #💖
        elif emoname == "question":
            return emojize(":question_mark:") #❓
        elif emoname == "sleep":
            return emojize(":zzz:") #💤
        elif emoname == "sun":
            return emojize(":sun_with_face:") #🌞
        elif emoname == "RLcloud":
            return emojize(":cloud_with_lightning_and_rain:") #⛈
        elif emoname == "Rcloud":
            return emojize(":cloud_with_rain:") #🌧
        elif emoname == "Scloud":
            return emojize(":sun_behind_cloud:") #⛅
        elif emoname == "Lcloud":
            return emojize(":cloud_with_lightning:") #🌩
        elif emoname == "snow":
            return emojize(":snowflake:") #❄
        elif emoname == "thunder":
            return emojize(":high_voltage:") #⚡
        elif emoname == "v":
            return emojize(":victory_hand:") #✌️
