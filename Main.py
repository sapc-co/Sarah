from Modules import STranslator, SWebscraper, SEmoji
from Data import intro_options
from random import choice as RC

intro = RC(intro_options)
intro_emoji = ["wink", "v", "smile", "heart"]
_emoji = SEmoji.Emoji(RC(intro_emoji))
print(intro + _emoji)
