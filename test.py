# Import the necessary modules
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot
chatbot = ChatBot('MyBot')

# Train the chat bot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Get responses from chatbot
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("Bot: ", response)
