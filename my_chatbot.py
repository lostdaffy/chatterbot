from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer  

import collections.abc
collections.Hashable = collections.abc.Hashable

import time 
time.clock = time.time

# creating a chatbot  
myBot = ChatBot(  
    name = 'lostdaffy',
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    database_uri = 'sqlite:///chatbot.sqlite3'
)
  

corpus_trainee = ChatterBotCorpusTrainer(myBot)  
corpus_trainee.train('chatterbot.corpus.english')  


while True:
    try:
        bot_input = myBot.get_response(input('>>'))
        print("Bot: ", bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
