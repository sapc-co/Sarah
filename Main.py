from Modules import STranslator, SWebscraper, SEmoji
from Data import IntroOptions, langs
from random import choice
from Setting import *


intro = choice(IntroOptions)
intro_emoji = ["wink", "v", "smile"]
_emoji = SEmoji.Emoji(choice(intro_emoji)) #making a random emoji
print("{} {}".format(intro, _emoji)) #introducing to user
#print("")

try :
    while True:
        inp = input("~> ")

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

except (KeyboardInterrupt):
    print("\nClosing ...")
    exit()

#tars nadare ke by jadi (my teacher)
#meaning : No fear