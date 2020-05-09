# -*- coding: utf-8 -*-
""" 
This is the Modeles for the the main file of Sarah
#TODO: This Doctype needs changes
""" 

#Packages and Libraries :
import sys, 
import os
import time
import requests
import wikipedia
###
from googletrans import Translator
from Data import *
from Setting import *
from webbrowser import open_new_tab as ont
from bs4 import BeautifulSoup as bs
from emoji import emojize
from gtts import gTTS
from playsound import playsound

class STranslator():
    def Translate(Content, Dest) :
        translator = Translator()
        try :
            translations = translator.translate([Content], src="auto", dest=Dest)
            for translation in translations :
                return [0, translation.origin, translation.text]
                #("{}, will be, {}").format(translation.origin, translation.text)
        except(ValueError) :
            return ("Ooops, Couldn't recognize that language")
        except :
            return ("Ooops, Connection failed \nMaybe you need to check your network connection") 


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
<<<<<<< HEAD


class Stts():
    def say(txt):
        if SpeakingAbbility == "on" :
            try :
                tts = gTTS(text=txt, lang='en')
                tts.save("good.mp3")
                playsound('good.mp3')
            except :
                print("Ooops connection failed \nWhen you're offline, You can't hear my voice")
        elif SpeakingAbbility == "off" :
            pass
        else : 
            pass

    def write(txt): #Slow Typing function
        if WritingAbbility == "on" :
            """for Char in txt + '\n':
                sys.stdout.write(Char)
                sys.stdout.flush()
                time.sleep(0.09)"""
            print(txt)
        elif WritingAbbility == "off" :
            pass
        else : 
            pass


def sayandwrite(txt):
    Stts.say(txt)
    Stts.write(txt)

class SShorter(): #TODO coplete this class
    def Short(url):
        return(url)

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
