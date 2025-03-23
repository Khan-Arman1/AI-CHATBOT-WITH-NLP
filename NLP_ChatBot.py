# importing necessary library
import random # for random answer
import spacy # for loading the pre trained model
import re # search specific syntax
import wikipedia # for simple searches
import pyjokes # for some humor
from google import genai # for better performance of the bot
from google.colab import userdata # to load the api keys from google colab
from datetime import datetime

# create a api instance
client = genai.Client(api_key=userdata.get('GOOGLEGEMINI_API_KEY'))

# load the instance of spacy pre trained model
nlp = spacy.load('en_core_web_sm')

# checking pipeline
nlp.pipe_names

# response data
responses = {
    'greeting': ['Hello!', 'Hi there!', 'Hey! How can I assist you?'],
    'goodbye': ['Goodbye!', 'See you later!', 'Have a great day!'],
    'how are you': ['I\'m doing great, thank you for asking!', 'I\'m just a bot, but I\'m functioning well!'],
    'what is your name': ['I am a chatbot!\nCan I know you name.', 'I am your friendly chatbot!\nCan I know you name.'],
    'default': ['I\'m sorry, I didn\'t quite understand that. Could you please rephrase?'],
    'what are you': ['I\'m a chatbot ']
}

def chatbot_response():

  while True:
    user_input = input("You: ")
    # create an nlp object
    doc = nlp(user_input)
    expression = re.findall('date|time|time.*now|day.*today',user_input.lower())
    if expression:
      print("Bot: ",datetime.ctime(datetime.now()))
    # using regular expression for greeting
    expression = re.findall('hello|hi|hey|hy',user_input.lower())
    if expression:
      print("Bot: ",responses['greeting'][random.randrange(0,len(responses['greeting']))])
    # recognizing user name
    for ent in doc.ents:
      expression = re.findall('my name is|i\'m| i am|My name is|Myname is|My nameis|Mynameis|mynameis|I\'m|Iam|I am',user_input)
      if expression:
        print("Bot: ",f"Hello, {ent.text}\nHow can I assist you today?")
    # telling jokes
    expression = re.findall('joke|tell me a joke|tell joke',user_input.lower())
    if expression:
      print("Bot: ",pyjokes.get_joke())
    # splitting in different sentences
    sentences=[token.text.lower() for token in doc.sents]
    for i in sentences:
      try:
        # simple question answering using wikipedia
        for ent in doc.ents:
          search_result = wikipedia.summary(i,sentences=2)
          print(f"Bot: Searching for {ent.text}\n",search_result)
      except:
        pass

      # using regular expression for simple questions
      expression = re.findall('how.+you|you.*fine|you.*well|hope.*you.+well|feel.*good',i)
      if expression:
        print("Bot: ",responses['how are you'][random.randrange(0,len(responses['how are you']))])
      # using regular expression for simple questions
      expression = re.findall('.+ your.*name|who.*are.*you|what.*are.*you',i)
      if expression:
        print("Bot: ",responses['what is your name'][random.randrange(0,len(responses['what is your name']))])

      # searching for wikipedia
      expression = re.findall('who is.+|what.*is.+|explain.+|explain.+to.+me|elaborate.+|where does.+|when does.+|when did.+|when do.+|do .+|does .+',i)
      if expression:
          try:
            # pass direct query to the gemini model for better result except passing into the chunks
              query = user_input
              response = client.models.generate_content(
                  model="models/gemini-1.5-flash",
                  contents=query+'\t answer me in 100 words',
              )
              print(response.text)
          except:
              print("Bot: ",responses['default'][random.randrange(0,len(responses['default']))])

    if user_input.lower() == 'exit':
      print("Bot: ",responses['goodbye'][random.randrange(0,3)])
      break

# if main file excecutes the function call to awake the chatbot 
if __name__ == "__main__":
    chatbot_response()
