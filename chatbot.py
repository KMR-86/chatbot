import nltk
#nltk.download()
#print("done downloading")
"""this is only used when someone is using nltk for the first time"""

import numpy as np
import random
import string

#corpus code
name_of_the_corpus="corpus-large.txt"
#name_of_the_corpus="corpus-medium.txt"
#name_of_the_corpus="corpus-small.txt"
f=open(name_of_the_corpus,'r',errors='ignore')
raw=f.read()
raw=raw.lower()
sent_tokens=nltk.sent_tokenize(raw)
word_tokens=nltk.word_tokenize(raw)


#WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [token for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))



GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
        
        
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2] # sorting the values and returning the index serial. it is a [[,,,]] matrix 
    # and getting [0][-2] means getting the second largest element's index in it's only row (0 th row). largest element is always 1 as userinput 
    # is inside sent_tokens
 
    flat = vals.flatten()
    #this line converts the 2d array into a 1d array. that means [[]] -> []

    flat.sort()
    req_tfidf = flat[-2] #second largest element of flat 1d matrix . 
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx][6:]
        return robo_response
    
    

flag=True
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("MARK: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("MARK: "+greeting(user_response))
            else:
                print("MARK: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("MARK: Bye! take care..")
