from Modules import STranslator, SWebscraper, SEmoji, SWikipedia
from Data import IntroOptions, langs
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

        elif inp[1:9] == "ranslate" :
            Content = inp[10:]
            Dest = input("To what language? Leave empty for using the default ({}) ".format(TDL))
            if Dest == "" :
                Dest = langs[TDL]
            else :
                for lang in langs.keys() :
                    if lang in Dest :
                        Dest = langs[lang]
            print(STranslator.Translate(Content, Dest))
        else :
            print(SWikipedia.Compliter(SWikipedia.Wikipedia(inp)))
            Morecheck = input()
            if "More" in Morecheck :
                ont(SWikipedia.GetURL(inp))

except (KeyboardInterrupt):
    print("\nClosing ...")
    exit()
