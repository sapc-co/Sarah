from Modules import STranslator, SWebscraper, SEmoji, SWikipedia
from Data import IntroOptions, langs, YES
from random import choice
from Setting import *
from nltk.tokenize import WordPunctTokenizer
import re 
from webbrowser import open_new_tab as ont

intro = choice(IntroOptions)
intro_emoji = ["wink", "v", "smile"]
_emoji = SEmoji.Emoji(choice(intro_emoji)) #making a random emoji
print("{} {}".format(intro, _emoji)) #introducing to user
#print("")
tokenizer = WordPunctTokenizer()

try :
    while True:
        inp = input("~> ")
        tokenizedinp = tokenizer.tokenize(inp)
        if inp is "" : # if 
            pass

        elif (inp[1:9] == "TRANSLATE") or (inp[1:9] == "Translate") or (inp[1:9] == "translate") :
            Content = inp[10:]
            Dest = input("To what language? Leave empty for using the default ({}) ".format(TDL))
            if Dest == "" :
                Dest = langs[TDL]
            else :
                for lang in langs.keys() :
                    if lang in Dest :
                        Dest = langs[lang]
            print(STranslator.Translate(Content, Dest))
        """ else :
            try:
                print(SWikipedia.Compliter(SWikipedia.Wikipedia(inp)))
                Morecheck = input()
                if "More" in Morecheck :
                    ont(SWikipedia.GetURL(inp)
                    
            except:
                print("I'm sorry I didn't understand what did you mean, and I couldn't find any match for in Wikipeia")
                SearchAsk = input("Do you want me to search it for you? ")
                if SearchAsk in YES :
                    print("Sure, Opening Browser")
                    ont(inp) """

except (KeyboardInterrupt):
    print("\nClosing ...")
    exit()
