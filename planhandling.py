# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:43:37 2018

@author: Marie
"""
import random
import todobot

def handle_plan(plan,index):
    response = "I'm very sorry, but I don't understand. No.: " + str(plan)
    
    GREETING_RESPONSES = ["Hello! How can I help you?", "Hey! Can I do something for you?", 
                          "Greetings! Please specify how I can help you",]
    APPLICATION_RES = ["So your question regards your application status?", 
                       "Do you have a problem with your application?"]
    if index == 1:
        if plan == 1:
            response = random.choice(GREETING_RESPONSES)
        if plan == 2:
            response = APPLICATION_RES[index]
    else:
        plan = plan_flag
         
        
  
    return response