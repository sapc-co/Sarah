# -*- coding: utf-8 -*-
""" 
This is the Main file of Sarah
#TODO: This Doctype needs changes
""" 

#Packages and Libraries :
import re 
from Modules import STranslator, SWebscraper, SEmoji, SWikipedia, Stts, sayandwrite
from Data import IntroOptions, langs, YES
from Setting import *
#---
from random import choice
from webbrowser import open_new_tab as ont


intro = choice(IntroOptions)
intro_emoji = ["wink", "smile"]
_emoji = SEmoji.Emoji(choice(intro_emoji)) #making a random emoji
intro2 = ("{} {}".format(intro, _emoji))
#Stts.say(intro), Stts.write(intro2)
#Stts.say(intro)
Stts.write(intro2)

try :
    while True:
        inp = input(Prompt)
        if inp is "" : # if the entered value was empty i'll pass
            pass #passing
        #---
        elif (inp[0:9] == "TRANSLATE") or (inp[0:9] == "Translate") or (inp[0:9] == "translate") :
            Content = inp[10:]
            Stts.say("To what language?")
            Stts.write("To what language? Leave empty for using the default ({}) ".format(TDL))
            Desti = input("> ")
            if Desti == "" :
                Desti = TDL
                Dest = langs[TDL]
            else :
                for lang in langs.keys() :
                    if lang in Desti :
                        Dest = langs[lang]
            translist = STranslator.Translate(Content, Dest)
            Stts.say("{}, will be, {}, in {}".format(translist[1], translist[2], Desti))
            Stts.write("{} ~> {} ({})".format(translist[1], translist[2], Desti))

        #---
        elif (inp == MainName) or (inp == "sarah") :
            a = ["Yes, I'm here to help you", "Yes, Sir", "I'm right here"]
            print("{} {}".format(choice(a), _emoji))
        #---
        else :
            try:
                print(SWikipedia.Compliter(SWikipedia.Wikipedia(inp)))
                Morecheck = input("Type More to see the whole article ")
                if ("More" in Morecheck) or ("more" in Morecheck) or ("MORE" in Morecheck) :
                    print("Opening Browser ...")
                    ont(SWikipedia.GetURL(inp))
            except:
                print("I'm sorry I didn't understand what did you mean, and I couldn't find any match for in Wikipeia\
                    \nBut in still can search it for you in {}".format(DiffBrow))
                SearchAsk = input("Do You Want? ")
                if SearchAsk in YES :
                    print("Opening Browser ...")
                    url = "https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8".format(inp)
                    ont(url)


except (KeyboardInterrupt):
    print("\nSure, Closing ...")
    try :
        exit()
    except:
        quit()
