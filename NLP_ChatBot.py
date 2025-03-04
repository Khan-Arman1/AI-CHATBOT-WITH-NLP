# importing necessary library
import spacy
import random
import re
import wikipedia
import googlesearch
import pyjokes 
from google import genai


# google api key for better search experience
client = genai.Client(api_key="YOUR_API_KEY")

# creating object and loading pre-trianed model
nlp = spacy.load('en_core_web_sm')

# checking pipeline
nlp.pipe_names

# classifying responses
responses = {
    'greeting': ['Hello!', 'Hi there!', 'Hey! How can I assist you?'],
    'goodbye': ['Goodbye!', 'See you later!', 'Have a great day!'],
    'how are you': ['I\'m doing great, thank you for asking!', 'I\'m just a bot, but I\'m functioning well!'],
    'what is your name': ['I am a chatbot!\nCan I know you name.', 'I am your friendly chatbot!\nCan I know you name.'],
    'default': ['I\'m sorry, I didn\'t quite understand that. Could you please rephrase?'],
    'what are you': ['I\'m a chatbot ']
}


# creating function with all functionalities
def chatbot_response():
#   looping over the functionality
  while True:
      # takes user input
    user_input = input("You: ")
      # tokenizing the input with nlp pipeline 
    doc = nlp(user_input)

    # using regular expression for greeting
    expression = re.findall('hello|hi|hey|hy',user_input.lower())
      # if expression found the below code return a response
    if expression:
      print("Bot: ",responses['greeting'][random.randrange(0,len(responses['greeting']))])

    # recognizing user name
    for ent in doc.ents:
      expression = re.findall('my name|i\'m| i am',user_input.lower())
      if expression:
        print("Bot: ",f"Hello, {ent.text}\nHow can I assist you today?")

    # telling jokes
    expression = re.findall('joke|tell me a joke|tell joke',user_input.lower())
    if expression:
      print("Bot: ",pyjokes.get_joke())

    # splitting in different sentences
    sentences=[token.text.lower() for token in doc.sents]
    for i in sentences:

      # using regular expression for simple questions
      expression = re.findall('how.+you|you.*fine|you.*well|hope.*you.+well|feel.*good',i)
      if expression:
        print("Bot: ",responses['how are you'][random.randrange(0,len(responses['how are you']))])

      # using regular expression for simple questions
      expression = re.findall('.+ your name|who .+ you|what .+ you',i)
      if expression:
        print("Bot: ",responses['what is your name'][random.randrange(0,len(responses['what is your name']))])

      # searching for wikipedia
      expression = re.findall('who is.+|what is.+|explain.+|explain.+to.+me|elaborate.+|where does.+|when does.+|when did.+|when do.+|do .+|does .+',i)
      if expression:
        # performing search for entity
        for ent in doc.ents:

        # performing search throught wikipedia
          try:
            search_result = wikipedia.summary(i,sentences=2)
            print(f"Bot: Searching for {ent.text}\n",search_result)
          except:
            try:

              # checking for the organization or person
              search_data=nlp(i)
              for entity in search_data.ents:
                # entity if organisation
                if ent.label_ == 'ORG':
                    try:
                      for j in googlesearch.search(entity.text, tld=".org", num=5, stop=5, pause=2):
                        print("Bot: Searching for",entity.text,"|",j)
                        break
                    except:
                      for j in googlesearch.search(entity.text, tld="co.in", num=5, stop=5, pause=2):
                        print("Bot: Searching for",entity.text,"|",j)
                        break
                # entity if person
                if entity.label_ == "PERSON":
                    try:
                      for j in googlesearch.search(entity.text, tld="co.in", num=5, stop=5, pause=2):
                        print("Bot: Searching for",entity.text,"|",j)
                        break
                    except:
                      response = client.models.generate_content(model="gemini-1.5-flash", contents=i)
                      print("Bot: ",response.text)
                      break
            except:
              print("Bot: ",responses['default'][random.randrange(0,len(responses['default']))])

    if user_input.lower() == 'exit':
      print("Bot: ",responses['goodbye'][random.randrange(0,3)])
      break


# if main file excecutes the function call to awake the chatbot 
if __name__ == "__main__":
    chatbot_response()
