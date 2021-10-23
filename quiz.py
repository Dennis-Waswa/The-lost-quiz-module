# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 12:42:29 2020

@author: Dennis Waswa
"""


import os, re 
import json
import random
from datetime import datetime

def get_available_data_files():   
    #Get all files ending with .json in my directory and return them as list
    path_json = [json_file for json_file in os.listdir() if re.search("\.json$",json_file)]
    json_string = [open(f"{path_json[i]}").read() for i in range(len(path_json))] 
    
    return json_string

def select_questions(fileList, n):
    path_json = [] #list of all questions 
    for string in fileList:
        x = json.loads(string)
        path_json.append(x)
    questionlist = [path_json[random.randint(0,3)]["results"]# get some random questions from the json file list and return 3 questions at a time
                        [random.randint(0,len(path_json[0]["results"])-1)] #to get random three questions at a time from the lenght of the all the list
                         for i in range(n) ]
    return questionlist

def shuffle_options(question):
    shuffle_x = [answer for answer in question['incorrect_answers']] #get incorrect answers and store them in a list
    shuffle_x.append(question['correct_answer']) #append correct answers to the correct answer list
    random.shuffle(shuffle_x) #shuffle both corect and incorrect answers  in the shuffle_x list
    return shuffle_x #return shuffled list with all possible answers 
    
def question_worth_points(question):  
    difficulty_x = question['difficulty'] #check the questions difficulty level
    if difficulty_x == 'easy': #for easy questions reward 50 points 
        return 50
    elif difficulty_x == 'medium': #for medium difficulty questions reward 100 points
        return 100
    else:
        return 150 #rewards 150 points to hard questions 
    
def calculate_total_achievable_points(questionlist):
    #get all possible achievable points for a given quesion 
    points = 0
    for question in questionlist:
        points += question_worth_points(question)
    return points
    
def calculate_achieved_points(question, user_selection, duration): 
    points = (question_worth_points(question)-duration) #checks points to be rewarded against time spend for the question 
    if points < 0: points = 0
    if user_selection == question['correct_answer']: #check user answer and if answer is correct it rewards points accordingly and shows user time spend for the question 
        print('Correct Answer {} provided in {}'.format(user_selection, duration))
        print('Points: {}'.format(points))
        return points
    else:
        print('Wrong Answer "{}" provided in {}'.format(user_selection, duration)) #returns if the user answer is incorrect
        print('Points: 0.00')
        return 0

def display_question(q):
    #display question, topic, and answer options to the user 
    print(f"Topic  {q['category']}")
    print(f"Worth points: {question_worth_points(q)}")
    print(f"{q['question']}")
    
    shuffle_x = shuffle_options(q)
    for x in range(4):
            print('\t'*4 + '{}. {}'.format(chr(65+x),shuffle_x[x]))
            
    #start time count down when user clicks enter 
    time_x = datetime.now() 
    while True: #to run until a user enters an answer 
        user = input('Enter your answer: ')
        #user selection from provided limit of choices 
        if re.match('[A-D]$', user) and len(shuffle_x)==4 or re.match('[AB]$',user) and len(shuffle_x)==2:
            #time lapses after user enters answer and breaks 
            time_y = datetime.now()  
            break
    print("."*30)
    #time calculation to get the time spend per question between user clicking ender and entering the answer
    total_time = time_y-time_x 
    sec_x = total_time.total_seconds()
    
    ord_int = ord(user)-65
    answer = shuffle_x[ord_int]
    
    return (answer,round(sec_x,2))
