import urllib.parse
import requests

def sendMessage(message):
    bot_token = "5953645919:AAEU9QcdoE799ImWqaT6m5ezDgEYNQqt0E0"
    chat_id = "916444149"
    encoded_message = urllib.parse.quote_plus(message)
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={encoded_message}"
    requests.get(url)



mymsg = ""
#mymsg = "hi man\ni really need to thank you that you got it"


MsgVideos = []

MsgVideos.append('A ✅\n')
MsgVideos.append('B ✅\n')
MsgVideos.append('C ✅\n')
for x in MsgVideos:
    mymsg += x

mymsg += "Uploaded & Done Successfully 👍"

sendMessage(mymsg)
