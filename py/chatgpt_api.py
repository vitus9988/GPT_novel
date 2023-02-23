
from revChatGPT.V1 import Chatbot
import sys
import secure

def makeNovelApi(promp):
    access_token = secure.access_token
    chatbot = Chatbot(config={
    "access_token": access_token,
    "paid" : True
    })
    
    response = chatbot.ask(promp)
    gen = list(response)
    msg = gen[-1]
    return msg['message']

if __name__ == '__main__':
    #makeNovelApi('write 50 word novel, main theme: detective, sub theme: horor, language: korean')
    sentence = "write git actions workflow example sourcecode"
    result = makeNovelApi(sentence)
    print(result)
    #makeNovelApi(sys.argv[1])
    







