# AI-CHATBOT-WITH-NLP


## DESCRIPTION:

_**Spacy library doesn't support in my system, I have used google colab to work on chatbot, I have uploaded a googlecolab python chatbot downloaded file on this repositery**_

The code create a NLP Chatbot using a spacy library and google api for better search experience, In the code I have first imported necessary libraries- spacy, random, re, wikipedia, googlesearch, pyjokes, google genai.
_Spacy_ is used to create a pipeline that finds entity and other data from a entered query or sentence.
_Random_ is used to select random string from response dictionary's keys that respond for the entered query.
_Regular expression_ is used to search expressions or selected data from the entered query.
_Wikipedia_ is used to search for a query if searching for a entity or something.
_Google Search_ is used to return url of some data if user doesn't file relevant data from wikipedia.
_Google gemeni_ is the final search result responder to the user query if the wikipedia and google search dosen't work.
_Pyjokes_ is used for some humor.

I have created a response dictionary that have different keys of response and those keys have different values that will be return randomly from the list of key values.

After response there is Function called chatbot_response() that works the actual functionality of the chatbot, a while loop is started to operate or asks user to enter the next query, first return greeting, asks for your name, search for wikipedia, google etc. Here pyjokes is used for some humor.

Expression is used to search an particular expression in the entered query. 

## Output Image
![Image](https://github.com/user-attachments/assets/05f29f95-489a-4c89-aa78-9dc513d4f2b2)
