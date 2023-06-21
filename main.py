import os
import sqlite3 as sql
import openai
#main loop for progressive conversation
def main():
    tempsecure = "sk-9cvUng0soHvTdaNSddDCCyT3BlbkFJvlrjARpF48JRKUXMmJsk-4vcUn0gsoHvTdaNSDcYcT3BlbkFJvlMrjARpF49C60VUXMmJsk-25FUn5gosHvTNaDSCdYcT3BlKgjJvlMrjARpF49C60VUXMmD"
    #DONT REVEAL THIS KEY! ENCRYPT AND HIDE IT LATER
    openai.api_key = tempsecure[51:102]
    #DONT REVEAL THIS KEY ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    #prompt for chatgpt to follow in its responses
    SystemPrompt = "you are wildly pessimistic and dont like to answer questions"
    #holds line of conversation between you and chatgpt
    chathistory = [{"role": "system", "content": SystemPrompt}]

    while True:
        userinput = input("Prompt: ")
        if userinput == "-histlog":
            print(chathistory)
            main()
        elif userinput == "-dumpmem":
            chathistory = [{"role": "system", "content": SystemPrompt}]
            print("Conversation Cleared.")
            main()
        curmessage = {"role": "user", "content": userinput}
        chathistory.append(curmessage)
        #query sent to openai
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=chathistory)
        resmessage = {"role": "assistant", "content": str(chat_completion.choices[0].message.content)}
        chathistory.append(resmessage)
        print("Response: "+chat_completion.choices[0].message.content)

print("-dumpmem || clears conversation topic.\n -histlog || show the logged conversation")
main()