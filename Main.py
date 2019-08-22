from Modules import STranslator, SWebscraper, SEmoji
from Data import intro_options, langs
from random import choice
from Setting import *


intro = choice(intro_options)
intro_emoji = ["wink", "v", "smile"]
_emoji = SEmoji.Emoji(choice(intro_emoji))
print("{} {}".format(intro, _emoji))
print("")

try :
    while True:
        inp = input()

        if inp is "" :
            pass

        elif inp[1:9] == "ranslate" :
            Content = inp[10:]
            Dest = input("To what language? Leave empty to use Default({}) ".format(TDL))
            if Dest == "" :
                Dest = TDL
            else :
                for lang in langs.keys() :
                    if lang in Dest :
                        Dest = langs[lang]
            print(STranslator.Translate(Content, Dest))

except (KeyboardInterrupt):
    print("\nClosing ...")
    exit()
    