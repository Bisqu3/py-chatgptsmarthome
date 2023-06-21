import os
import openai

#main loop for progressive conversation
def main():
    # Load your API key from an environment variable or secret management service
    openai.api_key = "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"
    #prompt for chatgpt to follow in its responses1
    SystemPrompt = "you are a helpful assistant"
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


main()