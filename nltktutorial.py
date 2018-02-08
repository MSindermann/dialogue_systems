# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 16:53:18 2018

@author: Marie
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from nltk.corpus import state_union

from nltk.chat.util import Chat, reflections



#########################################################
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

#print(sent_tokenize(EXAMPLE_TEXT))
#print(word_tokenize(EXAMPLE_TEXT))

#########################################################
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(EXAMPLE_TEXT)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

#print(word_tokens)
#print(filtered_sentence)

#########################################################
train_text = state_union.raw("2005-GWBush.txt")

punctuation = ['.', ',', ';']
no_punct = [x for x in word_tokenize(train_text) if not x in punctuation]

pairs = [
    [
        r'(.*)* my name is (.*)',
        ['hello %2',]
    ],
]
    
def hugot_bot():
    print("Hi, what is your name?")
    chat = Chat(pairs, reflections)
    chat.converse()
    
if __name__ == "__main__":
    hugot_bot()
