
from revChatGPT.V1 import Chatbot
import sys
import secure

def makeNovelApi(promp):
    access_token = secure.access_token
    chatbot = Chatbot(config={
    "access_token": access_token
    })

    prev_text = ""
    for data in chatbot.ask(promp):
        message = data["message"][len(prev_text) :]
        print(message, end="", flush=True)
        prev_text = data["message"]
    print()


if __name__ == '__main__':
    #makeNovelApi('what is 1+1?')
    makeNovelApi(sys.argv[1])
    







